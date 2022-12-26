import logging
import scree_lib.eink as eink

try:
    logging.info("manual clear")
    epd = eink.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    epd.sleep()
except:
    logging.warning('failed')