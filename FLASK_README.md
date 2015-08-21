# Overview

The Flask example (`flask_example.py`) has been tested with Flask version
0.10.1 on both Python 2.7.10 and Python 3.4.3.

## Setup

First, install the required Python modules:

```console
pip install -r requirements.txt
```

You should, of course, also have Flask installed. If you don't, install it with
`pip install flask`.

### Configure your Layer app

There are 3 constants that you must be set in layer.py, all of which are
available in the **Keys** section of the Layer dashboard for your app.

* `PROVIDER_ID` - Provider ID found in the Layer Dashboard under
"Keys"
* `KEY_ID` - Public key generated and stored in the Layer Dashboard under
"Keys"
* `RSA_KEY_PATH` - Path to the file containing the private key associated with
the public key

## Running the sample

1. Open two terminal windows.
2. In the first, start the app:

  ```console
  python flask_example.py```

  You should see:

   ```console
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```

3. Now, in the second terminal window, send an example request:

  ```console
  curl                          \
  -D -                          \
  -X POST                       \
  -d "nonce=1" -d "user_id=1"   \
  http://127.0.0.1:5000/identity_token```

  You will see something similar to the following:

  ```console
  HTTP/1.0 200 OK
  Content-Type: application/json
  Content-Length: 371
  Server: Werkzeug/0.10.4 Python/2.7.10
  Date: <LOCAL DATE / TIME>

  {"identity_token": ...SNIP...}```

  The value of the `identity_token` key is what you will provide back to the
  Layer SDK to complete authentication in your app.

## Verify

You should verify the output of the signing request by visiting the **Tools**
section of the [Layer dashboard](https://developer.layer.com/dashboard/).
Paste the value of the `identity_token` key you received from the output above
and click `validate`. You should see "Token valid".
