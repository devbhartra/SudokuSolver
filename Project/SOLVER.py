from sys import argv; from math import sqrt
try: f = open(argv[1], "r")
except FileNotFoundError as e:
	print("Enter Valid Filename")
	quit()
sudoku = [[int(i, 16) for i in x.split()] for x in f]
f.close()
N = len(sudoku[0]); n = int(sqrt(N)); s = "\n" + ("+ " + ("- " * n)) * n + "+"
def valid(sudoku, r, c, num):
	R, C = (r // n) * n, (c // n) * n
	for i in range(N):
		if num in (sudoku[r][i], sudoku[i][c], sudoku[R + (i % n)][C + (i // n)]): return 0
	return 1
def solve(sudoku, r = 0, c = 0):
	if r > N and c > N: return 1
	if sudoku[r][c]: return solve(sudoku, r, c + 1) if c + 1 < N else (solve(sudoku, r + 1, 0) if r + 1 < N else 1)
	else:
		for i in range(1, N + 1):
			if valid(sudoku, r, c, i):
				sudoku[r][c] = i
				if solve(sudoku, r, c): return 1
				else: sudoku[r][c] = 0
	return 0
def disp(sudoku):
	print(s)
	[print((("| " + "{} " * n) * n + "|").format(*('{:x}'.format(j) if j else " " for j in sudoku[i])), s if not (i + 1) % n else "") for i in range(N)]
disp(sudoku)
disp(sudoku) if solve(sudoku) else print("NO SOLUTION")