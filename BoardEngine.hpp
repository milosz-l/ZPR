#ifndef BoardEngine_H
#define BoardEngine_H
#include <array>
#include <iostream>

const int NUM_OF_ROWS = 2;
const int NUM_OF_COLS = NUM_OF_ROWS;

struct GameParameters {
	int range = 1;							 // range of neighborhood
	int count_of_states = 2;				 // number of possible states (starts from 0)
	bool count_middle = false;				 // defines whether to count middle cell when counting cells in neighborhood
	int alive_min = 2;						 // Smin
	int alive_max = 3;						 // Smax
	int be_born_min = 3;					 // Bmin
	int be_born_max = 3;					 // Bmax
	bool neighborhood_type_is_moore = true;	 // defines whether neighborhood type is NM or NN
};

typedef int CellValue;
typedef std::array<CellValue, NUM_OF_COLS> Row;
typedef std::array<Row, NUM_OF_ROWS> Board;

class BoardEngine {
	// const GameParameters parameters;
	Board current_board;
	Board previous_board;

   public:
	BoardEngine();
	BoardEngine(const Board &starting_board);
	void set_cell(int row_num, int col_num, int new_value);
	void print_current_board() const;
	void calculate_next_state();
};

#endif