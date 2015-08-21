# Overview

The Django sample (`django_example.py`) provides a view that can be added to an existing Django project's views.

This sample has been tested with Django 1.8.3 on both Python 2.7.10 and Python 3.4.3.

## Setup

First, install the required Python modules:

```console
pip install -r requirements.txt
```

### Configure your Layer app

There are 3 constants that you should set in layer.py, all of which are available in the **Keys** section of the Layer dashboard for your app.

* `PROVIDER_ID` - Provider ID found in the Layer Dashboard under "Keys"
* `KEY_ID` - Public key generated and stored in the Layer Dashboard under "Keys"
* `RSA_KEY_PATH` - Path to the file containing the private key associated with the public key

## Implementing the view

1. Add the code in `django_example.py` to an existing app's view in your Django project.
2. Update urls.py to reference the `get_identity_token` method to an endpoint of your choice, e.g.

```python
# urls.py

# import the views for your target app
from myapp import views

# expose the method
...
url(r'^identity_token/', views.get_identity_token, name='identity_token')
...
```

## Running the sample

1. Open two terminal windows
2. In the first, run your sample with:

  ```console
  python manage.py runserver
  ```

  You should see the server start:

  ```console
  Performing system checks...

  System check identified no issues (0 silenced).

  August 03, 2015 - 23:15:28
  Django version 1.8.3, using settings 'layer.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```

3. Now, in the second terminal window, send an example request:

  ```console
  curl                          \
  -D -                          \
  -X POST                       \
  -d "nonce=1" -d "user_id=1"   \
  http://127.0.0.1:8000/identity_token/```

  You should see something similar to the following:

  ```console
  HTTP/1.0 200 OK
  Date: Mon, 03 Aug 2015 23:16:04 GMT
  Server: WSGIServer/0.1 Python/2.7.10
  X-Frame-Options: SAMEORIGIN
  Content-Type: application/json

  {"identity_token": "...SNIP..."}
  ```

## Verify

You should verify the output of the signing request by visiting the **Tools**
section of the [Layer dashboard](https://developer.layer.com/dashboard/).
Paste the value of the `identity_token` key you received from the output above
and click `validate`. You should see "Token valid".
