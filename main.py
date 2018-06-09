import repository as informacio
import parse as parsejar_info
import pantalla as PTE
import epd7in5b
import Image
import ImageDraw
import ImageFont
import horari as horari
import constants
import time

#import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384

def demo(epd):
	for elem in constants.LIST_AULES_HORARI:
		image = PTE.pintar_horari_aules(elem)
		epd.display_frame(epd.get_frame_buffer(image))
		time.sleep(30)
	image = PTE.pintar_punta_fangar()
	epd.display_frame(epd.get_frame_buffer(image))
	time.sleep(30)
	image = PTE.pintar_logo_fib()
	epd.display_frame(epd.get_frame_buffer(image))

def proves(epd):
	image = PTE.pintar_horari_aules(constants.LIST_AULES_HORARI[0])
	epd.display_frame(epd.get_frame_buffer(image))

def main():
    epd = epd7in5b.EPD()
    epd.init()
    #demo(epd)
    proves(epd)


if __name__ == '__main__':
    main()
