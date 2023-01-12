#ifndef BoardEngine_H
#define BoardEngine_H
#include <array>
#include <iostream>

const int NUM_OF_ROWS = 30;
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
	const GameParameters parameters;
	Board current_board;
	Board previous_board;

   public:
	BoardEngine();
	BoardEngine(const Board &starting_board);
	void set_cell(int row_num, int col_num, int new_value);
	void print_current_board() const;
	Board get_board() const;
	void change_random_cell();
	void randomize_board(int num_of_random_cells);
	void calculate_next_state();

   private:
	bool cell_is_dead(CellValue) const;
	bool cell_is_alive(CellValue) const;
	int add_bias_to_coordinate(int bias, int coordinate, int max_coordinate_value) const;
	// int count_neighbours_in_row(int row_num, int col_num, int bias) const;
	bool BoardEngine::cell_in_neighbourhood(int current_row, int current_col, int center_row, int center_col) const;
	int count_neighbours(int row_num, int col_num, int max_num_of_neighbours) const;
	bool dead_cell_should_be_born(int row_num, int col_num) const;
	bool state_one_cell_should_survive(int row_num, int col_num) const;
	int get_random_number_from_range(int min, int max) const;
};

#endif