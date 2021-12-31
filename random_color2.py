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
            x = random.randint(1,400)
            y = random.randint(1,400)
            dx = random.randint(1,400)
            dy = random.randint(1,400)
            time.sleep(0.01)
            self.canvas.create_rectangle(x, y, x+dx, y+dy, fill = color)
    def canvas_start(self):
        #キャンバスエリア
        self.canvas = tkinter.Canvas(self.root, width = 800, height = 550)
        #キャンバスバインド
        self.canvas.place(x=0, y=0)
        thread1 = threading.Thread(target=self.color_set,args=("green",))
        thread1.start()
        thread2 = threading.Thread(target=self.color_set,args=("red",))
        thread2.start()
        thread3 = threading.Thread(target=self.color_set,args=("blue",))
        thread3.start()
        thread4 = threading.Thread(target=self.color_set,args=("yellow",))
        thread4.start()
        self.root.mainloop()
c1 = canvas_class()
c1.canvas_start()