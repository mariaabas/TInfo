
def comprovarSiAulaEsta(llistaAules, aula):
	for elem in llistaAules:
		if (elem==aula):
			return True
	return False

def parsePerAules():
	fileAssig=open("horari_totes_assignatures.txt", "r")
	llistaAulesFib = []
	for assig in fileAssig:
		llistaAula = assig.split()
		esta = comprovarSiAulaEsta(llistaAulesFib, llistaAula[len(llistaAula)-1])
		if (esta==False):
			llistaAulesFib.append(llistaAula[len(llistaAula)-1])
		fileBucle=open("./aules/" + llistaAula[len(llistaAula)-1] + ".txt","a")
		fileBucle.write(assig)
		fileBucle.close()

def ordenarEliminarDuplicatLinies(elem):
	listaAssignatures=sorted(file("/home/pi/Documents/treball_fi_grau/TInfo/aules/" + elem + ".txt"))
	file("aux.txt","w").writelines(listaAssignatures)
	liniesVistes = set()
	fileSortida = open("/home/pi/Documents/treball_fi_grau/TInfo/aules/" + elem + ".txt", "w")
	for linia in open("aux.txt", "r"):
		if linia not in liniesVistes: 
			fileSortida.write(linia)
			liniesVistes.add(linia)
	fileSortida.close()
	fileAula=open("/home/pi/Documents/treball_fi_grau/TInfo/aules/" + elem + ".txt", "r")
	return fileAula


