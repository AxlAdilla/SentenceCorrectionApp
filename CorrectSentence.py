#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:51:14 2019

@author: axl
"""
import minimumEditDistance as MED
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class customBox(BoxLayout):
    def do_MED(self,sentence):
        print("raw Sentence from doMed : {}\n ".format(sentence))
        self.hasil.corrSentence.text = MED.sentencesCorrection(str(sentence))

class CorrectSentenceApp(App):
            
    def build(self):
        return customBox()

if __name__ == "__main__":
    CorrectSentenceApp().run()