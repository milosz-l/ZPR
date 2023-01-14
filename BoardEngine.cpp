#include "BoardEngine.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <iostream>

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

// BoardEngine::BoardEngine(const GameParameters &user_parameters) {
// 	// set parameters to parameters given as an argument
// 	this->parameters = user_parameters;
// }

// BoardEngine::BoardEngine(const GameParameters &user_parameters, const Board &starting_board) {
// 	// set parameters and board to those given as parameters
// 	this->parameters = user_parameters;
// 	this->current_board = starting_board;
// }

// BoardEngine::BoardEngine(const int Rr, const int Cc, const bool Mm, const int Smin, const int Smax, const int Bmin, const int Bmax, const std::string Nn) {
// 	parameters.range = Rr;
// 	parameters.count_of_states = Cc;
// 	parameters.count_middle = Mm;
// 	parameters.alive_min = Smin;
// 	parameters.alive_max = Smax;
// 	parameters.be_born_min = Bmin;
// 	parameters.be_born_max = Bmax;
// 	parameters.neighb = Nn;
// }

void BoardEngine::set_parameters(const int Rr, const int Cc, const bool Mm, const int Smin, const int Smax, const int Bmin, const int Bmax, const std::string Nn) {
	parameters.range = Rr;
	if (Cc <= 2) {
		parameters.count_of_states = 2;	 // convert Cc 0 or 1 to 2
	} else {
		parameters.count_of_states = Cc;
	}
	parameters.count_middle = Mm;
	parameters.alive_min = Smin;
	parameters.alive_max = Smax;
	parameters.be_born_min = Bmin;
	parameters.be_born_max = Bmax;
	parameters.neighb = Nn;
}

void BoardEngine::set_cell(int row_num, int col_num, int new_value) {
	// sets cell with given coordinates to given state
	this->current_board[row_num][col_num] = new_value;
}

void BoardEngine::print_current_board() const {
	// prints current board
	for (int i = 0; i < this->current_board.size(); ++i) {
		for (int j = 0; j < this->current_board[i].size(); ++j) {
			std::cout << this->current_board[i][j];
		}
		std::cout << "\n";
	}
}

Board BoardEngine::get_board() const {
	// returns board
	return this->current_board;
}

int BoardEngine::get_height() const {
	return NUM_OF_ROWS;
}

int BoardEngine::get_width() const {
	return NUM_OF_COLS;
}

// int BoardEngine::get_range() const {
// 	return parameters.range;
// }

// int BoardEngine::get_count_of_states() const {
// 	return parameters.count_of_states;
// }

// bool BoardEngine::get_count_middle() const {
// 	return parameters.count_middle;
// }

// int BoardEngine::get_alive_min() const {
// 	return parameters.alive_min;
// }

// int BoardEngine::get_alive_max() const {
// 	return parameters.alive_max;
// }

// int BoardEngine::get_be_born_min() const {
// 	return parameters.be_born_min;
// }

// int BoardEngine::get_be_born_max() const {
// 	return parameters.be_born_max;
// }

// std::string BoardEngine::get_neighb() const {
// 	return parameters.neighb;
// }

void BoardEngine::change_random_cell() {
	// set random cell to random state
	int random_cell_row = get_random_number_from_range(0, NUM_OF_ROWS - 1);
	int random_cell_col = get_random_number_from_range(0, NUM_OF_COLS - 1);
	int random_cell_state = get_random_number_from_range(0, parameters.count_of_states - 1);
	set_cell(random_cell_row, random_cell_col, random_cell_state);
}

void BoardEngine::randomize_board(int num_of_random_cells) {
	// changes random cell given number of times
	for (int i = 0; i < num_of_random_cells; ++i) {
		change_random_cell();
	}
}

void BoardEngine::calculate_next_state() {
	// calculate next state of board using LTL algorithm
	previous_board = current_board;
	for (int row_num = 0; row_num < NUM_OF_ROWS; ++row_num) {
		for (int col_num = 0; col_num < NUM_OF_COLS; ++col_num) {
			CellValue cell_value = current_board[row_num][col_num];
			// if (cell_is_dead(cell_value)) {
			// 	if (dead_cell_should_be_born(row_num, col_num)) {
			// 		current_board[row_num][col_num] = 1;  // set cell's value to alive
			// 	}
			// } else if (cell_value > 1 || state_one_cell_should_survive(row_num, col_num)) {
			// 	++current_board[row_num][col_num];
			// 	if (current_board[row_num][col_num] >= parameters.count_of_states) {
			// 		current_board[row_num][col_num] = 0;
			// 	}
			// }
			if (cell_is_dead(cell_value)) {
				if (dead_cell_should_be_born(row_num, col_num)) {
					current_board[row_num][col_num] = 1;  // set cell's value to alive
				}
			} else if (cell_is_alive(cell_value) && cell_should_be_incremented(row_num, col_num)) {
				if (!(cell_value + 1 > parameters.count_of_states - 1))
					++current_board[row_num][col_num];	// increment cell
			} else if (cell_is_alive(cell_value) && !cell_should_be_incremented(row_num, col_num)) {
				if (!(cell_value - 1 < 0))
					--current_board[row_num][col_num];	// decrement cell
			}
		}
	}
}

bool BoardEngine::cell_should_be_incremented(int row_num, int col_num) const {
	CellValue cell_value = previous_board[row_num][col_num];
	int count_of_neighbours = count_neighbours(row_num, col_num, parameters.alive_max);
	if (count_of_neighbours >= parameters.alive_min && count_of_neighbours <= parameters.alive_max) {
		return true;
	} else {
		return false;
	}
}

