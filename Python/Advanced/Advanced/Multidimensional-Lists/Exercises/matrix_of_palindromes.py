rows, cols = [int(n) for n in input().split()]
matrix = [[chr(fl) + chr(fl+x) + chr(fl) for x in range(cols)] for fl in range(ord('a'), ord('a') + rows)]
[print(' '.join(matrix[r])) for r in range(len(matrix))]
