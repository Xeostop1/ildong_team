import numpy as np
import pickle
import pandas as pd

filename = "./appliedStatistics/load.csv"

# 열(헤더)과 데이터(배열) 분리
cols = None
data = []
with open(filename)as f:
    # 한줄씩 읽기
    for i in f.readlines():
        # ,을 기준으로 나누기
        vals = i.replace("\n", "").split(",")
        if cols is None:
            cols = vals
        else:
            # 리스트 컴프리헨션(list comprehension)
            # 파이썬에서 리스트를 생성하는 간결한 방법
            data.append(float(x) for x in vals)

# 데이터 프레임에 1줄씩 데이터 보내기
d0 = pd.DataFrame(data, columns=cols)
print(d0.dtypes)
d0.head()

# 넘파일 loadtext() 사용→ 굳이 for를 사용하지 않아도 되네 편하다
# 데이터프래임이 아닌 2차원배열로 불러올 수 있음
d1 = np.loadtxt(filename, skiprows=1, delimiter=",")
print(d1.dtype)
# 처음부터 5행까지 모든 열(속성)가져오기
print(d1[:5, :])


# 넘파이 genfromtxt() 사용→ 로드텍스트보다 유연함
# dtype 데이터타입(인트/플로트)을 넘파이가 직접 지정하게 세팅(None)해야 오류가 적음(이 데이터는 소수랑 정수랑 섞여있음)
# names=T을 하게되면 열마다 이름이 부여되면서 1차원 배열로 세팅됨
d2 = np.genfromtxt(filename, delimiter=",", names=True, dtype=None)
print(d2.dtype)
# 처음부터 5행까지 모든 열(속성)가져오기
print(d2[:5])


# 판다스 read_csv 제일 간단하네!***주로 이거사용 
d3 = pd.read_csv(filename)
print(d3.dtypes)
d3.head()

# 피클로 dlfrdjdhrl 
with open("./appliedStatistics/load_pickle.pickle", "rb") as f:
    d4 = pickle.load(f)
print(d4.dtypes)
d4.head()
