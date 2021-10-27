import sys
import webview
import defaultGen
import pipesGen

if sys.platform == "linux":
    platform_gui = 'gtk'
elif sys.platform == "win32":
    platform_gui = 'mshtml'
elif sys.platform == "darwin":
    platform_gui = ''


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

    def generate(self, gen_type="default", width=2100, height=1300, fg="#ffffff", bkg="#242424", n=50, steps=30, substeps=10, length=100, angleincr=10, angle=0, exportPath="./image.png"):
        if gen_type == "default":
            defaultGen.generate(width, height, fg, bkg, n, steps,
                                substeps, length, angleincr, angle, exportPath)
            window.evaluate_js(
                f"document.querySelector('.result img').src = ('{exportPath}')")
        elif gen_type == "pipes":
            pipesGen.generate(width, height, n, prob, fg, bkg)
            window.evaluate_js(
                f"document.querySelector('.result img').src = ('{exportPath}')")
        else:
            pass


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Art Generator | Made by Antoine Meloche',
                                   './index.html', frameless=True, easy_drag=False, js_api=api, resizable=True, min_size=(1200, 800))
    webview.start(gui=platform_gui, debug=True)
