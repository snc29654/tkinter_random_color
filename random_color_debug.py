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
        self.root.geometry("800x700")
        time.sleep(10)
        print("start")

    def color_set(self,color):
        for y in range(100):            #self.canvas.delete("view")
            for x in range(80):            #self.canvas.delete("view")
                
                dx = 5
                dy = 5
                #time.sleep(0.01)
                self.canvas.create_rectangle(x*5, y*5, x*5+dx, y*5+dy,
                fill = color,tag="view")

    def canvas_start(self):


        #キャンバスエリア
        self.canvas = tkinter.Canvas(self.root,
        width = 800, height = 700)
        #キャンバスバインド
        self.canvas.place(x=0, y=0)


        thread1 = threading.Thread(
            target=self.color_set,args=("green",))
        thread1.start()
        thread2 = threading.Thread(
            target=self.color_set,args=("red",))
        thread2.start()
        thread3 = threading.Thread(
            target=self.color_set,args=("blue",))
        thread3.start()
        thread4 = threading.Thread(
            target=self.color_set,args=("yellow",))
        thread4.start()
        thread5 = threading.Thread(
            target=self.color_set,args=("white",))
        thread5.start()
        thread6 = threading.Thread(
            target=self.color_set,args=("black",))
        thread6.start()
        thread7 = threading.Thread(
            target=self.color_set,args=("cyan",))
        thread7.start()
        thread8 = threading.Thread(
            target=self.color_set,args=("magenta",))
        thread8.start()


        self.root.mainloop()


c1 = canvas_class()
c1.canvas_start()