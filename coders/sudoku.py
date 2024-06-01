from pprint import pprint

#Finds the next row that is not filled
def find_next_empty(puzzle):
  
    #We are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
     #If no spaces in the puzzle are empty
    return None, None 


#Figures out whether the guess at the row or col is a valid guess
def is_valid(puzzle, guess, row, col):
  
    #Start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
      #If we have repeated, this guess is not valid
      return False
      
    #
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #Then the square, 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

#Our puzzle is a list of lists, 
def solve_sudoku(puzzle):

    #Choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    if row is None:
      return True 
      # range(1, 10) is 1, 2, 3, ... 9
      for guess in range(1, 10):
        #Check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        #It not valid or if nothing gets returned true, need try a new number
        puzzle[row][col] = -1

    #When this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
