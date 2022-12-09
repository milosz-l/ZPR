#include <iostream>

#include "BoardEngine.hpp"

int main() {
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

	return 0;
}