import requests
from bs4 import BeautifulSoup


i=15									       #Starts from 15 , earlier pages do not exist
while i <= 4225:
	url_cnh = "http://explosm.net/comics/" + str(i)
	r1 = requests.get(url_cnh)
	if r1.status_code == 200:
		soup = BeautifulSoup(r1.text,"html.parser")
		file_link = soup.find(id="main-comic")['src']
		if file_link[0]!= "h":						#Some links have http: while some dont				
			file_link = "http:" + file_link
		file_name = 	file_link.split('/')[-1]
		r2 = requests.get(file_link)
		if r2.status_code == 200:
			f = open("cnh/" + str(i) + "___" + file_name, "wb")
			f.write(r2.content)
			f.close()
		print(url_cnh)	
	i=i+1
	
