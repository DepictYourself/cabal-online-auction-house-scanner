import cv2
import pytesseract
import numpy
import pyautogui
import win32gui
import win32con

import constants as c



def make_screenshot():
    img = pyautogui.screenshot(region=(0, 0, 826, 756))
    converted_img = convert_to_cv2_img(img)
    return converted_img



def convert_to_cv2_img(img):
    open_cv_img = numpy.array(img)
    open_cv_img = cv2.cvtColor(open_cv_img, cv2.COLOR_RGB2BGR)
    return open_cv_img



def parse_name(img, n = 0):
    cropped_img = crop_image(img, c.AREA_NAME["x1"], c.AREA_NAME["y1"], c.AREA_NAME["x2"], c.AREA_NAME["y2"])
    return parse_crop(cropped_img)



def parse_qty(img):
    cropped_img = crop_image(img, c.AREA_QTY["x1"], c.AREA_QTY["y1"], c.AREA_QTY["x2"], c.AREA_QTY["y2"])
    return parse_crop(cropped_img)



def parse_price(img):
    cropped_img = crop_image(img, c.AREA_PRICE["x1"], c.AREA_PRICE["y1"], c.AREA_PRICE["x2"], c.AREA_PRICE["y2"])
    return parse_crop(cropped_img)



def crop_image(img, x1, y1, x2, y2):
    return img[y1:y2, x1:x2].copy()



def parse_crop(img_crop):
    # resize to double for more readability
    img_crop = cv2.resize(img_crop, (0, 0), fx=2, fy=2)
    # conver to greyscale
    img_crop = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
    # apply simple treshold for easier recognition with pytesseract
    thr = cv2.threshold(img_crop, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    item = pytesseract.image_to_string(thr, config="-c page_separator=''")
    return item



def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))



def move_window(hwnd, x, y, n_width, n_height, b_repaint):
    win32gui.MoveWindow(hwnd, x - 7, y, n_width, n_height, b_repaint)



def initialize_cabal_window():
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "CABAL" in i[1]:
            win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
            win32gui.SetForegroundWindow(i[0])
            rect = win32gui.GetWindowRect(i[0])
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            move_window(i[0], 0, 0, 1024, 768, True)
            break