import epd7in5b
import Image
import ImageDraw
import ImageFont

EPD_WIDTH = 640
EPD_HEIGHT = 384

def pasejar_dies_setmana(indicador):
	if (indicador=="1"):
		return "Dilluns"
	elif (indicador=="2"):
		return "Dimarts"
	elif (indicador=="3"):
		return "Dimecres"
	elif (indicador=="4"):
		return "Dijous"
	else:
		return "Divendres" 


def prova_horari(epd):
	image = Image.new('L', (EPD_WIDTH, EPD_HEIGHT), 255)    # 255: clear the frame
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
	file_aula=open("aules/A6206.txt", "r")
	inici=4
	for assig in file_aula:
		llista_aula = assig.split()
		llista_aula[2] = pasejar_dies_setmana(llista_aula[2])
		cadena = " ".join(map(str,llista_aula))
		draw.text((10, inici), cadena, font = font, fill = 127)
		inici=inici + 20
	epd.display_frame(epd.get_frame_buffer(image))
		