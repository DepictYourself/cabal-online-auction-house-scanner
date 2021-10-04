from helpers import *
import constants as c


def init():
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    initialize_cabal_window()


#Run the whole project with "python run.py"
def run():
    init()
    img = make_screenshot()
    item_name = parse_name(img)
    item_quantity = parse_qty(img)
    item_price = parse_price(img)
    print(item_name, item_quantity ,item_price)



if (__name__ == '__main__'):
    run()