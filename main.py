#! /usr/bin/env python3
# -*- coding: utf-8 -*-
 
import kivy
# kivy.require('1.10.1') 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

try:
    with open("eleves.csv","r") as f:
        eleves = f.readlines()

except:
    pass

def create_dic():
    d_eleves = []
    try:
        with open("eleves.csv","r") as f:
            for line in f.readlines():
                eleve = line.split(',')
                d_eleve = {}
                d_eleve['nom'] = eleve[0]
                d_eleve['prenom'] = eleve[1]
                d_eleve['code'] = eleve[2]
                d_eleves.append(d_eleve)
    except:
        pass
    return d_eleves


class EnClasseApp(App):
    def build(self):
        self.mylayout = BoxLayout(orientation="vertical")
        self.mylabel = Label(text= "My App")
        self.K_label = Label(text= "")
        self.mytextinput = TextInput(multiline=False)
        self.mytextinput.bind(text=self.on_text)
        self.mytextinput.focus = True
        self.mylayout.add_widget(self.K_label)
        self.mylayout.add_widget(self.mylabel)
        self.mylayout.add_widget(self.mytextinput)
        self.eleves = create_dic()
        Window.bind(on_key_down=self._keydown)
        return self.mylayout

    def _keydown(self,*args):
        try:
            self.K_label.text = args[3]
        except Exception as e:
            self.K_label.text = e

    def on_text(self, instance, value):
        check = False
        for eleve in self.eleves:
            if value == eleve['code']:
                self.mylabel.text = "{} {}".format(eleve['nom'], eleve['prenom'])
                check = True
                print(eleve)
            else:
                pass
        if not check:
            self.mylabel.text = "Code inconnu"
        self.mytextinput.text = ""
        self.mytextinput.focus = True
 

if __name__ == '__main__':
    EnClasseApp().run()