import requests
from requests import Response

from api_urls import ApiUrls
from secrets import Secrets

if __name__ == '__main__':
    # https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    data = {'uname': Secrets.uname, 'password': Secrets.get_pass_b64(), 't': 'true'}
    r: Response = requests.post(ApiUrls.fanyalogin, data=data)

    print(r.text)
