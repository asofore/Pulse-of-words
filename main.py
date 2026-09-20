from kivy.app import App
from kivy.uix.label import Label
from arkivy import ArLabel,ArButton
from kivy.graphics import Rectangle
from quotes import quotes





class MainKv(App):
    def build(self):
        self.box = self.root.ids.box
        
        for i in quotes:
            j = ArButton(text=i)
            j.background_normal='box.png'
            j.background_down='box.png'
            j.size_hint_y = None
            j.font_name='arb.ttf'
            j.halign='right'
            

            j.bind(width=lambda instance, value: setattr(instance, 'text_size', (value-200, None)))

            j.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
            
            j.split_str = ''
            
            self.box.add_widget(j)

if __name__ == '__main__':
    MainKv().run()
