import sys
from functools import partial

import requests
from requests import Response

from api_urls import ApiUrls
from secrets import Secrets


# https://alexwlchan.net/2017/10/requests-hooks/
def check_for_errors(resp, *args, **kwargs):
    resp_json = resp.json()
    if not resp_json['status']:
        sys.exit(resp_json)


requests_post = partial(requests.post, hooks={'response': check_for_errors})

if __name__ == '__main__':
    # https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    data = {'uname': Secrets.uname, 'password': Secrets.get_pass_b64(), 't': 'true'}
    r: Response = requests_post(ApiUrls.fanyalogin, data=data)

    r_cookies = r.cookies
    r: Response = requests_post(ApiUrls.getNoticeCount, cookies=r_cookies)
    print(r.json())
