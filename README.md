# PactContractTestingPOC


# Pre-requistes:
Python 3.7+
Pipenv or virtualenv for dependency management


# Installation

1. Clone the repository:
git clone https://github.com/ramgokul/PactContractTestingPOC.git
cd PactContractTestingPOC

2. Set up a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate  
pip install -r requirements.txt

# Example Flask API
This project includes a simple Flask API (provider.py) that can be used as a mock provider for contract testing. The API simulates a user service with basic functionality to retrieve user information.

# Running the Flask API
To run the Flask API:

Ensure you are in the virtual environment.

Run the Flask application using the command: python3 provider.py

The application will start on http://localhost:<port_number>. Make sure the port number you choose (in this example, 5003) is free and not used by other applications.

You can use this API as a mock provider in your contract tests. Modify the port argument in the app.run() method to use a different port if 5003 is not available.

# To run the consumer tests and generate a Pact file (i,e a JSON file):
python3 test_consumer.py

# To verify the provider against the generated Pact file:
python3 test_provider.py
