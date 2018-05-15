import urllib2

def obtenir_assignatures():
	url_assig="https://raco.fib.upc.edu/api/horaris/assignatures-titulacio.txt?codi=GRAU"
	req_assig=urllib2.Request
	response_assig = urllib2.urlopen(url_assig)
	file_assig=open("assignatures_grau.txt", "w")
	file_assig.write(response_assig.read())
	file_assig.close()


def obtenir_informacio_assignatures():
	url_info_assig="https://raco.fib.upc.edu/api/horaris/horari-assignatures.txt?"
	obtenir_assignatures()
	file_assig=open("assignatures_grau.txt", "r")
	file_aux=open("horari_totes_assignatures", "w")
	suma="assignatures=" + file_assig.readline().rstrip('\n')
	for assig in file_assig:
		suma = suma	+ "&assignatures=" + assig.rstrip('\n')
	
	print(suma)
	#file_aux.write(suma)
	file_assig.close()
	file_aux.close()