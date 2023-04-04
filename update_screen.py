from PIL import ImageGrab, ImageDraw
import scree_lib.eink as eink

im = ImageGrab.grab(bbox=(0,0,800,480))

epd = eink.EPD()

epd.init()
epd.Clear()
epd.display(epd.getbuffer(im))
epd.sleep()