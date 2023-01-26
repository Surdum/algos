from single_array import SingleArray
from vector_array import VectorArray
from factor_array import FactorArray
from matrix_array import MatrixArray
from datetime import datetime
from time import time


def test_add_array(data, total):
    start = time()
    for j in range(0, total):
        data.add(datetime.now())
    print(data.__class__, "test_add_array:", time() - start)


def test_pure_list(total):
    start = time()
    d = list()
    for j in range(0, total):
        d.append(datetime.now())
    print(d.__class__, "test_pure_list:", time() - start)


single_array = SingleArray()
vector_array = VectorArray()
factor_array = FactorArray(factor=120)
matrix_array = MatrixArray()


class BuiltInList(list):
    def add(self, item):
        super().append(item)


builtin_list = BuiltInList()

print('Performance by adding 10.000 elements')
test_add_array(single_array, 10_000)
test_add_array(vector_array, 10_000)
test_add_array(factor_array, 10_000)
test_add_array(matrix_array, 10_000)
test_add_array(builtin_list, 10_000)
test_pure_list(10_000)

"""

"""
