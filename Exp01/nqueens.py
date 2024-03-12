def attack(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def placing_queens(board, row, n):
    if row >= n:
        return True
    
    for col in range(n):
        if attack(board, row, col, n):
            board[row][col] = 1
            
            if placing_queens(board, row + 1, n):
                return True
            
            board[row][col] = 0
    
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    
    if not placing_queens(board, 0, n):
        print("No solution exists.")
        return
    
    print("The positions of queens where they don't attack each other:")
    print_board(board)

def main():
    n = int(input("Enter the number of queens: "))
    solve_n_queens(n)

if __name__ == "__main__":
    main()
