import requests
from requests import Response

from api_urls import ApiUrls
from secrets import Secrets

if __name__ == '__main__':
    # https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    data = {'uname': Secrets.uname, 'password': Secrets.get_pass_b64(), 't': 'true'}
    r: Response = requests.post(ApiUrls.fanyalogin, data=data)

    r_json = r.json()
    if not r_json['status']:
        print(r_json)
        exit(r.status_code)

    r_cookies = r.cookies
    r: Response = requests.post(ApiUrls.getNoticeCount, cookies=r_cookies)
    print(r.json())
