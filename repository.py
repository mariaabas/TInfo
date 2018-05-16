import urllib2
import json

URL_ASSIG="https://raco.fib.upc.edu/api/horaris/assignatures-titulacio.txt?codi=GRAU"
URL_INFO_ASSIG="https://raco.fib.upc.edu/api/horaris/horari-assignatures.txt?"
URL_ASSIG_JSON="https://raco.fib.upc.edu/api/assignatures/llista.json"


def obtenir_assignatures_txt():
	req_assig=urllib2.Request(URL_ASSIG)
	response_assig = urllib2.urlopen(req_assig)
	file_assig=open("assignatures_grau.txt", "w")
	file_assig.write(response_assig.read())
	file_assig.close()

def obtenir_assignatures_json():
	req_assig=urllib2.Request(URL_ASSIG_JSON)
	opener = urllib2.build_opener()
	f=opener.open(req_assig)
	json_result=json.loads(f.read())
	primer = True
	url="assignatures=GRAU-"
	for assig in json_result:
		if (primer==True):
			primer = False
			url = url + assig['idAssig']
		else:
			url=url + "&assignatures=GRAU-" + assig['idAssig']
	return url

def obtenir_informacio_assignatures():
	file_aux=open("horari_totes_assignatures.txt", "w")
	concatenacio=obtenir_assignatures_json()
	url_unio=URL_INFO_ASSIG+concatenacio
	req=urllib2.Request(url_unio)
	response = urllib2.urlopen(req)
	file_aux.write(response.read())
	file_aux.close()