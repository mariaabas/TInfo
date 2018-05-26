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

def crear_llista_tupla_dies():
	llarg = constants.LLARGADA
	alt = constants.ALTURA+50
	llista_pos_dies=[]
	for dia in constants.LIST_DIES:
		llista_pos_dies.appned(crear_llista_tupla(alt, llarg))
		llarg=llarg+100
	return llista_pos_dies

def crear_llista_tupla_hores():
	alt=constants.ALTURA+50
	llista_pos_hores=[]
	for hora in constants.LIST_HORES:
		alt = alt+25
		llista_pos_hores.appned(crear_llista_tupla(10, alt))
	return llisata_pos_hores

def pintar_dies_setmana(draw, font_lletra):
	llarg = constants.LLARGADA
	alt = constants.ALTURA+50
	for dia in constants.LIST_DIES:
		draw.text((llarg, alt), dia, font= font_lletra, fill=constants.NEGRE)
		llarg=llarg+100
	return draw

def pintar_hores(draw, font_lletra):
	alt=constants.ALTURA+50
	for hora in constants.LIST_HORES:
		alt = alt+25
		draw.text((10, alt), hora, font= font_lletra, fill=constants.NEGRE)
	return draw

def pintar_assignatures(draw, font_lletra, llista_tupla_hores, llista_tupla_dies):
	file_aula=open("/home/pi/Documents/treball_fi_grau/TInfo/aules/A6206.txt", "r")
	font_lletra2 = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRA)
	alt = constants.ALTURA+50
	for assig in file_aula:
		llista_aula = assig.split()
		aux = llista_aula[0:1]
		mostra =  " ".join(map(str,aux))
		alt=alt+25
		draw.text((constants.LLARGADA, alt), mostra, font= font_lletra2, fill=constants.NEGRE)
	return draw

def estructura_horari(image):
	draw = ImageDraw.Draw(image)
	font_lletra = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRES)
	font_titol = ImageFont.truetype(constants.PATH_TITOL, constants.MIDA_TITOL)
	draw.text((constants.CENTRAR_TITOL, 4), 'HORARI AULA A6206', font =font_titol, fill = constants.NEGRE)
	draw = pintar_dies_setmana(draw, font_lletra)
	draw = pintar_hores(draw, font_lletra)
	llista_tupla_hores = crear_llista_tupla_hores()
	llista_tupla_dies = crear_llista_tupla_dies()
	draw = pintar_assignatures(draw, font_lletra, llista_tupla_hores, llista_tupla_dies)
	return image




