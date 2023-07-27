import pandas as pd
import numpy as np

# 데이터셋 로드
df = pd.read_csv("./appliedStatistics/PreparingDatasets/Diabetes.csv")
df.head()

# 0→ null change(변경하고 꼭 변수에 넣기)
df = df.fillna(0)
# 행추가
d2 = df[["Glucose", "BMI", "Age", "Outcome"]]
d2.head()
d2.describe()

# 0값 필터링/TF → any로 T값 변경→ loc T값은 삭제 ~(틸드 사용이래)
df3 = d2.loc[~(d2[d2.columns[:-1]] == 0).any(axis=1)]
# print(df3)
# 기술통계: describe()
# print(df3.describe())
# print(df3.info())

# 그룹화 하기
df3.groupby("Outcome").mean()
# 글루코사민의 평균값으로 그룹화 하기
# print(df3.groupby("Outcome").mean().agg({"Glucose": "mean"}))
# print(df3.groupby("Outcome").mean().agg({"Glucose": "mean", "BMI":"median", "Age":"sum"}))
# 속성이름 다 써줄필요 없이 열에 넣고 싶은 값만 넣기
# print(df3.groupby("Outcome").agg("mean", "median"))


# 데이터프레임 2개로 나누기
# 포지티브 값만 넣기 loc[] 판다스의 데이터 선택 및 인덱싱 함수
positive = df3.loc[df3["Outcome"] == 1]
negatice = df3.loc[df3["Outcome"] == 0]
# 결과값 (264, 4) (488, 4)
# print(positive.shape, negatice.shape)
# 결과값 수동으로 저장하기, id값(인덱스) 삭제

df3.to_csv("clean_diavetes.csv", index=False)
