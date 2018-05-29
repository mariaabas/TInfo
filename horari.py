import epd7in5b
import Image
import ImageDraw
import ImageFont
import constants

def crear_llista_tupla(alt, llarg):
	llista = []
	llista.append(alt)
	llista.append(llarg)
	tupla = tuple(llista)
	return tupla

def crear_llista_tupla_dies(draw, font_lletra):
	llarg = constants.LLARGADA
	alt = constants.ALTURA+50
	llista_pos_dies=[]
	for dia in constants.LIST_DIES:
		llista_pos_dies.append(crear_llista_tupla(alt, llarg))
		llarg=llarg+110
	return llista_pos_dies

def crear_llista_tupla_hores():
	alt=constants.ALTURA+50
	llista_pos_hores=[]
	for hora in constants.LIST_HORES:
		alt = alt+25
		llista_pos_hores.append(crear_llista_tupla(10, alt))
	return llista_pos_hores

def pintar_dies_setmana(draw, font_lletra):
	llarg = constants.LLARGADA
	alt = constants.ALTURA+50
	for dia in constants.LIST_DIES:
		draw.text((llarg, alt), dia, font= font_lletra, fill=constants.NEGRE)
		llarg=llarg+110
	return draw

def pintar_hores(draw, font_lletra):
	alt=constants.ALTURA+50
	for hora in constants.LIST_HORES:
		alt = alt+25
		draw.text((10, alt), hora, font= font_lletra, fill=constants.NEGRE)
	return draw

def obtenir_llarg(llista_tupla_dies, llista_aula):
	return llista_tupla_dies[int(llista_aula[2])-1][1]

def obtenir_alt(llista_tupla_hores, llista_aula):
	hora = llista_aula[3]
	if (hora == '08:00'):
		return llista_tupla_hores[0][1]
	if (hora == '09:00'):
		return llista_tupla_hores[1][1]
	if (hora == '10:00'):
		return llista_tupla_hores[2][1]
	if (hora == '11:00'):
		return llista_tupla_hores[3][1]
	if (hora == '12:00'):
		return llista_tupla_hores[4][1]
	if (hora == '13:00'):
		return llista_tupla_hores[5][1]
	if (hora == '14:00'):
		return llista_tupla_hores[6][1]
	if (hora == '15:00'):
		return llista_tupla_hores[7][1]
	if (hora == '16:00'):
		return llista_tupla_hores[8][1]
	if (hora == '17:00'):
		return llista_tupla_hores[9][1]
	if (hora == '18:00'):
		return llista_tupla_hores[10][1]
	if (hora == '19:00'):
		return llista_tupla_hores[11][1]

def pintar_assignatures(draw, font_lletra, llista_tupla_hores, llista_tupla_dies, elem):
	file_aula=open("/home/pi/Documents/treball_fi_grau/TInfo/aules/" + elem + ".txt", "r")
	font_lletra2 = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRA)
	for assig in file_aula:
		llista_aula = assig.split()
		aux = llista_aula[0:2]
		mostra =  " ".join(map(str,aux)) 
		mostra = mostra + str(llista_aula[4])
		alt = obtenir_alt(llista_tupla_hores, llista_aula)
		llarg = obtenir_llarg(llista_tupla_dies, llista_aula)
		draw.text((llarg-10, alt), mostra, font= font_lletra2, fill=constants.NEGRE)
	return draw
def pintar_linies_verticals(draw, llista_tupla_dies, llista_tupla_hores):
	for elem in llista_tupla_dies:
		llarg = elem[1]-13
		alt = llista_tupla_hores[0][1]
		alt2 = llista_tupla_hores[11][1]+20
		draw.line((llarg,alt, llarg, alt2), fill = constants.NEGRE)
	return draw
def pintar_linies_horitzontals(draw, llista_tupla_dies, llista_tupla_hores):
	for elem in llista_tupla_hores:
		alt = elem[1]+20
		llarg = llista_tupla_dies[4][1]+100
		llarg2 = llista_tupla_hores[0][1]-70
		draw.line((llarg,alt, llarg2, alt), fill = constants.NEGRE)
	return draw

def estructura_horari(image, elem):
	draw = ImageDraw.Draw(image)
	font_lletra_hores_dies = ImageFont.truetype(constants.PATH_LLETRA_HORES_DIES, constants.MIDA_LLETRES)
	font_titol = ImageFont.truetype(constants.PATH_TITOL, constants.MIDA_TITOL)
	font_lletra = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRES)
	draw.text((constants.CENTRAR_TITOL, 4), 'HORARI AULA ' + elem, font =font_titol, fill = constants.NEGRE)
	draw = pintar_dies_setmana(draw, font_lletra_hores_dies)
	draw = pintar_hores(draw, font_lletra_hores_dies)
	llista_tupla_hores = crear_llista_tupla_hores()
	llista_tupla_dies = crear_llista_tupla_dies(draw, font_lletra_hores_dies)
	draw = pintar_assignatures(draw, font_lletra, llista_tupla_hores, llista_tupla_dies, elem)
	draw = pintar_linies_verticals(draw, llista_tupla_dies, llista_tupla_hores)
	draw = pintar_linies_horitzontals(draw, llista_tupla_dies, llista_tupla_hores)
	return image




