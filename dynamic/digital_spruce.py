from copy import deepcopy


def solve(orig_t) -> None:
    t = deepcopy(orig_t)
    for i in range(len(t) - 2, -1, -1):
        for j in range(i + 1):
            t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])
    return t[0][0]


if __name__ == '__main__':
    tree = [
           [1],
          [2, 3],
         [4, 5, 6],
        [9, 8, 0, 3]
    ]
    res = solve(tree)
    print(res)
