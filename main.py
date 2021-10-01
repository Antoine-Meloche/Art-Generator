import time
import webview
import defaultGen
import sys

class Api:
    def __init__(self):
        self._window = None

    def close_window(self):
        window.destroy()
        quit()

    def toggle_fullscreen(self):
        window.toggle_fullscreen()

    def minimize(self):
        window.minimize()

    def generate(self, type, width, height, bkg, exportPath):
        if type == "default":
            defaultGen.generate(width, height, bkg, exportPath)
        elif type == "":
            pass
        else:
            pass

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Art Generator | Made by Antoine Meloche', url='./index.html', frameless=True, easy_drag=False, js_api=api, resizable=False)
    webview.start()