bool BoardEngine::cell_is_dead(CellValue cell_value) const {
	if (cell_value == 0) {
		return true;
	} else {
		return false;
	}
}

bool BoardEngine::cell_is_alive(CellValue cell_value) const {
	if (cell_value > 0) {
		return true;
	} else {
		return false;
	}
}

int BoardEngine::add_bias_to_coordinate(int bias, int coordinate, int max_coordinate_value) const {
	// returns a coordinate with added bias (adjusts range if needed)
	int new_coordinate = coordinate + bias;
	if (new_coordinate < 0) {
		return 0;
	} else if (new_coordinate > max_coordinate_value - 1) {
		return max_coordinate_value - 1;
	} else {
		return new_coordinate;
	}
}

bool BoardEngine::cell_in_neighbourhood(int current_row, int current_col, int center_row, int center_col) const {
	// return whether a (current_row, current_col) cell should be counted as a neighbor of (center_row, center_col) cell
	// type of neighborhood is defined in GameParameters
	if (parameters.neighb == "NM") {
		return true;
	} else {
		int vertical_distance = abs(current_row - center_row);
		int horizontal_distance = abs(current_col - center_col);
		if ((vertical_distance + horizontal_distance) <= parameters.range) {
			return true;
		}
		return false;
	}
}

int BoardEngine::count_neighbours(int row_num, int col_num, int max_num_of_neighbours) const {
	// returns the number of neighbours in range specified in GameParameters for given cell coordinates
	// uses neighbourhood type specified in GameParameters
	// if count of neighbours is bigger than max_num_of_neighbours, the function immediately returns max_num_of_neighbours + 1
	int count = 0;
	int first_row_num = add_bias_to_coordinate(-parameters.range, row_num, NUM_OF_ROWS);
	int last_row_num = add_bias_to_coordinate(parameters.range, row_num, NUM_OF_ROWS);
	int first_col_num = add_bias_to_coordinate(-parameters.range, col_num, NUM_OF_COLS);
	int last_col_num = add_bias_to_coordinate(parameters.range, col_num, NUM_OF_COLS);

	for (int current_row = first_row_num; current_row <= last_row_num; ++current_row) {
		for (int current_col = first_col_num; current_col <= last_col_num; ++current_col) {
			if (cell_in_neighbourhood(current_row, current_col, row_num, col_num) && previous_board[current_row][current_col] == 1) {
				++count;
				if (current_row == row_num && current_col == col_num && !parameters.count_middle) {
					--count;
				}
			}
			if (count > max_num_of_neighbours) {
				return max_num_of_neighbours + 1;
			}
		}
	}
	// if (!parameters.count_middle && previous_board[row_num][col_num] == 1) {
	// 	--count;
	// }
	// std::cout << "count of neighbours for " << row_num << ", " << col_num << " equals: " << count << ". neighb =  " << parameters.neighb << "\n";
	assert(count >= 0);
	return count;
}

bool BoardEngine::dead_cell_should_be_born(int row_num, int col_num) const {
	CellValue cell_value = previous_board[row_num][col_num];
	assert(cell_is_dead(cell_value));

	int count_of_neighbours = count_neighbours(row_num, col_num, parameters.be_born_max);
	if (count_of_neighbours >= parameters.be_born_min && count_of_neighbours <= parameters.be_born_max) {
		return true;
	} else {
		return false;
	}
}

bool BoardEngine::state_one_cell_should_survive(int row_num, int col_num) const {
	// returns whether a cell with state equal to one should survive according to  alive_min and alive_max
	CellValue cell_value = previous_board[row_num][col_num];
	assert(cell_value == 1);
	int count_of_neighbours = count_neighbours(row_num, col_num, parameters.alive_max);
	if (count_of_neighbours >= parameters.alive_min && count_of_neighbours <= parameters.alive_max) {
		return true;
	} else {
		return false;
	}
}

int BoardEngine::get_random_number_from_range(int min, int max) const {
	return min + (rand() % static_cast<int>(max - min + 1));
}

PYBIND11_MODULE(generatedBoardEngineModuleName, handle) {
	handle.doc() = "this is a class generated from cpp";
	py::class_<BoardEngine>(
		handle, "PySomeClass")
		.def(py::init<>())
		.def("set_parameters", &BoardEngine::set_parameters)
		.def("set_cell", &BoardEngine::set_cell)
		.def("print_current_board", &BoardEngine::print_current_board)
		.def("get_board", &BoardEngine::get_board)
		.def("get_height", &BoardEngine::get_height)
		.def("get_width", &BoardEngine::get_width)
		// .def("get_range", &BoardEngine::get_range)	// TODO: maybe remove these params getters
		// .def("get_count_of_states", &BoardEngine::get_count_of_states)
		// .def("get_count_middle", &BoardEngine::get_count_middle)
		// .def("get_alive_min", &BoardEngine::get_alive_min)
		// .def("get_alive_max", &BoardEngine::get_alive_max)
		// .def("get_be_born_min", &BoardEngine::get_be_born_min)
		// .def("get_be_born_max", &BoardEngine::get_be_born_max)
		// .def("get_neighb", &BoardEngine::get_neighb)
		.def("randomize_board", &BoardEngine::randomize_board)
		.def("calculate_next_state", &BoardEngine::calculate_next_state);
}