def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    rw_len = len(mat[0])
    for rw in mat:
        if len(rw) != rw_len:
            raise 'ValueError'

    rw, cl = len(mat), rw_len
    result = []

    for j in range(cl):
        t = 0
        for i in range(rw):
            t += mat[i][j]
        result.append(float(t))
    return result


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
