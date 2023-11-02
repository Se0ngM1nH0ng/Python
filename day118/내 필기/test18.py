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
##choice에 p 속성에 확률을 분산해놓을수 있다. 
plt.hist(dice,bins=6)
plt.show()

##세 번째 매개변수 p는 선택된 요소의 확률 배열을 나타냅니다. 
##이 배열의 길이는 선택 대상 배열의 길이와 일치해야 합니다. 각 요소의 인덱스에 해당하는 확률이 지정됩니다. 
##예를 들면, 0부터 5까지의 숫자 중 5가 가장 높은 확률로 선택되며 (0.5의 확률), 
##나머지 숫자는 각각 0.1의 확률로 선택됩니다.

##따라서 이 코드는 0부터 5까지의 숫자 중 5가 가장 높은 확률로 선택되며, 
##나머지 숫자는 각각 0.1의 확률로 선택되어 총 10만번의 선택을 수행하게 됩니다.
