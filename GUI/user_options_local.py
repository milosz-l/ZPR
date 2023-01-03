import pygame
import tkinter as tk
from tkinter import messagebox
import random
from time import sleep
from board_display import BoardWindow
import utils as utils


WIDTH = 100
HEIGHT = 100
RANGE = 2

SLEEP=0.5


class UserOptions:
    """
    Class representing main window that enables user to choose and specify options for the game.
    """

    def __init__(self, game_engine, width: int = 100, height: int = 100):
        """
        Creates a window for choosing a way to specify game parameters or an option
        to run with default parameters.
        Possible choices:
            Start:  Starts a game if parameters are not provided, game runs with random parameters.
            Custom options: Redirects to a next window for typing custom parameters.
            Custome file:   Redirects to a next window for specifying a path to json file with parameters.
            Close:  Closes all windows.
        """
        self.root = tk.Tk()
        self.start_frame = tk.Frame(self.root, width=width, height=height)
        self.start_frame.pack()
        start_btn = tk.Button(self.start_frame, text="Start", command=self.start)
        start_btn.pack()
        option_btn = tk.Button(
            self.start_frame, text="Custom options", command=self.options
        )
        option_btn.pack()
        file_btn = tk.Button(
            self.start_frame, text="Custom file", command=self.file_options
        )
        file_btn.pack()
        sleep_btn = tk.Button(self.start_frame, text="Sleep", command=self.sleep_option)
        sleep_btn.pack()
        resleep_btn = tk.Button(self.start_frame, text="Reset sleep", command=self.resleep)
        resleep_btn.pack()
        stop_btn = tk.Button(self.start_frame, text="Close", command=self.stop)
        stop_btn.pack()
        self.game_engine = game_engine
        self.root.update()

    def options(self):
        """
        Window for manually specifying custom parameters.
        Parameters to fill are: range, states, middle, neighbourhood type.
        """
        self.start_frame.pack_forget()
        self.options_frame = tk.Frame(self.root, width=WIDTH, height=HEIGHT)
        self.middle_opt = tk.IntVar()
        self.neighb_type = tk.StringVar()
        self.neighb_type.set(None)
        label_entry = tk.Label(self.options_frame, text="Range", font=("Courier 12"))
        label_entry.pack()
        self.entry_range = tk.Entry(self.options_frame, text="", bd=5)
        self.entry_range.pack()
        label_states = tk.Label(self.options_frame, text="States", font=("Courier 12"))
        label_states.pack()
        self.entry_states = tk.Entry(self.options_frame, text="", bd=5)
        self.entry_states.pack()
        label_s_min = tk.Label(
            self.options_frame, text="Survive min", font=("Courier 12")
        )
        label_s_min.pack()
        self.entry_s_min = tk.Entry(self.options_frame, text="", bd=5)
        self.entry_s_min.pack()
        label_s_max = tk.Label(
            self.options_frame, text="Survive max", font=("Courier 12")
        )
        label_s_max.pack()
        self.entry_s_max = tk.Entry(self.options_frame, text="", bd=5)
        self.entry_s_max.pack()
        label_b_min = tk.Label(
            self.options_frame, text="Birth min", font=("Courier 12")
        )
        label_b_min.pack()
        self.entry_b_min = tk.Entry(self.options_frame, text="", bd=5)
        self.entry_b_min.pack()
        label_b_max = tk.Label(
            self.options_frame, text="Birth max", font=("Courier 12")
        )
        label_b_max.pack()
        self.entry_b_max = tk.Entry(self.options_frame, text="", bd=5)
        self.entry_b_max.pack()
        choice_middle = tk.Radiobutton(
            self.options_frame, text="Middle", variable=self.middle_opt, value=1
        )
        choice_middle.pack()
        label_neighb = tk.Label(
            self.options_frame, text="Neighbourhood type", font=("Courier 12")
        )
        label_neighb.pack()
        choice_neighb_NM = tk.Radiobutton(
            self.options_frame, text="Moore", variable=self.neighb_type, value="NM"
        )
        choice_neighb_NM.pack()
        choice_neighb_NN = tk.Radiobutton(
            self.options_frame,
            text="von Neumann",
            variable=self.neighb_type,
            value="NN",
        )
        choice_neighb_NN.pack()
        self.stop_btn = tk.Button(
            self.options_frame, text="Done", command=self.save_options
        )
        self.stop_btn.pack(side=tk.LEFT)
        self.options_frame.pack()

    def save_options(self):
        """
        Saves custom options entered by the user.
        If user provides incorrect values, an error message will be displayed.

        Raises:
            ValueError:     When one or more values is missing.
        """
        try:
            utils.OPTIONS.range = int(self.entry_range.get())
            utils.OPTIONS.states = int(self.entry_states.get())
            utils.OPTIONS.s_range = [
                int(self.entry_s_min.get()),
                int(self.entry_s_max.get()),
            ]
            utils.OPTIONS.b_range = [
                int(self.entry_b_min.get()),
                int(self.entry_b_max.get()),
            ]
            utils.OPTIONS.mid = self.middle_opt.get()
            utils.OPTIONS.neighb = self.neighb_type.get()
            check_user_options()
        except ValueError:
            error_msg("Missing values", "All values must be provided.")

        self.options_frame.pack_forget()
        self.start_frame.pack()

    def file_options(self):
        """
        Window for entering a path to json file with custom parameters.
        """
        self.file_frame = tk.Frame(self.root, width=WIDTH, height=HEIGHT)
        filepath_entry = tk.Label(
            self.file_frame, text="File path", font=("Courier 12")
        )
        filepath_entry.pack()
        self.entry_filepath = tk.Entry(self.file_frame, text="", bd=5)
        self.entry_filepath.pack()
        self.path_btn = tk.Button(
            self.file_frame, text="Done", command=self.save_file_options
        )
        self.path_btn.pack(side=tk.LEFT)
        self.start_frame.pack_forget()
        self.file_frame.pack()

    def save_file_options(self):
        """
        Saves file path provided by the user.
        """
        path = self.entry_filepath.get()
        utils.OPTIONS = utils.load_params(path)
        self.file_frame.pack_forget()
        self.start_frame.pack()

    def sleep_option(self):
        """
        Window for manually specifying custom parameters.
        Parameters to fill are: range, states, middle, neighbourhood type.
        """
        self.start_frame.pack_forget()
        self.sleep_opt_frame = tk.Frame(self.root, width=WIDTH, height=HEIGHT)
        self.sleep_opt = tk.StringVar()
        label_sleep_time = tk.Label(
            self.sleep_opt_frame, text="Sleep in seconds", font=("Courier 12")
        )
        label_sleep_time.pack()
        self.entry_sleep_time = tk.Entry(self.sleep_opt_frame, text="", bd=5)
        self.entry_sleep_time.pack()

        self.sleep_opt_btn = tk.Button(
            self.sleep_opt_frame, text="Done", command=self.save_sleep
        )
        self.sleep_opt_btn.pack(side=tk.LEFT)
        self.sleep_opt_frame.pack()

    def save_sleep(self):
        """
        Saves custom options entered by the user.
        """
        utils.OPTIONS.sleep_time = float(self.entry_sleep_time.get())
        self.sleep_opt_frame.pack_forget()
        self.start_frame.pack()

    def resleep(self):
        """
        Return to previous time setup.
        """
        utils.OPTIONS.sleep_time = SLEEP

    def start(self):
        """
        Starts game with random parameters.
        """
        self.board = BoardWindow(
            utils.OPTIONS.range, utils.OPTIONS.range, utils.OPTIONS.states
        )
        self.root.update()
        #self.proc = Process(target=self.run, args=(utils.OPTIONS.states, utils.OPTIONS.range, utils.OPTIONS.range))
        #self.proc.start()
        self.run(utils.OPTIONS.states, utils.OPTIONS.range, utils.OPTIONS.range)

    def run(self, states, height, width):
        """
        Runs the game. Updates window with game display each time new board becomes available.
        """
        while True:
            new_version = new_board(
                states, height, width
            )  # TODO: pass as param - self.game_engine)
            self.board.update(new_version)
            pygame.display.flip()
            self.root.update()
            sleep(utils.OPTIONS.sleep_time)

    def stop(self):
        """
        Stops the game and closes all windows.
        """
        #self.proc.join()
        pygame.quit()
        self.root.quit()


def error_msg(title, msg):
    messagebox.showerror(title, msg)


def check_user_options():
    if not (1 <= utils.OPTIONS.range <= 10):
        error_msg("Incorrect data", "Range must be in [1, 10]")
    if not (1 <= utils.OPTIONS.states <= 25):
        error_msg("Incorrect data", "States must be in [1, 25]")
    if not (1 <= utils.OPTIONS.s_range[0] <= 25) or not (
        1 <= utils.OPTIONS.s_range[1] <= 25
    ):
        error_msg("Incorrect data", "Survive count must be in [1, 25]")
    if not (1 <= utils.OPTIONS.b_range[0] <= 25) or not (
        1 <= utils.OPTIONS.b_range[1] <= 25
    ):
        error_msg("Incorrect data", "Birth count must be in [1, 25]")


def new_board(states, height, width):
    board = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            board[y][x] = random.randint(0, states - 1)
    return board


def main():
    # game_engine = generatedBoardEngineModuleName.PySomeClass()
    game_engine = "place holder"
    game = UserOptions(game_engine)
    while True:
        game.root.update()


main()
# https://stackoverflow.com/questions/23319059/embedding-a-pygame-window-into-a-tkinter-or-wxpython-frame
