import re
import time
import requests
from bs4 import BeautifulSoup

with open('requirements.txt', 'r') as f:
    packageList = f.read().splitlines()


for package in packageList:
    packageName, file_version = package.split("==")
    url = "https://pypi.org/project/" + packageName + "/"

    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    soup_version = str(soup.find("p", {"class": "release__version"}))  # Get version in soup html

    scrap_version = re.findall("\d.+", soup_version)[0]

    if file_version == scrap_version:
        msg = ("[%s] 현재 버전은 %s 이며, 최신 버전입니다." % (packageName, file_version))
        print(msg)
    else:
        msg = ("[%s] 현재 버전은 %s 이며, 최신 버전은 %s 입니다." % (packageName, file_version, scrap_version))
        print(msg)
        # API

    time.sleep(10)  # requests 딜레이

