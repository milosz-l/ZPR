#ifndef BoardEngine_H
#define BoardEngine_H
#include <iostream>
#include <vector>

using twoDimVec = std::vector<std::vector<int> >;

class BoardEngine {
	// const GameParameters parameters;
	int board_height;
	int board_width;
	twoDimVec board_array;

   public:
	BoardEngine(int board_height, int board_width);
	twoDimVec get_board_array();
	void set_cell(int row_num, int col_num, int new_value);
	void print_board_array();
};

#endif