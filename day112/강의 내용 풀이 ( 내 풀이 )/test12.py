import matplotlib.pyplot as plt # plt로 별칭을 부르는게 일반적임
import csv

maxTempList=[] # 최고 기온 데이터들만 저장
minTempList=[] # 최저 기온 데이터 들만 저장 

with open('a.csv','r') as file: #헤더 만들어 주기 
    data=csv.reader(file)
    header=next(data)
    print(header)

    month = input('월 입력 >> ')
    day = input('일 입력 >> ')

    for row in data:
        if row[-1]=='':
            continue
##        if 내가 보는 데이터(row[0])가 8월 데이터라면: # 최고기온을 볼때 8월이 가장 덥기 때문에
        if row[0].split('-')[1] == month and row[0].split('-')[2] == day:
            maxTempList.append(float(row[-1])) #최고기온 데이터들 추가 한다.
            minTempList.append(float(row[-2])) #최저기온 데이터들 추가 한다. 
            
print('최고기온 데이터 개수 : %d' % len(maxTempList))
print('최저기온 데이터 개수 : %d' % len(minTempList))
print('%s월 %s일의 그래프' % (month,day))

##plt.title('only ENGLISH') # 캡션 추가하기
plt.title('maxTemp/minTemp')
##plt.plot(aList, color='hotpink', label='aList')
plt.plot(maxTempList, color='red', label='maxTemp')
plt.plot(minTempList, color='blue', label='minTemp')
##plt.plot(bList, ls='--' label='bList') #ls = lineStyle 그래프 선 모양 변경하기 ':','--'
plt.legend() #label, 범례 추가하기 
#plt.plot(bList) 
plt.show() # 그것을 보여줄래 ? 라는뜻


## 문제
##월 입력 >> 12
##일 입력 >> 11
##a.csv에 존재하는
##12월 11일 최고 기온 데이터들과
##최저 기온 데이터들을 한번에 show() 해주세요 !
##단 , 범례를 maxTemp/minTemp로 해주시고
##    빨간색/파란색 그래프로 표기 해주세요!


    

 
