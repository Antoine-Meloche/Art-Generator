import time
import webview
import defaultGen
import sys


class Api:
    def __init__(self):
        self._window = None

    def init(self):
        return "Pywebview Initialized."

    def close_window(self):
        window.destroy()
        quit()

    def toggle_fullscreen(self):
        window.toggle_fullscreen()

    def minimize(self):
        window.minimize()

    def generate(self, gen_type, width, height, fg, bkg, n, steps, substeps, length, angleincr, angle, exportPath):
        if gen_type == "default":
            defaultGen.generate(width, height, fg, bkg, n, steps, substeps, length, angleincr, angle, exportPath)
            window.evaluate_js(f"document.querySelector('.result img').src = ('{exportPath}')")
        elif gen_type == "":
            pass
        else:
            pass


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Art Generator | Made by Antoine Meloche',
                                   './index.html', frameless=True, easy_drag=False, js_api=api, resizable=True, min_size=(1200,800))
    webview.start(debug=True)
