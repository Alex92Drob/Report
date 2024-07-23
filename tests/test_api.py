import pytest
from peewee import SqliteDatabase
from main_report_Alex_Drob.models import RacingReport
from main_report_Alex_Drob.app import create_app


@pytest.fixture
def test_client():
    test_database = SqliteDatabase(':memory:')
    app = create_app(database=test_database)
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            test_database.bind([RacingReport])
            test_database.create_tables([RacingReport])

            RacingReport.create(place='1.', abbr='SVF', name='Sebastian Vettel', car='FERRARI', time='0:01:04.415000')
            RacingReport.create(place='2.', abbr='VBM', name='Valtteri Bottas', car='MERCEDES', time='0:01:12.434000')

            yield app.test_client()
            test_database.drop_tables([RacingReport])
            test_database.close()


def test_api_report_data_json(test_client):
    response = test_client.get('/api/v1/report/?format=json')
    assert {
               "abbr": "SVF",
               "car": "FERRARI",
               "name": "Sebastian Vettel",
               "place": "1.",
               "time": "0:01:04.415000"
           } in response.json


def test_api_report_data_xml(test_client):
    response = test_client.get('/api/v1/report/?format=xml')
    assert '<name>Sebastian Vettel</name>' in response.text


def test_api_drivers_json(test_client):
    response = test_client.get('/api/v1/drivers/?format=json')
    assert {
               "abbr": "VBM",
               "name": "Valtteri Bottas"
           } in response.json


def test_api_drivers_xml(test_client):
    response = test_client.get('/api/v1/drivers/?format=xml')
    assert '<name>Valtteri Bottas</name>' in response.text


def test_api_driver_json(test_client):
    response = test_client.get('/api/v1/drivers/?driver_id=VBM&format=jsom')
    assert {
               "abbr": "VBM",
               "car": "MERCEDES",
               "name": "Valtteri Bottas",
               "place": "2.",
               "time": "0:01:12.434000"
           } in response.json


def test_api_driver_xml(test_client):
    response = test_client.get('/api/v1/drivers/?driver_id=SVF&format=xml')
    assert '<name>Sebastian Vettel</name>' in response.text
