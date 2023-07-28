import numpy as np

b = np.array([1, 55, 9, 33, 5, 6, 7, 95, 11, 1, 11, 121, 13, 14, 152, 16333, 17, 180, 19, 2033])
b_arg = b.argsort()
#artsort => 작은 숫자대로 오름차순 나열 (인덱스 기준으로)
print(b_arg)
print(b_arg[:-11:-1]) # == print(3, b[-1:-11:-1])