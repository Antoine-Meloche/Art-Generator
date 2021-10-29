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

    def generate(self, gen_type: str, options: list):
        if gen_type == "default":
            defaultGen.generate(options[0], options[1], options[2], options[3], options[4], options[5],
                                options[6], options[7], options[8], options[9], options[10])
            window.evaluate_js(
                f"document.querySelector('.result img').src = ('{options[10]}')")
        elif gen_type == "pipes":
            pipesGen.generate(
                options[0], options[1], options[2], options[3], options[4], options[5])
            window.evaluate_js(
                f"document.querySelector('.result img').src = ('{exportPath}')")
        else:
            pass


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Art Generator | Made by Antoine Meloche',
                                   './index.html', frameless=True, easy_drag=False, js_api=api, resizable=True, min_size=(1200, 800))
    webview.start(gui=platform_gui, debug=True)
