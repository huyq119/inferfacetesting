#   coding = utf-8

import requests

rep = requests.post("http://www.baidu.com?")
print rep.text