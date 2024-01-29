# BleuApiClientV2

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

BleuApiClientV2 is a Python client for interacting with the Faceki API. It provides convenient methods for tasks such as KYC verification, face matching, and more.

## Installation

You can install this package using `pip`:

```bash
pip install bleu-api-client
```

## Usage

To use the BleuApiClientV2 in your Python project, you need to create an instance of the `BleuApiClientV2` class, providing your client ID and client secret. Once initialized, you can call methods to interact with the Faceki API.

Here's an example of how to get started:

```python
from bleu_api.client import BleuApiClientV2

# Initialize the client with your client ID and client secret
client = BleuApiClientV2(client_id='your_client_id', client_secret='your_client_secret')

# Get an access token
access_token = client.generate_token()

# Perform a single KYC verification
response = client.requestKYC(
    selfie_image='path/to/selfie_image.jpg',
    doc_front_image='path/to/doc_front.jpg',
    doc_back_image='path/to/doc_back.jpg'
)

# Check the response
if response:
    print(response)
    # Process the verification results as needed

# Continue using other methods as needed
```

## API Endpoints

The `BleuApiClientV2` provides methods for interacting with various API endpoints. Refer to the [API_ENDPOINTS](#api-endpoints) section in the code for the available endpoints.

## Response Codes

The `BleuApiClientV2` includes a set of predefined response codes to help you interpret the results of your API requests. These codes are available as a dictionary under the `RESPONSE_CODES` class variable.

## Configuration

You can configure the client by modifying its class variables, such as `BASE_URL` or adding new API endpoints and response codes as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions to this project are welcome. Please refer to the [CONTRIBUTING](CONTRIBUTING.md) guidelines for more information on how to contribute.

```

Make sure to replace 'your_client_id' and 'your_client_secret' with your actual credentials. Feel free to add more details or examples to the README file as needed.# bleu-api-client
