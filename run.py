from helpers import *
import constants as c


def init():
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    initialize_cabal_window()


#Run the whole project with "python run.py"
def run():
    init()
    img = make_screenshot()
    for i in range(7):
        item_name, item_quantity, item_price = parse_row(img, i)
        print(item_name, item_quantity ,item_price)
    cv2.waitKey(0)



if (__name__ == '__main__'):
    run()