import urllib.request
import re
host_root = "http://unmsm.claro.net.pe/resultAdmin20192"
main_url = "http://unmsm.claro.net.pe/resultAdmin20192/A.html"

def mapping(url):
	main_html = urllib.request.urlopen(url).read().decode('utf-8')
	links = re.findall(r"<a href=[\"\']([a-zA-Z0-9\./]*)[\"\']>",main_html)

	print("El tamaño es -> ",len(links))
	for link in links:
		print(link)
	return links

def eapcod(cadena):
	cod = re.search(r'\./\w+/(\d+)/0.html',cadena)
	return cod.group(1)

def transfer(html):
	pattern = re.compile(r"<tr><td class=\"text-center\">(\d+)</td><td>([\w, ]+)</td><td class=\"text-center\">(\d+)</td><td class=\"text-center\">([&nbsp;]*|[\d\.]*)</td><td class=\"text-center\">([&nbsp;]*|[\d\.]*)</td><td class=\"text-center\">([&nbsp;|&nbsp;ALCANZO VACANTE|AUSENTE]*)</td></tr>")
	data = pattern.findall(html)
	#print("Longitud data -> ",len(data))
	return data

def outshape(data):
	with open("database.txt","w",encoding='utf-8') as f:
		for d in data:
			#print("\t".join(d)+"\n")
			f.write("\t".join(d)+"\n")
		
if __name__ == "__main__":
	directory = {}
	eap_links = mapping(main_url)
	eap_cods = list(map(eapcod,eap_links))
	dataframe = []
	for suffix in eap_links:
		url_aux = host_root + suffix[1:]
		print(url_aux)
		pages = mapping(url_aux)
		directory[eap_cods[eap_links.index(suffix)]] = pages
	print("Scanning...")
	for cod, pages in directory.items():
		for page in pages:
			html_aux = urllib.request.urlopen(host_root+"/A/"+cod+"/"+page).read().decode('utf-8')
			dataframe += transfer(html_aux)
	print("Writing data...")
	outshape(dataframe)
	print("Completed :D")
	print("numero de postulantes -> ",len(dataframe))