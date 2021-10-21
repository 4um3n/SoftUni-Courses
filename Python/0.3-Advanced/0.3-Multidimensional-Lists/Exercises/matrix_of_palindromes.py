rows, cols = [int(n) for n in input().split()]
matrix = [[chr(fl) + chr(fl+c) + chr(fl) for c in range(cols)] for fl in range(ord('a'), ord('a') + rows)]
[print(' '.join(matrix[r])) for r in range(len(matrix))]
