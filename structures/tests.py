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


single_array = SingleArray()
vector_array = VectorArray()
factor_array = FactorArray()
matrix_array = MatrixArray()

test_add_array(single_array, 10_000)
test_add_array(vector_array, 10_000)
test_add_array(factor_array, 10_000)
test_add_array(matrix_array, 10_000)

