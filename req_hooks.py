import sys
from functools import partial

import requests


# https://alexwlchan.net/2017/10/requests-hooks/
def check_for_errors(resp, *args, **kwargs):
    resp_json = resp.json()
    if not resp_json['status']:
        sys.exit(resp_json)


requests_post = partial(requests.post, hooks={'response': check_for_errors})
