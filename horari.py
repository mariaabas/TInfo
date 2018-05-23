import epd7in5b
import Image
import ImageDraw
import ImageFont
import constants

def estructura_horari(epd):
	image = Image.new('L', (constants.EPD_WIDTH, constants.EPD_HEIGHT), 255)    # 255: clear the frame
	draw = ImageDraw.Draw(image)
	font_lletra = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRES)
	font_titol = ImageFont.truetype(constants.PATH_TITOL, constants.MIDA_TITOL)
	draw.text((constants.CENTRAR_TITOL, 4), 'HORARI AULA A6206', font =font_titol, fill = constants.NEGRE)
	llarg = constants.LLARGADA
	alt = constants.ALTURA+50
	for dia in constants.LIST_DIES:
		draw.text((llarg, alt), dia, font= font_lletra, fill=constants.NEGRE)
		llarg=llarg+100
	for hora in constants.LIST_HORES:
		alt = alt+25
		draw.text((10, alt), hora, font= font_lletra, fill=constants.NEGRE)
	file_aula=open("aules/A6206.txt", "r")
	font_lletra2 = ImageFont.truetype(constants.PATH_LLETRA, constants.MIDA_LLETRA)
	alt = constants.ALTURA+50
	for assig in file_aula:
		llista_aula = assig.split()
		aux = llista_aula[0:1]
		mostra =  " ".join(map(str,aux))
		alt=alt+25
		draw.text((constants.LLARGADA, alt), mostra, font= font_lletra2, fill=constants.NEGRE)

	epd.display_frame(epd.get_frame_buffer(image))



