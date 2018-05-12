# -*- coding: utf-8 -*-

import re
import  requests

def get_xsrf(session):
    index_url = r"http://www.zhihu.com"
    index_page = session.get( index_url,headers = headers)
    html = index_page.text
    print(html)
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf =re.findall(pattern,html)
    print(_xsrf)
    return _xsrf[0]

agent = "Mozilla/5.0 (Windows NT 10.0; rv:59.0) Gecko/20100101 Firefox/59.0"
headers = {  "User-Agent":agent }

session = requests.session()
_xsrf = get_xsrf(session)
post_url = "http://www.zhihu.com/login/phone_num"
post_data = {
    "_xsrf":_xsrf,
    "password":"12ER56YU",
    "remember_me":"true",
    "phone_num":"13112809608"
}
login_page = session.post(post_url,data=post_data,headers=headers)
login_code = login_page.text
print(login_code.status_code)
print(login_code)



