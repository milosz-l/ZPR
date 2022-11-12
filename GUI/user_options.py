import pygame
import tkinter as tk
from tkinter import *
from board_display import BoardWindow
import random

RANGE=2

class UserOptions:
    def __init__(self, width=100, height=100):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width = width, height = height)
        self.frame.pack(side = LEFT)
        start_button = Button(self.frame,text = 'Start',  command=self.start)
        start_button.pack(side=LEFT)
        stop_button = Button(self.frame,text = 'Stop',  command=self.stop)
        stop_button.pack(side=LEFT)
        option_button = Button(self.frame,text = 'Custom options',  command=self.options)
        option_button.pack(side=LEFT)
        self.root.update()

    def start(self):
        STATES = 12
        height = 45
        width = 60
        self.board = BoardWindow(height, width, STATES)
        self.root.update()
        self.run()

    def options(self):
        self.window_options = Toplevel(self.root)
        # self.frame_options = tk.Frame(self.window_options, width = 100, height = 200)
        # self.frame.pack(side = LEFT)
        self.middle_opt = IntVar()
        self.neighb_type = StringVar()
        self.neighb_type.set(None)
        label_entry=Label(self.window_options, text="Range", font=("Courier 12"))
        label_entry.pack()
        self.entry_range=Entry(self.window_options, text="", bd=5)
        self.entry_range.pack()
        label_states=Label(self.window_options, text="States", font=("Courier 12"))
        label_states.pack()
        self.entry_states=Entry(self.window_options, text="", bd=5)
        self.entry_states.pack()
        choice_middle=Radiobutton(self.window_options, text="Middle", variable=self.middle_opt,value=1)
        choice_middle.pack()
        label_neighb=Label(self.window_options, text="Neighbourhood type", font=("Courier 12"))
        label_neighb.pack()
        choice_neighb_NM=Radiobutton(self.window_options, text="Moore", variable=self.neighb_type,value="NM")
        choice_neighb_NM.pack()
        choice_neighb_NN=Radiobutton(self.window_options, text="von Neumann", variable=self.neighb_type,value="NN")
        choice_neighb_NN.pack()
        self.stop_button = Button(self.window_options,text = 'Done',  command=self.save_options)
        self.stop_button.pack(side=LEFT)
        self.window_options.mainloop()
    
    def save_options(self):
        self.range= self.entry_range.get()
        RANGE=self.range
        self.states = self.entry_states.get()
        self.middle = self.middle_opt.get()
        self.neighb = self.neighb_type.get()
        self.window_options.destroy()


    def run(self):
        print(self.range)
        print(self.states)
        STATES = 12
        height = 45
        width = 60
        while True:
            new_version=new_board(STATES, height, width)
            self.board.update(new_version)
            pygame.display.flip()
            self.root.update()

    def stop(self):
        pygame.quit()


def new_board(states, height, width):
    board = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            board[y][x]=random.randint(0, states-1)
    return board

game = UserOptions()
while True:
    game.root.update()

# https://stackoverflow.com/questions/23319059/embedding-a-pygame-window-into-a-tkinter-or-wxpython-frame
