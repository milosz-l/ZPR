#include <iostream>
#include <vector>

#include "BoardEngine.hpp"

int main() {
	int NUM_OF_ROWS = 2;
	int NUM_OF_COLS = 2;
	BoardEngine board = BoardEngine(NUM_OF_ROWS, NUM_OF_COLS);
	board.print_board_array();
	std::cout << "\n";

	board.set_cell(0, 0, 1);
	board.set_cell(1, 0, 1);
	board.set_cell(1, 1, 1);
	board.print_board_array();
	std::cout << "\n";

	// board.set_row(NUM_OF_ROWS, std::vector<int>(NUM_OF_COLS, 1));
	// board.print_board_array();
	// std::cout << "\n";

	return 0;
}