# 파일 읽어와야 해 import
##파일 먼저 읽어와
##데이터를 만들거다
##헤더가 있어야 한다.
##헤더가 무엇인지 한번 출력
##헤더가 무엇인지 앎 으로서 내가 뭘 조사 하고 싶은지 찾을 수 있다.
##최고기온 값을 저장할 리스트와 최저기온을 저장할 리스트를 만들자
##maxTempList=[] #8월 데이터
##minTempList=[] #1월 데이터
##
##데이터를 꺼내서 읽어보기
##데이터가 없으면 안되므로 continue
##
##생략이 안되고 넘어온 데이터 중
##만약에 8월 데이터라면
##최고 기온에 append
##1월 데이터라면
##최저 기온에 append

# 문제
# a.csv에 기온 데이터가 저장되어있습니다.
# 최저 기온의 분포도와 최고 기온의 분포도를 출력해주세요!~~

import csv
import matplotlib.pyplot as plt

maxTempList=[] # 8월 데이터
minTempList=[] # 1월 데이터

with open('a.csv','r') as file:
    data=csv.reader(file)
    header=next(data)
##print(header)
# 최고 기온 [-1]   최저 기온 [-2]

    for row in data:
        if row[-1]=='' or row[-2]=='':
            continue
        month=row[0].split('-')[1]
        if month=='08':
            maxTempList.append(float(row[-1]))
        elif month=='01':
            minTempList.append(float(row[-2]))

plt.hist(maxTempList,color='red',label='08')
plt.hist(minTempList,color='blue',label='01')
plt.legend()
plt.show()


        
