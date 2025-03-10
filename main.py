import os
import logging
from lib import epd7in3f
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Running Main")
    epd = epd7in3f.EPD()   

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    # Get the directory of the current script (`main.py`)
    root_dir = os.path.dirname(os.path.realpath(__file__))

    logging.info("load font")
    font = ImageFont.truetype(os.path.join(root_dir, 'resources', 'Font.ttc'), 18)

    logging.info("load image")
    Himage = Image.open(os.path.join(root_dir, 'resources', '7in3f1.bmp'))

    draw = ImageDraw.Draw(Himage)
    draw.text((5, 0), 'Testing', font = font, fill = epd.RED)

    # draw.line((80, 170, 5, 245), fill = epd.ORANGE)
    # draw.rectangle((5, 170, 80, 245), outline = epd.BLACK)
    # draw.arc((5, 250, 80, 325), 0, 360, fill = epd.RED)
    # draw.chord((90, 250, 165, 325), 0, 360, fill = epd.YELLOW)

    epd.display(epd.getbuffer(Himage))
    time.sleep(3)
    
    # logging.info("Clear...")
    # epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3f.epdconfig.module_exit(cleanup=True)
    exit()
