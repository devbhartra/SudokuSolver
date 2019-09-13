from sys import argv
from math import sqrt
from typing import List
from time import sleep

class Sudoku:
	def __init__(self, sudoku: List[List[int]]):
		'''
		:param sudoku: int[n][n]
		:attr N: n * n
		'''
		self.board = sudoku
		self.N = len(self.board[0])
		self.n = int(sqrt(self.N))
		self.sep = "\n" + ("+ " + ("- " * self.n)) * self.n + "+"
		self.s = 1 / self.N / 2

	def valid(self, r: int, c: int, num: int) -> bool:
		'''
		:param r, c: current position (rth row, cth col)
		:returns True if num can be placed at board[r, c] else False
		'''
		R, C = (r // self.n) * self.n, (c // self.n) * self.n

		for i in range(self.N):
			if num in (self.board[r][i], self.board[i][c], self.board[R + (i % self.n)][C + (i // self.n)]): return False

		return True

	def solve(self, r: int = 0, c: int = 0, verbose=0) -> bool:
		'''
		:param r, c: current position (rth row, cth col)
		:recursively tries to solve the sudoku by trying to place numbers from [r, c]
		'''
		if r > self.N and c > self.N: return True

		if self.board[r][c]: return self.solve(r, c + 1, verbose) if c + 1 < self.N else (self.solve(r + 1, 0, verbose) if r + 1 < self.N else True)

		for i in range(1, self.N + 1):
			if self.valid(r, c, i):
				if verbose:
					sleep(self.s)
					print("\033c", end='')
					self.disp()
				self.board[r][c] = i

				if self.solve(r, c, verbose): return True
				else: self.board[r][c] = 0

		return False

	def disp(self):
		print(self.sep)
		[print((("| " + "{} " * self.n) * self.n + "|").format(*('{:x}'.format(j) if j else " " for j in self.board[i])), self.sep if not (i + 1) % self.n else "") for i in range(self.N)]


def main():
	try:
		with open(argv[1], "r") as f: sudoku = Sudoku([list(map(lambda x: int(x, 16), x.split())) for x in f])
		solved = sudoku.solve(verbose=int(argv[2]))
		print("\033c", end='')
		sudoku.disp()
		print("Solved" if solved else "No Solution")
	except Exception as e:
		# print(f"Error! {e}")
		print(f"Usage python(3) {argv[0]} filename 0/1 {{1 for solution with steps. 0 for only final solution}}")
		print("file contains n lines of n space separated integers between 1 and n")
		exit(1)

# 0 0 0 2 6 0 7 0 1
# 6 8 0 0 7 0 0 9 0
# 1 9 0 0 0 4 5 0 0
# 8 2 0 1 0 0 0 4 0
# 0 0 4 6 0 2 9 0 0
# 0 5 0 0 0 3 0 2 8
# 0 0 9 3 0 0 0 7 4
# 0 4 0 0 5 0 0 3 6
# 7 0 3 0 1 8 0 0 0

if __name__ == '__main__':
	main()
