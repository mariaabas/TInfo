import repository as informacio
import parse as parsejar_info
import pantalla as PTE
import epd7in5b
import Image
import ImageDraw
import ImageFont
import horari as horari
import constants

#import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    #informacio.obtenir_informacio_assignatures()
    #parsejar_info.parse_per_aules()
    epd = epd7in5b.EPD()
    epd.init()
    #PTE.prova_horari(epd)
    horari.estructura_horari(epd)
    # For simplicity, the arguments are explicit numerical coordinates
    #image = Image.new('L', (EPD_WIDTH, EPD_HEIGHT), 255)    # 255: clear the frame
    #draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 40)
    #draw.rectangle((0, 6, 640, 40), fill = 127)
    #draw.text((250, 192), 'BON DIA FAMILIA', font = font, fill = 127)
    #draw.rectangle((200, 80, 600, 280), fill = 127)
    #draw.chord((240, 120, 580, 220), 0, 360, fill = 255)
    #draw.rectangle((20, 80, 160, 280), fill = 0)
    #draw.chord((40, 80, 180, 220), 0, 360, fill = 127)
    #epd.display_frame(epd.get_frame_buffer(image))

    #image = Image.open('640x384.bmp')
    #image = Image.open('foto.bmp')
    #epd.display_frame(epd.get_frame_buffer(image))

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)

if __name__ == '__main__':
    main()
