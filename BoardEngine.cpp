#include "BoardEngine.hpp"

BoardEngine::BoardEngine() {
	// fill with zeros
	for (int row_num = 0; row_num < NUM_OF_ROWS; ++row_num) {
		this->current_board[row_num].fill(0);
	}
}

BoardEngine::BoardEngine(const Board &starting_board) {
	this->current_board = starting_board;
}

void BoardEngine::set_cell(int row_num, int col_num, int new_value) {
	this->current_board[row_num][col_num] = new_value;
}

void BoardEngine::print_current_board() const {
	for (int i = 0; i < this->current_board.size(); i++) {
		for (int j = 0; j < this->current_board[i].size(); j++) {
			std::cout << this->current_board[i][j];
		}
		std::cout << "\n";
	}
}

void BoardEngine::calculate_next_state() {
}