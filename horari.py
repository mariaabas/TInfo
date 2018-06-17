import epd7in5b
import Image
import ImageDraw
import ImageFont
import constants
import parse as parsejar_info

def crearLlistaTupla(llarg, alt):
	llista = []
	llista.append(llarg)
	llista.append(alt)
	tupla = tuple(llista)
	return tupla

def crearLlistaTuplaDies():
	llarg = constants.LLARGADA
	alt = constants.ALTURA+constants.ESPAI_Y
	llistaPosDies=[]
	for dia in constants.LIST_DIES:
		llistaPosDies.append(crearLlistaTupla(llarg, alt))
		llarg=llarg+constants.ESPAI_X 
	return llistaPosDies

def crearLlistaTuplaHores():
	alt=constants.ALTURA+constants.ESPAI_Y
	llistaPosHores=[]
	for hora in constants.LIST_HORES:
		alt = alt+25
		llistaPosHores.append(crearLlistaTupla(10, alt))
	return llistaPosHores

def pintarDiesSetmana(draw, font_lletra):
	llarg = constants.LLARGADA
	alt = constants.ALTURA+constants.ESPAI_Y
	for dia in constants.LIST_DIES:
		draw.text((llarg, alt), dia, font= font_lletra, fill=constants.NEGRE)
		llarg=llarg+constants.ESPAI_X 
	return draw

def pintarHores(draw, fontLletra):
	alt=constants.ALTURA+constants.ESPAI_Y
	for hora in constants.LIST_HORES:
		alt = alt+25
		draw.text((10, alt), hora, font= fontLletra, fill=constants.NEGRE)
	return draw

def obtenirLlarg(llistaTuplaDies, llistaAula):
	return llistaTuplaDies[int(llistaAula[2])-1][0]

def obtenirAlt(llistaTuplaHores, llistaAula):
	hora = llistaAula[3]
	if (hora == '08:00'):
		return llistaTuplaHores[0][1]
	if (hora == '09:00'):
		return llistaTuplaHores[1][1]
	if (hora == '10:00'):
		return llistaTuplaHores[2][1]
	if (hora == '11:00'):
		return llistaTuplaHores[3][1]
	if (hora == '12:00'):
		return llistaTuplaHores[4][1]
	if (hora == '13:00'):
		return llistaTuplaHores[5][1]
	if (hora == '14:00'):
		return llistaTuplaHores[6][1]
	if (hora == '15:00'):
		return llistaTuplaHores[7][1]
	if (hora == '16:00'):
		return llistaTuplaHores[8][1]
	if (hora == '17:00'):
		return llistaTuplaHores[9][1]
	if (hora == '18:00'):
		return llistaTuplaHores[10][1]
	if (hora == '19:00'):
		return llistaTuplaHores[11][1]


def pintarLiniesVerticals(draw, llistaTuplaDies, llistaTuplaHores):
	for elem in llistaTuplaDies:
		llarg = elem[0]-13
		alt = llistaTuplaHores[0][1]
		alt2 = llistaTuplaHores[11][1]+20
		draw.line((llarg,alt, llarg, alt2), fill = constants.NEGRE)
	return draw

def pintarLiniesHoritzontals(draw, llistaTuplaDies, llistaTuplaHores):
	for elem in llistaTuplaHores:
		alt = elem[1]+20
		llarg = llistaTuplaHores[0][1]-70
		llarg2 = llistaTuplaDies[4][0]+100
		draw.line((llarg,alt, llarg2, alt), fill = constants.NEGRE)
	return draw

def transformarFormat(assig):
	llistaAula = assig.split()
	aux = llistaAula[0:2]
	mostra =  " ".join(map(str,aux)) 
	mostra = mostra + str(llistaAula[4])
	return mostra

def sonIguals(assig, assigAnterior):
	aSplit = assig.split()
	anatSplit = assigAnterior.split()
	strAssig = str(aSplit[0]) + str(aSplit[1]) + str(aSplit[2]) + str(aSplit[4])
	strAssigAnterior =str(anatSplit[0]) + str(anatSplit[1]) + str(anatSplit[2]) + str(anatSplit[4])
	if (strAssig == strAssigAnterior):
		if (str(aSplit[3]) == str(anatSplit[3])):
			return False
		else:
			return True
	return False

def pintarAssignatures(draw, fontLletra, llistaTuplaHores, llistaTuplaDies, elem):
	fileAula=parsejar_info.ordenarEliminarDuplicatLinies(elem)
	fontLletra2 = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRA)
	assigAnterior = fileAula.readline()
	mostra = transformarFormat(assigAnterior)
	llarg = obtenirLlarg(llistaTuplaDies, assigAnterior.split())
	alt = obtenirAlt(llistaTuplaHores,  assigAnterior.split())
	draw.text((llarg-10, alt+13), mostra, font= fontLletra2, fill=constants.NEGRE)
	for assig in fileAula:
		llistaAula = assig.split()
		llistaAulaAnt = assigAnterior.split()
		alt = obtenirAlt(llistaTuplaHores, llistaAula)
		llarg = obtenirLlarg(llistaTuplaDies, llistaAula)
		if (sonIguals(assig, assigAnterior)== True):
			maxLlista = llistaAulaAnt
			mostra = transformarFormat(assigAnterior)
			llargLine = obtenirLlarg(llistaTuplaDies, maxLlista)
			altLine = obtenirAlt(llistaTuplaHores, maxLlista)
			alt = obtenirAlt(llistaTuplaHores, maxLlista)
			llarg = obtenirLlarg(llistaTuplaDies, maxLlista)
			draw.line((llargLine-12, altLine+20, llargLine+97, altLine+20), fill=constants.BLANC)
			draw.text((llarg-10, alt), mostra, font= fontLletra2, fill=constants.BLANC)
			draw.text((llarg-10, alt), mostra, font= fontLletra2, fill=constants.BLANC)
			draw.text((llargLine-10,  altLine+13), mostra, font= fontLletra2, fill=constants.NEGRE)
		else:
			mostra = transformarFormat(assig)
			draw.text((llarg-10, alt), mostra, font= fontLletra2, fill=constants.NEGRE)
		assigAnterior = assig
	return draw

def estructuraHorari(image, elem):
	draw = ImageDraw.Draw(image)
	fontLletraHoresDies = ImageFont.truetype(constants.PATH_LLETRA_HORES_DIES, constants.MIDA_LLETRES)
	fontTitol = ImageFont.truetype(constants.PATH_TITOL, constants.MIDA_TITOL)
	fontLletra = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRES)
	draw.text((constants.CENTRAR_X, constants.CENTRAR_Y), 'HORARI AULA ' + elem, font =fontTitol, fill = constants.NEGRE)
	draw = pintarDiesSetmana(draw, fontLletraHoresDies)
	draw = pintarHores(draw, fontLletraHoresDies)
	llistaTuplaHores = crearLlistaTuplaHores()
	llistaTuplaDies = crearLlistaTuplaDies()
	draw = pintarLiniesVerticals(draw, llistaTuplaDies, llistaTuplaHores)
	draw = pintarLiniesHoritzontals(draw, llistaTuplaDies, llistaTuplaHores)
	draw = pintarAssignatures(draw, fontLletra, llistaTuplaHores, llistaTuplaDies, elem)
	return image




