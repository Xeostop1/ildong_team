import numpy as np
import pandas as pd

#데이터 프레임을 apply사용 
#특정 행이나 열의 계산을 가능함 
a = pd.DataFrame({'국어': [51,65,78], \
                  '수학': [80,90,100]}, \
                  index=['Kim','Lee','Choi'])
print(a)
#sqrt 제곱근 루트를 씌우는 방법 
b = a.apply(np.sqrt)
print(b)
