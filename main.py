from secrets import Secrets

if __name__ == '__main__':
    # https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    # r: Response = requests.post(ApiUrls.fanyalogin, data={'key': 'value'})

    print(Secrets.uname)
    print(Secrets.password)
    print(Secrets.get_pass_b64())
