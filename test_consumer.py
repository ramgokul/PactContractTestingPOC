import pytest
from pactman import Consumer, Provider
import requests

pact = Consumer('UserServiceConsumer').has_pact_with(Provider('UserServiceProvider'), port=1234)


@pytest.fixture
def client():
    return requests.Session()


def test_get_user(client):
    expected = {
        'username': 'pat',
        'fullname': 'Pat Dorsy'
    }

    with pact:
        (pact
            .given('the user "pat" exists')
            .upon_receiving('a request for user with username "pat"')
            .with_request('get', '/users/pat')
            .will_respond_with(200, body=expected))

        response = client.get('http://localhost:1234/users/pat')
        assert response.status_code == 200
        assert response.json() == expected
