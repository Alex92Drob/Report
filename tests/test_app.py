import pytest
from bs4 import BeautifulSoup
from main_report_Alex_Drob.app import app


@pytest.fixture()
def test_client():
    app.testing = True
    yield app.test_client()


def test_homepage_asc(test_client):
    response = test_client.get('/?order=asc')
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.find_all('td', {'class': 'racer.name'})
    expected_drivers = {'Sebastian Vettel', 'Valtteri Bottas', 'Stoffel Vandoorne', 'Kimi Räikkönen', 'Fernando Alonso',
                        'Charles Leclerc', 'Sergio Perez', 'Romain Grosjean', 'Pierre Gasly', 'Carlos Sainz',
                        'Nico Hulkenberg', 'Brendon Hartley', 'Marcus Ericsson', 'Lance Stroll', 'Kevin Magnussen',
                        'Daniel Ricciardo', 'Lewis Hamilton', 'Esteban Ocon', 'Sergey Sirotkin'}
    assert all([i.text in expected_drivers for i in res])


def test_homepage_desc(test_client):
    response = test_client.get('/?order=desc')
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.find_all('td', {'class': 'racer.name'})
    expected_drivers = {'Daniel Ricciardo', 'Lewis Hamilton', 'Esteban Ocon', 'Sergey Sirotkin', 'Kevin Magnussen',
                        'Lance Stroll', 'Marcus Ericsson', 'Brendon Hartley', 'Nico Hulkenberg', 'Carlos Sainz',
                        'Pierre Gasly', 'Romain Grosjean', 'Sergio Perez', 'Charles Leclerc', 'Fernando Alonso',
                        'Kimi Räikkönen', 'Stoffel Vandoorne', 'Valtteri Bottas', 'Sebastian Vettel'}
    assert all([i.text in expected_drivers for i in res])


def test_drivers(test_client):
    response = test_client.get('/drivers')
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.find_all('td', {'class': 'racer.name'})
    expected_drivers = {'Sebastian Vettel', 'Valtteri Bottas', 'Stoffel Vandoorne', 'Kimi Räikkönen', 'Fernando Alonso',
                        'Charles Leclerc', 'Sergio Perez', 'Romain Grosjean', 'Pierre Gasly', 'Carlos Sainz',
                        'Nico Hulkenberg', 'Brendon Hartley', 'Marcus Ericsson', 'Lance Stroll', 'Kevin Magnussen',
                        'Daniel Ricciardo', 'Lewis Hamilton', 'Esteban Ocon', 'Sergey Sirotkin'}
    assert all([i.text in expected_drivers for i in res])


def test_driver_info(test_client):
    response = test_client.get('/drivers?driver_id=SVF')
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.find_all('td', {'class': 'racer.name'})
    expected_drivers = {'Sebastian Vettel'}
    assert all([i.text in expected_drivers for i in res])
