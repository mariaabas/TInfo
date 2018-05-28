import Image
import horari as horari
import constants

def pintar_logo_fib():
	image = Image.open('fib2.bmp')
	return image

def pintar_punta_fangar():
	image = Image.open('punta_fangar_delta.bmp')
	return image

def pintar_horari_aules(elem):
	 image = Image.new('L', (constants.EPD_WIDTH, constants.EPD_HEIGHT), 255) 
	 image = horari.estructura_horari(image, elem)
	 return image