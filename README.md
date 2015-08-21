# Overview

The code in this folder provides examples for creating a Layer Identity Token
for both the Flask and Django web frameworks.

Each example shows how to create an endpoint, `identity_token`, that requires
the following parameters:

* `user_id`:  The user ID of the user you want to authenticate.
* `nonce`: The nonce you receive from Layer. See [docs](https://developer.layer.com/docs/guide#authentication) for more info.

#### Response

Upon success, the endpoint will return a JSON object that contains a single key, `identity_token`. If the required input parameters were not provided, the
endpoint will respond with "Invalid response."

Example successful response:

```json
{
"identity_token": "eyJ0eXAiOiJKV1Mi..."
}
```

### Python setup

For both examples, you need to first install the required Python libraries:

* PyJWT - The officially supported JWT library for Python
* pycrypto - Provides RSA signing capabilities for PyJWT

To install these modules, run the following command:

```console
pip install -r requirements.txt
```

_Note: the `pip` command may be `pip3` if you are running Python 3.0+._

### Configure your Layer app

To run either example, there are 3 constants that you should set in layer.py,
all of which are available in the **Keys** section of the Layer dashboard for
your app.

* `PROVIDER_ID` - Provider ID found in the Layer Dashboard under
"Keys"
* `KEY_ID` - Public key generated and stored in the Layer Dashboard under
"Keys"
* `RSA_KEY_PATH` - Path to the file containing the private key associated with
the public key

### Detailed instructions

* Django - see [DJANGO_README.md](DJANGO_README.md) for instructions
* Flask - see [FLASK_README.md](FLASK_README.md) for instructions
