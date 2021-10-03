import cv2
import pytesseract
import numpy
import pyautogui
import win32gui
import win32con



def make_screenshot():
    img = pyautogui.screenshot(region=(0, 0, 826, 756))
    converted_img = convert_to_cv2_img(img)
    return converted_img


def convert_to_cv2_img(img):
    open_cv_img = numpy.array(img)
    open_cv_img = cv2.cvtColor(open_cv_img, cv2.COLOR_RGB2BGR)
    return open_cv_img



def parse_item_name(img):
    #                 x1  y1
    # balfelso_pont= (175,195)
    #                 x2  y2
    # jobbalso_pont= (425,235)
    # numpy slicing: img[y1:y2, x1:x2]
    img_crop_item = img[195:235, 175:425].copy()
    # resize to double for more readability
    img_crop_item = cv2.resize(img_crop_item, (0, 0), fx=2, fy=2)
    # conver to greyscale
    img_crop_item = cv2.cvtColor(img_crop_item, cv2.COLOR_BGR2GRAY)
    # apply simple treshold for easier recognition with pytesseract
    thr_item = cv2.threshold(img_crop_item, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    item_name = pytesseract.image_to_string(thr_item, config="-c page_separator='' ")
    return item_name



def parse_item_quantity(img):
    img_crop_quantity = img[195:235, 430:465].copy()
    img_crop_quantity = cv2.resize(img_crop_quantity, (0, 0), fx=2, fy=2)
    img_crop_quantity = cv2.cvtColor(img_crop_quantity, cv2.COLOR_BGR2GRAY)
    thr_quantity = cv2.threshold(img_crop_quantity, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    item_quantity = pytesseract.image_to_string(thr_quantity, config="-c page_separator=''")
    return item_quantity

def parse_item_price(img):
    img_crop_price = img[195:235, 475:585].copy()
    img_crop_price = cv2.resize(img_crop_price, (0, 0), fx=2, fy=2)
    item_price = pytesseract.image_to_string(img_crop_price, config="-c page_separator='' ")
    return item_price



def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))



def move_window(hwnd, x, y, n_width, n_height, b_repaint):
    win32gui.MoveWindow(hwnd, x - 7, y, n_width, n_height, b_repaint)



def initialize_cabal_window():
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "cabal" in i[1].lower():
            win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
            win32gui.SetForegroundWindow(i[0])
            rect = win32gui.GetWindowRect(i[0])
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            move_window(i[0], 0, 0, 1024, 768, True)
            break