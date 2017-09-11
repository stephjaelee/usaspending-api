from datetime import date
import json

from model_mommy import mommy
import pytest
from rest_framework import status

from usaspending_api.awards.models import Transaction, TransactionAssistance, TransactionContract
from usaspending_api.download.lookups import JOB_STATUS


@pytest.fixture
def award_data(db):

    # Populate job status lookup table
    for js in JOB_STATUS:
        mommy.make(
            'download.JobStatus',
            job_status_id=js.id,
            name=js.name,
            description=js.desc)

    # Create Locations
    loc1 = mommy.make('references.Location')

    # Create LE
    le1 = mommy.make('references.LegalEntity')

    # Create Awarding Top Agency
    ata1 = mommy.make(
        'references.ToptierAgency',
        name="Bureau of Things",
        cgac_code='100',
        website='http://test.com',
        mission='test',
        icon_filename='test')
    ata2 = mommy.make(
        'references.ToptierAgency',
        name="Bureau of Stuff",
        cgac_code='101',
        website='http://test.com',
        mission='test',
        icon_filename='test')

    # Create Awarding subs
    asa1 = mommy.make('references.SubtierAgency', name="Bureau of Things")

    # Create Awarding Agencies
    aa1 = mommy.make('references.Agency', id=1, toptier_agency=ata1, toptier_flag=False)
    aa2 = mommy.make('references.Agency', id=2, toptier_agency=ata2, toptier_flag=False)

    # Create Funding Top Agency
    fta = mommy.make(
        'references.ToptierAgency',
        name="Bureau of Money",
        cgac_code='102',
        website='http://test.com',
        mission='test',
        icon_filename='test')

    # Create Funding SUB
    fsa1 = mommy.make('references.SubtierAgency', name="Bureau of Things")

    # Create Funding Agency
    fa1 = mommy.make('references.Agency', id=3, toptier_flag=False)

    # Create Awards
    award1 = mommy.make(
        'awards.Award', category='contracts', awarding_agency=aa1)
    award2 = mommy.make(
        'awards.Award', category='contracts', awarding_agency=aa2)

    # Create Transactions
    tran1 = mommy.make(Transaction, award=award1)
    tran2 = mommy.make(Transaction, award=award2)

    # Create TransactionContract
    tc1 = mommy.make(TransactionContract, transaction=tran1, piid='tc1piid')
    tc2 = mommy.make(TransactionContract, transaction=tran2, piid='tc2piid')

    # Create TransactionAssistance
    ta1 = mommy.make(TransactionAssistance, transaction=tran1, fain='ta1fain')


@pytest.mark.skip
@pytest.mark.django_db
def test_download_transactions_v2_endpoint(client, award_data):
    """Test the transaction endpoint."""

    resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {},
            "columns": {}
        }))

    assert resp.status_code == status.HTTP_200_OK
    assert '.csv' in resp.json()['url']


@pytest.mark.skip
@pytest.mark.django_db
def test_download_transactions_v2_status_endpoint(client, award_data):
    """Test the transaction status endpoint."""

    dl_resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {},
            "columns": {}
        }))

    resp = client.get('/api/v2/download/status/?file_name={}'
                      .format(dl_resp.json()['file_name']))

    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['total_rows'] == 3
    assert resp.json()['total_columns'] > 100


@pytest.mark.django_db
def test_download_transactions_v2_endpoint_column_limit(client, award_data):
    """Test the transaction status endpoint's col selection."""

    # columns from both transaction_contract and transaction_assistance
    dl_resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {},
            "columns": ["piid", "fain"]
        }))
    resp = client.get('/api/v2/download/status/?file_name={}'
                      .format(dl_resp.json()['file_name']))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['total_rows'] == 3
    assert resp.json()['total_columns'] == 2


    # columns only from transaction_contract
    dl_resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {},
            "columns": ["piid", "naics", "idv_type"]
        }))
    resp = client.get('/api/v2/download/status/?file_name={}'
                      .format(dl_resp.json()['file_name']))
    assert resp.status_code == status.HTTP_200_OK
    # columns from both transaction_contract and transaction_assistance
    assert resp.json()['total_rows'] == 2
    assert resp.json()['total_columns'] == 3


@pytest.mark.django_db
def test_download_transactions_v2_endpoint_column_filtering(client, award_data):
    """Test the transaction status endpoint's filtering."""

    dl_resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {"agencies": [{'type': 'awarding', 'tier': 'toptier', 'name': "Bureau of Things", }, ]},
            "columns": ["piid", "fain"]
        }))
    resp = client.get('/api/v2/download/status/?file_name={}'
                      .format(dl_resp.json()['file_name']))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['total_rows'] == 2

    dl_resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {"agencies": [{'type': 'awarding', 'tier': 'toptier', 'name': "Bureau of Stuff", }, ]},
            "columns": ["piid", ]
        }))
    resp = client.get('/api/v2/download/status/?file_name={}'
                      .format(dl_resp.json()['file_name']))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['total_rows'] == 1

    dl_resp = client.post(
        '/api/v2/download/transactions',
        content_type='application/json',
        data=json.dumps({
            "filters": {"agencies": [{'type': 'awarding', 'tier': 'toptier', 'name': "Bureau of Stuff", },
                                     {'type': 'awarding', 'tier': 'toptier', 'name': "Bureau of Things", },]},
            "columns": ["piid", "fain", ]
        }))
    resp = client.get('/api/v2/download/status/?file_name={}'
                      .format(dl_resp.json()['file_name']))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['total_rows'] == 3
