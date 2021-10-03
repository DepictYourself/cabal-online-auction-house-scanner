from helpers import *
import constants as c


#Run the whole project with "python run.py"
def run():
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    initialize_cabal_window()
    img = make_screenshot()
    item_name = parse_item_name(img)
    item_quantity = parse_item_quantity(img)
    item_price = parse_item_price(img)
    print(item_name, item_quantity ,item_price)



if (__name__ == '__main__'):
    run()