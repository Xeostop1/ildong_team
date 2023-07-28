import numpy as np
import pandas as pd

a = pd.DataFrame({'국어': [51,65,78], \
                  '수학': [80,90,100]}, \
                  index=['Kim','Lee','Choi'])
print(a)
#행은 사라지고 열단위로 집계 0

b = a.apply(np.average, axis=0)
print(b)
#열은 없어지고 행단위로 집계 그래서 1을 사용했구나 
print("*"*30)
c = a.apply(np.average, axis=1)
print(c)
