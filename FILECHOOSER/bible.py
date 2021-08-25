
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('bible.kv')

class MyLayout(Widget):
        def selected(self,filename):
            try:
                self.ids.my_image.source = filename[0]
                with open("abcd.txt", "r") as f:
                    return (f.read())

                self.ids.my_image.source = filename[0]
                with open("abcd.txt", "r") as f:
                    return (f.read())
            except:
                pass

        def load(self, path, filename):
            with open("abcd/abcd.txt", "wb", filename[0]) as stream:
                self.text_input.text = stream.read()

            self.dismiss_popup()

            def load(self, path, filename):
                with open(os.path.join(path, filename[0])) as stream:
                    self.text_input.text = stream.read()

                self.dismiss_popup()

            """with open("abcd/abcd.txt", "wb") as f:
                r = requests.get(user.avatar_url, stream=True)
                for block in r.iter_content(1024):
                    if not block:
                        break
                    f.write(block) """

class P2(FloatLayout):
    def btn(self):
        pass

    def showtext(self):
        with open("abcd.txt", "r") as f:
            return (f.read())


class AwesomeApp(App):
    def build(self):
        return MyLayout()



if __name__ == '__main__':
    AwesomeApp().run()


