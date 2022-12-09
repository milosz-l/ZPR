import pygame
import tkinter as tk
from tkinter import *
from board_display import BoardWindow
import random
import utils

WIDTH=100
HEIGHT=100
RANGE=2


class UserOptions:
    def __init__(self, width=100, height=100):
        self.root = tk.Tk()
        self.start_frame = tk.Frame(self.root, width = width, height = height)
        self.start_frame.pack()
        start_btn = Button(self.start_frame,text = 'Start',  command=self.start)
        start_btn.pack()
        option_btn = Button(self.start_frame,text = 'Custom options',  command=self.options)
        option_btn.pack()
        file_btn = Button(self.start_frame,text = 'Custom file',  command=self.file_options)
        file_btn.pack()
        self.root.update()

    def options(self):
        self.start_frame.pack_forget()
        self.options_frame = tk.Frame(self.root, width = WIDTH, height = HEIGHT)
        self.middle_opt = IntVar()
        self.neighb_type = StringVar()
        self.neighb_type.set(None)
        label_entry=Label(self.options_frame, text="Range", font=("Courier 12"))
        label_entry.pack()
        self.entry_range=Entry(self.options_frame, text="", bd=5)
        self.entry_range.pack()
        label_states=Label(self.options_frame, text="States", font=("Courier 12"))
        label_states.pack()
        self.entry_states=Entry(self.options_frame, text="", bd=5)
        self.entry_states.pack()
        choice_middle=Radiobutton(self.options_frame, text="Middle", variable=self.middle_opt,value=1)
        choice_middle.pack()
        label_neighb=Label(self.options_frame, text="Neighbourhood type", font=("Courier 12"))
        label_neighb.pack()
        choice_neighb_NM=Radiobutton(self.options_frame, text="Moore", variable=self.neighb_type,value="NM")
        choice_neighb_NM.pack()
        choice_neighb_NN=Radiobutton(self.options_frame, text="von Neumann", variable=self.neighb_type,value="NN")
        choice_neighb_NN.pack()
        self.stop_btn = Button(self.options_frame,text = 'Done',  command=self.save_options)
        self.stop_btn.pack(side=LEFT)
        self.options_frame.pack()

    def save_options(self):
        utils.OPTIONS.range=self.entry_range.get()
        utils.OPTIONS.states = self.entry_states.get()
        utils.OPTIONS.mid = self.middle_opt.get()
        utils.OPTIONS.neighb = self.neighb_type.get()
        self.options_frame.pack_forget()
        self.start_frame.pack()

    def file_options(self):
        self.file_frame = tk.Frame(self.root, width = WIDTH, height = HEIGHT)
        filepath_entry=Label(self.file_frame, text="File path", font=("Courier 12"))
        filepath_entry.pack()
        self.entry_filepath=Entry(self.file_frame, text="", bd=5)
        self.entry_filepath.pack()
        self.path_btn = Button(self.file_frame,text = 'Done',  command=self.save_file_options)
        self.path_btn.pack(side=LEFT)
        self.start_frame.pack_forget()
        self.file_frame.pack()

    def save_file_options(self):
        path=self.entry_filepath.get()
        utils.OPTIONS=utils.load_params(path)
        self.file_frame.pack_forget()
        self.start_frame.pack()


    def start(self):
        STATES = 12
        height = 45
        width = 60
        self.board = BoardWindow(height, width, STATES)
        self.root.update()
        self.run()

    def run(self):
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
