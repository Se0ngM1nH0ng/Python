# 데이터 분석 , 시각화
# 외부모듈  라이브러리 3대장

##연령별 인구 현황
##2023 10월 10세 0 ~100이상 남/여 구분 없이


##import matplotlib.pyplot as plt
##import random
##
##dice=[]
##for i in range(100000):
##    rand=random.randint(1,6)
##    dice.append(rand)
##plt.hist(dice,bins=6)
##plt.show()
##
##시행의 횟수가 많아지면 랜덤 값들이 고르게 잘 나온다.


import matplotlib.pyplot as plt
import numpy as np
##np 배열
dice=np.random.choice(6,100000,p=[0.1,0.1,0.1,0.1,0.1,0.5])
choice에 p 속성에 확률을 분산해놓을수 있다. 
plt.hist(dice,bins=6)
plt.show()

