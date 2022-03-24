from requests import Response

from api_urls import ApiUrls
from req_hooks import requests_post
from secrets import Secrets

if __name__ == '__main__':
    # https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    data = {'uname': Secrets.uname, 'password': Secrets.get_pass_b64(), 't': 'true'}
    r: Response = requests_post(ApiUrls.fanyalogin, data=data)

    r_cookies = r.cookies
    r: Response = requests_post(ApiUrls.getNoticeCount, cookies=r_cookies)

    r_json_count = r.json()['count']
    if r_json_count != 0:
        print('New messages! ')
