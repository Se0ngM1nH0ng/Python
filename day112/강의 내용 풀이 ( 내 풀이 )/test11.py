# 데이터 시각화
'''
데이터 시각화에 가장 많이 사용되는 라이브러리
matplotlib 라이브러리
외부모듈이라서 별도의 설치를 하고 사용 해야 한다.

이 라이브러리 안에
    pyplot 모듈이라고 있는데 가장 많이 사용

외부모듈을 설치 == pip
cmd 에서 함

cmd >> pip install matplotlib
pip NOT FOUND == PATH 설정

'''

import matplotlib.pyplot as plt # plt로 별칭을 부르는게 일반적임

aList=[10,20,30,40]
bList=[20,40,10,30]

## 방법 1 plt.plot(aList,bList) #리스트를 그래프화 시키고
plt.title('only ENGLISH') # 캡션 추가하기
plt.plot(aList, color='hotpink', label='aList')
plt.plot(bList, ls='--' label='bList') #ls = lineStyle 그래프 선 모양 변경하기 ':','--'
plt.legend() #label, 범례 추가하기 
##plt.plot(bList) 
plt.show() # 그것을 보여줄래 ? 라는뜻

