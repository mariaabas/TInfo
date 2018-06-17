import urllib2
import json
import constants



def obtenirAssignaturesFormaTxt():
	reqAssig=urllib2.Request(constants.URL_ASSIG)
	responseAssig = urllib2.urlopen(reqAssig)
	fileAssig=open("assignatures_grau.txt", "w")
	fileAssig.write(responseAssig.read())
	fileAssig.close()

def obtenirAssignaturesJson():
	reqAssig=urllib2.Request(constants.URL_ASSIG_JSON)
	opener = urllib2.build_opener()
	f=opener.open(reqAssig)
	if (f.getcode() == 200):
		jsonResult=json.loads(f.read())
		primerElementJson = True
		concatenacio="assignatures=GRAU-"
		for assig in jsonResult:
			print(assig)
			if (primerElementJson==True):
				primerElementJson = False
				concatenacio = concatenacio + assig['idAssig']
			else:
				concatenacio=concatenacio + "&assignatures=GRAU-" + assig['idAssig']
		return concatenacio
	else:
		print("[ERROR] No s'ha realitzat correctament la crida obtenirAssignaturesJson : " + str(f.getcode()))
		return "ERROR"


def obtenirInformacioAssignatures():
	fileAux=open("horari_totes_assignatures.txt", "w")
	concatenacio=obtenirAssignaturesJson()
	if (concatenacio != "ERROR"):
		urlUnio=constants.URL_INFO_ASSIG+concatenacio
		req=urllib2.Request(urlUnio)
		response = urllib2.urlopen(req)
		if (response.getcode() == 200): 
			fileAux.write(response.read())
			fileAux.close()
			return response.getcode()
		else:
			print("[ERROR] No s'ha realitzat correctament la crida: " + response.getcode())
			return response.getcode()
	else:
		return concatenacio
