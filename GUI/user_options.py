"""
    Module responsible for the GUI:
    - menu with game's options
    - gathering custom game options
    - running main pygame window with board
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from time import sleep
import pygame
from GUI.board_display import BoardWindow, calculate_next_state
from GUI import utils

try:
    from build.Debug import generatedBoardEngineModuleName
except ModuleNotFoundError or ImportError:  # pylint: disable=binary-op-exception
    from build import generatedBoardEngineModuleName

WIDTH = 100
HEIGHT = 100
BOARD_SIZE = 50  # TODO: get this from cpp or the other way
# RANGE = 1  # TODO: get this from cpp or the other way
SLEEP = 0.5


class UserOptions:         # pylint: disable=too-many-instance-attributes,attribute-defined-outside-init
    """
    Class representing main window that enables user to choose and specify options for the game.
    """

    def __init__(self, width: int = WIDTH, height: int = HEIGHT):
        """
        Creates a window for choosing a way to specify game parameters or an option
        to run with default parameters.
        Possible choices:
            Start:  Starts a game if parameters are not provided, game runs with random parameters.
            Custom options: Redirects to a window for typing custom parameters.
            Custome file:   Redirects to a window for specifying path to json file with parameters.
            Save board:     Saves current board to a PNG file.
            Sleep:          Slows down the game.
            Close:  Closes all windows.
        """
        self.root = tk.Tk()
        self.root.title("Game LtL")
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
        img_btn = tk.Button(
            self.start_frame, text="Save board", command=self.save_board
        )
        img_btn.pack()
        sleep_btn = tk.Button(self.start_frame, text="Sleep", command=self.sleep_option)
        sleep_btn.pack()
        resleep_btn = tk.Button(
            self.start_frame, text="Reset sleep", command=self.resleep
        )
        resleep_btn.pack()
        stop_btn = tk.Button(self.start_frame, text="Close", command=self.stop)
        stop_btn.pack()
        self.root.update()

    def options(self):
        """
        Window for manually specifying custom parameters.
        Parameters to fill are: range, states,
        count limits for a state to survive,
        count limits for a dead cell to become a birth,
        middle, neighbourhood type.
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
        choice_neighb_nm = tk.Radiobutton(
            self.options_frame, text="Moore", variable=self.neighb_type, value="NM"
        )
        choice_neighb_nm.pack()
        choice_neighb_nn = tk.Radiobutton(
            self.options_frame,
            text="von Neumann",
            variable=self.neighb_type,
            value="NN",
        )
        choice_neighb_nn.pack()
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
            ValueError:     When one or more values are missing.
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
        try:
            self.path_btn = tk.Button(
                self.file_frame, text="Done", command=self.save_file_options
            )
            self.path_btn.pack(side=tk.LEFT)
        except FileNotFoundError:
            error_msg(
                "File not found",
                "Please provide a valid path. Now redirecting to previous window.",
            )
        finally:
            self.start_frame.pack_forget()
            self.file_frame.pack()

    def save_file_options(self):
        """
        Saves file path provided by the user.
        """
        path = self.entry_filepath.get()
        try:
            utils.OPTIONS = utils.load_params(path)
            check_user_options()
        except FileNotFoundError:
            error_msg(
                "File not found",
                "Please provide a valid path. Now redirecting to previous window.",
            )
        finally:
            self.file_frame.pack_forget()
            self.start_frame.pack()

    def save_board(self):
        """
        Saves currently displayed board as a PNG file.
        Name of the file: board_{current_date_with_time}.
        """
        name = "board_" + datetime.now().strftime("%Y%m%d_%H%M")
        self.board.save_as_img(name)

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
        try:
            utils.OPTIONS.sleep_time = float(self.entry_sleep_time.get())
        except ValueError:
            error_msg("Incorrect values", "Please provide valid float values")
        finally:
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
        self.board = BoardWindow(BOARD_SIZE, BOARD_SIZE, utils.OPTIONS.states)
        self.root.update()
        # self.run(utils.OPTIONS.states, BOARD_SIZE, BOARD_SIZE)
        self.run()

    def run(self):
        """
        Runs the game. Updates window with game display each time new board becomes available.
        """
        game_engine = generatedBoardEngineModuleName.PySomeClass()
        game_engine.set_parameters(
            utils.OPTIONS.range,
            utils.OPTIONS.states,
            utils.OPTIONS.mid,
            min(utils.OPTIONS.s_range),
            max(utils.OPTIONS.s_range),
            min(utils.OPTIONS.b_range),
            max(utils.OPTIONS.b_range),
            utils.OPTIONS.neighb
        )

        # set cells for testing
        game_engine.set_cell(1, 2, 1)
        game_engine.set_cell(2, 1, 1)
        game_engine.set_cell(2, 2, 1)
        game_engine.set_cell(3, 3, 1)
        # game_engine.set_cell(3, 2, 1)

        while True:
            self.board.update(game_engine.get_board())
            pygame.display.flip()
            self.root.update()
            sleep(utils.OPTIONS.sleep_time)
            calculate_next_state(game_engine)

    def stop(self) -> None:
        """
        Stops the game and closes all windows.
        """
        pygame.quit()  # pylint: disable=no-member
        self.root.quit()


def error_msg(title: str, msg: str) -> None:
    """
    Shows pop up window with error message.

    Args:
        title:  Title of the error message.
        msg:    Main text of error message.
    """
    messagebox.showerror(title, msg)


def check_user_options() -> None:
    """
    Verifies values in options provided by the user.
    In case of incorrect data, shows a pop up window with error.
    """
    if not 1 <= utils.OPTIONS.range <= 10:
        error_msg("Incorrect data", "Range must be in [1, 10]")
    if not 1 <= utils.OPTIONS.states <= 25:
        error_msg("Incorrect data", "States must be in [1, 25]")
    if not (1 <= utils.OPTIONS.s_range[0] <= 25) or not (
        1 <= utils.OPTIONS.s_range[1] <= 25
    ):
        error_msg("Incorrect data", "Survive count must be in [1, 25]")
    if not (1 <= utils.OPTIONS.b_range[0] <= 25) or not (
        1 <= utils.OPTIONS.b_range[1] <= 25
    ):
        error_msg("Incorrect data", "Birth count must be in [1, 25]")


def main():
    """Main function."""
    game = UserOptions()
    while True:
        game.root.update()


main()
# https://stackoverflow.com/questions/23319059/embedding-a-pygame-window-into-a-tkinter-or-wxpython-frame
