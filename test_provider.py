import json
import subprocess
import time

import pytest
import requests
from pactman.verifier.verify import ProviderStateMissing

PACT_FILE = 'UserServiceConsumer-UserServiceProvider-pact.json'


@pytest.fixture(scope="module")
def provider_service():
    # Start the provider service
    process = subprocess.Popen(['python', 'provider.py'])
    time.sleep(2)  # Give the server some time to start

    yield 'http://localhost:5003'

    # Terminate the provider service after the test completes
    process.terminate()
    process.wait()


def test_provider(provider_service):
    # Load the pact file
    with open(PACT_FILE) as f:
        pact = json.load(f)

    # Verify the interactions and provider states
    for interaction in pact['interactions']:
        method = interaction['request']['method']
        path = interaction['request']['path']
        expected_status = interaction['response']['status']
        expected_body = interaction['response'].get('body')
        provider_state = interaction['providerState']

        try:
            response = requests.request(method, provider_service + path)
            response.raise_for_status()
            assert response.status_code == expected_status
            if expected_body:
                assert response.json() == expected_body
        except ProviderStateMissing:
            raise AssertionError(f'Provider state "{provider_state}" missing')

