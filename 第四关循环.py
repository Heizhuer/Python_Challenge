import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

# response = requests.get(url)
# html = response.content.decode('utf-8')
#
# a = re.findall('<a href="linkedlist.php\?nothing=(.*?)"', html)
# a = '12345'
# id = ''.join(a)
id = '8022'


def about_result(id):
    print(url + '?nothing=' + id)
    html = requests.get(url + '?nothing=' + str(id)).content.decode('utf-8')
    next_id = re.findall('\d{1,5}', html)
    # print(next_id)
    if not next_id:
        print(html)
    else:
        about_result(''.join(next_id))


about_result(id)

# '16044: Yes. Divide by two and keep going.'
# result = 'peak.html'
# 第五关链接: http://www.pythonchallenge.com/pc/def/peak.html
