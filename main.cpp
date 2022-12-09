#include <iostream>

#include "BoardEngine.hpp"

int main() {
	BoardEngine board = BoardEngine(2, 2);
	board.print_board_array();
	return 0;
}