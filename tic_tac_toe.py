# Working on computer AI
# Simple Tic Tac Toe game for two players
print("Welcome to Tic Tac Toe!") 
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    lines = board + [list(col) for col in zip(*board)]  # rows and columns
    lines.append([board[i][i] for i in range(3)])        # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])    # anti diagonal
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return line[0]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"
    while True:
        print_board(board)
        print(f"{current}'s turn. Enter row and column (0, 1, or 2): ")
        try:
            row = int(input("Row: "))
            col = int(input("Col: "))
            if board[row][col] == " ":
                board[row][col] = current
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"{winner} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                current = "O" if current == "X" else "X"
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Use numbers 0, 1, or 2.")
            
if __name__ == "__main__":
    main()
    
