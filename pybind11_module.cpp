#include <pybind11/pybind11.h>

#include <iostream>

#include "BoardEngine.hpp"

namespace py = pybind11;

void test_pybind_cpp_function() {
	int NUM_OF_ROWS = 2;
	int NUM_OF_COLS = 2;
	BoardEngine board = BoardEngine();
	board.print_current_board();
	std::cout << "\n";

	board.set_cell(0, 0, 1);
	board.set_cell(1, 0, 1);
	board.set_cell(1, 1, 1);
	board.print_current_board();
	std::cout << "\n";

	board.calculate_next_state();
	board.print_current_board();
}

PYBIND11_MODULE(module_name, handle) {
	handle.doc() = "This module is an engine for LargerThanLife game. It's used to calculate next state of the gameboard.";
	handle.def("cpp_function", &test_pybind_cpp_function);
}