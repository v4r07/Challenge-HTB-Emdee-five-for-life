import hashlib
import requests
from bs4 import BeautifulSoup

url_from_site = input("[+]: URL :")

sess = requests.session()

requete = sess.get(url_from_site).text
soup = BeautifulSoup(requete, 'html.parser')

for body in soup.find_all('body'):
	test = body.h3.text
	print("String: ", test)

hash_object = hashlib.md5(test.encode())
md5_hash = hash_object.hexdigest()
print("String en MD5: ", md5_hash)

requete2 = sess.post(url_from_site, data = {'hash':md5_hash})
print(requete2.text)