
def comprovar_si_aula_esta(llista_aules, aula):
	for elem in llista_aules:
		if (elem==aula):
			return True
	return False

def parse_per_aules():
	file_assig=open("horari_totes_assignatures", "r")
	llista_aules_fib = []
	for assig in file_assig:
		llista_aula = assig.split()
		esta = comprovar_si_aula_esta(llista_aules_fib, llista_aula[len(llista_aula)-1])
		if (esta==False):
			llista_aules_fib.append(llista_aula[len(llista_aula)-1])
		file_bucle=open("./aules/" + llista_aula[len(llista_aula)-1] + ".txt","a")
		file_bucle.write(assig)
		file_bucle.close()


	#split la funció que ajuda a treure els espais
	#aula = assig.split()


