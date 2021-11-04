def missing_number(matrix, S):
    contains = set()
    for row in matrix:
        contains |= set(row)
    missing_num = (S - contains).pop()
    for row in matrix:
        if '?' in row:
            row[row.index("?")] = missing_num
            break
    return missing_num, matrix

def sort_matrices(matrices):
    S = set('?') | set([str(i) for i in list(range(1, 17))])
    res = []
    for i, matrix in enumerate(matrices):
        num, new_matrix = missing_number(matrix, S)
        res.append((num, i))
        matrices[i] = new_matrix
    res.sort()
    return [matrices[i] for num, i in res]
