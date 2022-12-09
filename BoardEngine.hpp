#ifndef BoardEngine_H
#define BoardEngine_H
#include <array>
#include <iostream>

const int NUM_OF_ROWS = 2;
const int NUM_OF_COLS = NUM_OF_ROWS;

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