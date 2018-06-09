
def comprovar_si_aula_esta(llista_aules, aula):
	for elem in llista_aules:
		if (elem==aula):
			return True
	return False

def parse_per_aules():
	file_assig=open("horari_totes_assignatures.txt", "r")
	llista_aules_fib = []
	for assig in file_assig:
		llista_aula = assig.split()
		esta = comprovar_si_aula_esta(llista_aules_fib, llista_aula[len(llista_aula)-1])
		if (esta==False):
			llista_aules_fib.append(llista_aula[len(llista_aula)-1])
		file_bucle=open("./aules/" + llista_aula[len(llista_aula)-1] + ".txt","a")
		file_bucle.write(assig)
		file_bucle.close()

def ordenar_eliminar_duplicat_linies(elem):
	lista_definiciones=sorted(file("/home/pi/Documents/treball_fi_grau/TInfo/aules/" + elem + ".txt"))
	file("aux.txt","w").writelines(lista_definiciones)
	lines_seen = set() # holds lines already seen
	outfile = open(elem + ".txt", "w")
	for line in open("aux.txt", "r"):
		if line not in lines_seen: # not a duplicate
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	file_aula=open("/home/pi/Documents/treball_fi_grau/TInfo/"+ elem + ".txt", "r")
	return file_aula


