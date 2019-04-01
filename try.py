import re
import urllib.request

def outshape(data):
	with open("dbtest.txt","w",encoding='utf-8') as f:
		for d in data:
			print("\t".join(d))
			f.write("\t".join(d))

url = "http://unmsm.claro.net.pe/resultAdmin20192/A/011/0.html"

html = urllib.request.urlopen(url)
rd = html.read().decode('utf-8')

pattern = re.compile(r"<tr><td class=\"text-center\">(\d+)</td><td>([\w, ]+)</td><td class=\"text-center\">(\d+)</td><td class=\"text-center\">([&nbsp;]*|[\d\.]*)</td><td class=\"text-center\">([&nbsp;]*|[\d\.]*)</td><td class=\"text-center\">([&nbsp;|&nbsp;ALCANZO VACANTE|AUSENTE]*)</td></tr>")

data = pattern.findall(rd)


outshape(data)
print("Longitud -> ",len(data))



"""
with open('h.txt','w',encoding='utf-8') as f:
	f.write(rd)
"""