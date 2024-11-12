#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col) on the board."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N Queens problem and return all possible solutions."""
    def backtrack(row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * N
    solutions = []
    backtrack(0)
    return solutions


def main():
    """Main function to handle input and output for N Queens."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
