#include "BoardEngine.hpp"

BoardEngine::BoardEngine(int board_height, int board_width) {
	this->board_height = board_height;
	this->board_width = board_width;
	// this->board_array = std::vector<std::vector<int> >(board_height, std::vector<int>(board_width));
	this->board_array = twoDimVec(board_height, std::vector<int>(board_width));
}

twoDimVec BoardEngine::get_board_array() {
	return this->board_array;
}

void BoardEngine::print_board_array() {
	for (int i = 0; i < this->board_array.size(); i++) {
		for (int j = 0; j < this->board_array[i].size(); j++) {
			std::cout << this->board_array[i][j];
		}
		std::cout << "\n";
	}
}