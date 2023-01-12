#include "BoardEngine.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

// #include <cstdlib>

namespace py = pybind11;

BoardEngine::BoardEngine() {
	// fill board with zeros
	for (int row_num = 0; row_num < NUM_OF_ROWS; ++row_num) {
		this->current_board[row_num].fill(0);
	}
}

BoardEngine::BoardEngine(const Board &starting_board) {
	// set current board to a board given as an argument
	this->current_board = starting_board;
}

void BoardEngine::set_cell(int row_num, int col_num, int new_value) {
	// sets cell with given coordinates to given state
	this->current_board[row_num][col_num] = new_value;
}

void BoardEngine::print_current_board() const {
	// prints current board
	for (int i = 0; i < this->current_board.size(); i++) {
		for (int j = 0; j < this->current_board[i].size(); j++) {
			std::cout << this->current_board[i][j];
		}
		std::cout << "\n";
	}
}

Board BoardEngine::get_board() const {
	// returns board
	return this->current_board;
}

void BoardEngine::change_random_cell() {
	// set random cell to random state
	int random_cell_row = get_random_number_from_range(0, NUM_OF_ROWS - 1);
	int random_cell_col = get_random_number_from_range(0, NUM_OF_COLS - 1);
	int random_cell_state = get_random_number_from_range(0, parameters.count_of_states - 1);
	set_cell(random_cell_row, random_cell_col, random_cell_state);
}

void BoardEngine::randomize_board(int num_of_random_cells) {
	// changes random cell given number of times
	for (int i = 0; i < num_of_random_cells; i++) {
		change_random_cell();
	}
}

void BoardEngine::calculate_next_state() {
	// calculate next state of board using LTL algorithm
	// TODO
}

int BoardEngine::get_random_number_from_range(int min, int max) const {
	return min + (rand() % static_cast<int>(max - min + 1));
}

PYBIND11_MODULE(generatedBoardEngineModuleName, handle) {
	handle.doc() = "this is a class generated from cpp";
	py::class_<BoardEngine>(
		handle, "PySomeClass")
		.def(py::init<>())
		.def("set_cell", &BoardEngine::set_cell)
		.def("print_current_board", &BoardEngine::print_current_board)
		.def("get_board", &BoardEngine::get_board)
		.def("randomize_board", &BoardEngine::randomize_board)
		.def("calculate_next_state", &BoardEngine::calculate_next_state);
}