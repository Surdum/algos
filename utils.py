class MatrixOperations:
    def multiply(self, m1, m2):
        if len(m1[0]) != len(m2):
            raise Exception("First matrix column count does not equal second matrix row count")
        new_matrix = [[0 for __ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    new_matrix[i][j] += m1[i][k] * m2[k][j]
        return new_matrix

    def power(self, mat, p):
        d = mat
        res = None
        for bit in bin(p)[2:][::-1]:
            if bit == '1':
                if res is None:
                    res = d
                else:
                    res = self.multiply(res, d)
            d = self.multiply(d, d)
        return res or 1


def generate_shuffled_number_sequence(n):
    from random import shuffle
    numbers = list(range(n))
    shuffle(numbers)
    return numbers


def generate_random_number_sequence(n, t):
    from random import randint
    return [randint(0, t) for _ in range(n)]


if __name__ == '__main__':
    matrix = MatrixOperations()
    # mat2 = \
    #     [[1, 2, 3]]
    # mat1 = \
    #     [[4],
    #      [5],
    #      [6]]
    # mat3 = matrix.multiply(mat1, mat2)
    # for line in mat3:
    #     print(line)

    base_mat = \
        [[1, 1],
         [1, 0]]

    new_ = matrix.power(base_mat, 1)
    print(new_)

