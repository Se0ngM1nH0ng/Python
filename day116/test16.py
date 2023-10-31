import numpy as np

##배열 = np.array(리스트)
##자바에서는 배열 자리와 리스트가 같았지만
##파이썬은 리스트는 연산이 불가능하다고 판단함

#1. 파이썬에서는 리스트 != 배열
#2. 계산(연산)을 할때에는 배열 > 리스트

'''
a = np.array([[2,3,4], [5,1,7]])
print(a)

#1번 학생의 국어 ==2점, 영어 ==3점 , 수학==4점
#2번 학생의 국어 ==5점, 영어 ==1점, 수학== 7점
print(a[0][1]) #1번학생의 영어 점수볼래

a.shape # 2명의 학생의 3개의 과목을 치뤘다. 
a.dtype # 바이트를 볼 수 있다. #배열 내부에 저장된 데이터의 타입을 출력 
a.astype('float64') #모든 타입을 실수 로 보고 싶어요 # 배열에 저장된 데이터의 타입을 변환
np.sum(a) #안에 있는 수를 다 더하는 메서드

np.zeros((2,3)) # 0 으로 해줄래 ?
np.ones((2,3)) # 1 로 해줄래

np.arange(1,5) # 5는 포함 안됨

a=np.arange(2,6)
b=np.arange(1,5)

행렬을 맞춰야지만 계산 하는 것인데

행렬을 안맞추고 계산 하는 작업을 # 브로드 캐스팅 이라고 한다.


a+b a*b # 배열끼리 연산시  행,열을 맞춰주는 것을 권장(브로드 캐스팅)

학생이 3 명 있다는 사실을 알고 있어서 for문
for i in range(3):
    국어x2
    영어x2
    수학x2
    studentList.append(학생1)

for i in range(3):
    for j in range(2):
    국어 점수를 입력받을 거다
    입력받으면 각각의 리스트에 점수 추가 
    for j in range(2):
    영어
    for j in range(2):
    수학
    
    student=np.array( [kList, eList, mList ] ) # 3행 2열 
    studentList.append(학생1)

학생 1명이 각각의 과목을 세번 중간 기말 총 6번 
'''

import random

total=0
studentList=[]

for i in range(3):
    kList=[]
    
    for j in range(2): ## 이게 과목
        scorea=random.randint(0,100)
        kList.append(scorea)
        if j==0:
            print('%d번 학생의 중간고사 국어 점수는 %d점 입니다.' %(i+1,scorea))
        elif j==1:
            print('%d번 학생의 기말고사 국어 점수는 %d점 입니다.' %(i+1,scorea))
        total = sum(kList)

    eList=[]
    for j in range(2): ##
        scorea=random.randint(0,100)
        eList.append(scorea)
        if j==0:
            print('%d번 학생의 중간고사 영어 점수는 %d점 입니다.' %(i+1,scorea))
        elif j==1:
            print('%d번 학생의 기말고사 영어 점수는 %d점 입니다.' %(i+1,scorea))

    mList=[]
    for j in range(2):
        scorea=random.randint(0,100)
        mList.append(scorea)
        if j==0:
            print('%d번 학생의 중간고사 수학 점수는 %d점 입니다.' %(i+1,scorea))
        elif j==1:
            print('%d번 학생의 기말고사 수학 점수는 %d점 입니다.' %(i+1,scorea))

    print()
    student=np.array( [kList,eList,mList] )
    studentList.append(student)
    
print(studentList)


##j 가 2 가 없어서 인덱스 오류
##j 과목이 아니라 중간인지 기말인지 였다
##j 0,1 나눠서 0이라면 중간 1이라면 기말 

print()
print()
print()

### 과제2
##### 모든 학생들의 중간·기말고사 국어 평균 점수는 42.67점 입니다.
##### 국어/영어/수학 중에서 입력>> ㅁㄴㅇㄹ
##### 제대로 입력해주세요!
##### 국어/영어/수학 중에서 입력>> 수학
##### 수학 시험 1등은 1번 학생 입니다.

average_korean = float(total / 6)
print(f'모든 학생들의 중간·기말고사 국어 평균 점수는 {average_korean:.2f}점 입니다.')

while True:
    subject = input('국어/영어/수학 중에서 입력>> ')

