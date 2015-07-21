#!/usr/local/bin/python
#
from Tkinter import *
import random
import time
import logging

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)

        logger.debug ( self.id )

        starts = [ -3,-2,-1,1,2,3 ]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        logger.debug( self.canvas_height )
        logger.debug( canvas.winfo_height )

        self.canvas_width = self.canvas.winfo_width()
        logger.debug( self.canvas_width )
        logger.debug( canvas.winfo_width )


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move( self.id, 200, 300 )
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        pass

    def turn_left( self, evt ):
        self.x = -2

    def turn_right( self, evt ):
        self.x = 2


logger = logging.getLogger('BallBounce')
hdlr = logging.FileHandler('BallBounce.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'blue')

while 1:
    ball.draw()
    paddle.draw()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
