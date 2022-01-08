import sys
import webview
import time
import defaultGen
import perlinCircleGen

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

    def default_gen(self, width, height, fg, bkg, n, steps, substeps, length, angleincr, angle, export_path):
        width = int(width)
        height = int(height)
        fg = str(fg)
        bkg = str(bkg)
        n = int(n)
        steps = int(steps)
        substeps = int(substeps)
        length = int(length)
        angleincr = int(angleincr)
        angle = int(angle)
        export_path = str(export_path)
        defaultGen.generate(width, height, fg, bkg, n, steps,
                            substeps, length, angleincr, angle, export_path)
        self.set_image(export_path)

    def circle_gen(self, width, height, fg, bkg, export_path):
        width = int(width)
        height = int(height)
        fg = str(fg)
        bkg = str(bkg)
        export_path = str(export_path)
        perlinCircleGen.generate(width, height, fg, bkg, export_path)
        self.set_image(export_path)

    def set_image(self, export_path):
        window.evaluate_js(f"document.querySelector('.result img').src = ''")
        window.evaluate_js(
            f"document.querySelector('.result img').src = '{export_path + '?' + str(time.time())}'")
        window.evaluate_js("progress.hidden=true")


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Art Generator | Made by Antoine Meloche',
                                   './index.html', frameless=False, easy_drag=False, js_api=api, resizable=True, min_size=(1200, 800))
    webview.start(gui=platform_gui, debug=True)
