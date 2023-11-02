import csv

with open('apple.csv','r' ) as file:
    data=csv.reader(file)
    header=next(data)
    print(header)
    print()

##    i=0
    sample=[]
    area=input('출력할 동 입력 >>')
    for row in data:
##        i+=1
##        if i==5:
##            break

##        if area가 들어있다면 행정구역에 포함된 문자열이라면:
##        if area가 들어있다면 in 행정구역에 포함된:
        
        if area in row[0]:
            for v in row[3:]:# 내가 필요한 3번 인덱스 부터 보여줘 !    
##                print(row)
##                print()
                sample.append(v) # 샘플에 append 해줘 0,1 빼고 3인덱스 부터 넣을거야 

print(sample)

##, 가 있으면 int 변환이 안됨
##
##해결 방법
##1. v 를 값을 교환해준다. replace ',', ' ' 교환 해준다. 보통 이방법을 안쓴다 느려서
##2. 실무에서는 csv 데이터를 바꾼다. 일반으로 바꾸기


##sample을 만들건데 np 의 array 로 쓸거야 배열
##3번 인덱스 부터  그리고 dtype은 int 로 해줄거야
##
##
##지난주에 배우 그래프와 np를 혼합하여




