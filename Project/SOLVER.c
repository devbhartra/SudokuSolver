#include <stdio.h>
#include <stdlib.h>

int valid(int sudoku[9][9], int r, int c, int num);
int solve(int sudoku[9][9], int r, int c);
void print(int sudoku[9][9]);

int valid(int sudoku[9][9], int r, int c, int num) {
	int rStart = (r / 3) * 3, cStart = (c / 3) * 3;
	for (int i = 0; i < 9; i++) if (sudoku[r][i] == num || sudoku[i][c] == num || sudoku[rStart + (i % 3)][cStart + (i / 3)] == num) return 0;
	return 1;
}

int solve(int sudoku[9][9], int r, int c) {
	if (r > 9 && c > 9) return 1;
	if (sudoku[r][c]) {
		if (c + 1 < 9) return solve(sudoku, r, c + 1);
		else if (r + 1 < 9) return solve(sudoku, r + 1, 0);
		else return 1;
	}
	else {
		for (int i = 0; i < 9; i++) {
			if (valid(sudoku, r, c, i + 1)) {
				sudoku[r][c] = i + 1;
				if (solve(sudoku, r, c)) return 1;
				else sudoku[r][c] = 0;
			}
		}
	}
	return 0;
}

void print(int sudoku[9][9]) {
	printf("+ - - - + - - - + - - - +\n");
	for (int i = 0; i < 9; i++) {
		printf("|");
		for (int j = 0; j < 9; j++) {
			if (sudoku[i][j]) printf(" %d", sudoku[i][j]);
			else printf("  ");
			if (!((j + 1) % 3)) printf(" |");
		}
		printf("\n");
		if (!((i + 1) % 3)) printf("+ - - - + - - - + - - - +\n");
	}
}

int main(int argc, char const *argv[]) {
	int sudoku[9][9];
	if (argc < 2) { printf("Enter valid filename\n"); exit(1); }
	FILE *f = fopen(argv[1], "r");
	for (int i = 0; i < 9; i++) for (int j = 0; j < 9; j++) fscanf(f, "%d", &sudoku[i][j]);
	fclose(f);
	print(sudoku);
	if (solve(sudoku, 0, 0)) print(sudoku);
	else printf("NO SOLUTION");
}
