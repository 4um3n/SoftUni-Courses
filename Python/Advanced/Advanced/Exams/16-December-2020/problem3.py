def get_magic_triangle(n, r=0, matrix=[]):
    if r == n:
        return matrix

    matrix.append([1 for _ in range(r+1)])
    for c in range(1, len(matrix[r]) - 1):
        matrix[r][c] += (matrix[r-1][c-1] + matrix[r-1][c]) - 1

    return get_magic_triangle(n, r+1, matrix)
