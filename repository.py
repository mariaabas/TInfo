import requests

def obtenir_assignatures():
	url_assig="https://raco.fib.upc.edu/api/horaris/assignatures-titulacio.txt
	req_assig=requests.get(url_assig)
	file_assig=open("assignatures_grau.txt", "w")
	file_assig.write(res_assig.read())
	file_assig.close()
	return file_assig

def obtenir_informacio_assignatures():
	url_info_assig="https://raco.fib.upc.edu/api/horaris/horari-assignatures.txt?"
	file_assig=obtenir_assignatures()
	for assig in file_assig.readline()
		print(assig)
