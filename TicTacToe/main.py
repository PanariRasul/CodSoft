import copy

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("---------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            print("Invalid move. The position is already taken. Choice diffrent position")
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                return self.board[i]

        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                return self.board[i]

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]

        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]

        return None

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.check_winner() or self.is_board_full()

    def get_empty_positions(self):
        return [i for i, value in enumerate(self.board) if value == ' ']

def minimax(board, depth, maximizing_player):
    if board.is_game_over():
        winner = board.check_winner()
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.get_empty_positions():
            new_board = copy.deepcopy(board)
            new_board.make_move(move)
            eval = minimax(new_board, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for move in board.get_empty_positions():
            new_board = copy.deepcopy(board)
            new_board.make_move(move)
            eval = minimax(new_board, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = -1

    for move in board.get_empty_positions():
        new_board = copy.deepcopy(board)
        new_board.make_move(move)
        move_val = minimax(new_board, 0, False)

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move

def main():
    game = TicTacToe()

    while not game.is_game_over():
        game.print_board()

        if game.current_player == 'X':
            position = int(input("Enter your move (1-9): ")) - 1
            if 0 <= position <= 8 and game.make_move(position):
                pass
            else:
                print("Invalid move. Please try again.")
                continue
        else:
            print("AI is making a move...")
            position = find_best_move(game)
            game.make_move(position)

    game.print_board()

    winner = game.check_winner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("Thank You For Playing It's a Tie!")

if __name__ == "__main__":
    main()
