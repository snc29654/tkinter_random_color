#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import threading
import time
import random
class canvas_class():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(u"Canvas test")
        self.root.geometry("800x600")
    def color_set(self,color):
        while(1):
            for x in range(10):
                for y in range(100):
                    time.sleep(0.01)
                    self.canvas.delete("view")
                    self.canvas.create_rectangle(x*30, y*5, x*30+30, 
                    y*5+30, fill = color,tag="view")
    def canvas_start(self):
        #キャンバスエリア
        self.canvas = tkinter.Canvas(self.root, width = 800, height = 550)
        #キャンバスバインド
        self.canvas.place(x=0, y=0)
        thread2 = threading.Thread(target=self.color_set,args=("red",))
        thread2.start()
        self.root.mainloop()
c1 = canvas_class()
c1.canvas_start()