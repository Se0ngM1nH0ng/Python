# 막대 그래프
# 히스토그램
# 자료의 분포 상태를 막대그래프로 표기한 것

# 분포나 빈도 이런것들을 측정

import matplotlib.pyplot as plt
import random

##aList=[1,2,3,3,5]
##plt.hist(aList) #메서드 명 
##plt.show()

# 주사위는 과연 공정할까 ?
##어떤 행동을 하는걸 == 시행
##주사위를 굴리는 행위 == 시행
dice=[] #주사위를 굴리는 행위(==시행)의 결과를 저장할 리스트 # 자바에선 배열

##print(dice)
#bins 가로축 구간 설정 속성
for i in range(10000):
    dice.append( random.randint(1,6) ) # 1~6
##print(dice)
plt.hist(dice,bins=6) # 가로축 구간 설정 속성
plt.show()
