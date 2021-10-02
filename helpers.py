import win32gui
import win32con



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