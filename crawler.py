import urllib
from urllib.request import urlopen
from requests import get
import re
import os

SITE_PATH = 'http://www.mavericktheater.com/assets/images/'
REGEX_EXPRESSION = 'href=.*?">'

# 현재 폴더 경로
NOW_PATH = os.getcwd()


# 사진 다운받는 함수
def download(url):

    filename = url.split('/')[-1]

    try:
        with open(filename, "wb") as file:
            res = get(url)
            file.write(res.content)
            file.close()

    except FileNotFoundError:
        pass


with urlopen(SITE_PATH) as response:
    html = response.read()

# 다운된 파일 저장을 위한 download 폴더 생성
if not (os.path.isdir('download')):
    os.makedirs(os.path.join('download'))

# 현재 경로를 download 폴더로 바꾸기
os.chdir(NOW_PATH + '/download')

# 크롤링해온 html 코드에 정규표현식 적용하여 파일 이름들 얻기
regex = re.compile('{}'.format(REGEX_EXPRESSION))
matchobj = regex.finditer(str(html))

# 파일 이름 통해 사이트에서 다운받기
for r in matchobj:
    file_name = (r.group())[6:-2]
    if file_name[0] == '?':
        pass

    elif file_name[-1] == '/':
        pass

    else:
        urllib.request.urlretrieve(SITE_PATH + file_name, file_name)
