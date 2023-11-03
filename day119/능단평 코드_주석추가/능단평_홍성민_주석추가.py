import csv
import matplotlib.pyplot as plt
import numpy as np

while True: # 오답 시 다시 입력해야 하므로 while 
    with open('korea.csv','r') as file: # 해당자료를 읽어와 비교 해야 하므로 while안에 있어야 한다.
        data=csv.reader(file) # 한 행씩 데이터를 읽는다.
        header=next(data) # 헤더 부분
        
        print() 

    
    
    
        area=input('동 이름 입력>> ') # 사용자에게 입력을 받는다.  
        city=[] # 검색내용을 담을 배열 생성 
        
        for row in data: # 데이터의 행 중에서 
            if area in row[0]: # row[0] : 행정구역 중에서 입력받은 값이 있는지
                city.append(row[0]) # 해당하는 입력 값을 city 저장
                sample=np.array(row[3:], dtype=int) # 해당하는 값의 인구수를 모두 저장
                print(row[0]) # 검색조건으로 나온 데이터 출력 
                
        if not city: # 해당 이름이 없다면
            print('해당 이름을 가진 동은 없습니다.')
        elif len(city) ==1: # 정확히 입력하여 해당 입력이 1개만 출력된다면 
            break # 정답
        else: # 검색어 데이터 값이 2개 이상이라면
            print('해당 이름을 가진 동이 여러개입니다!') 
            print('정확하게 입력해주세요!')
         
        
plt.plot(sample) # 그래프
plt.show() # 그래프 출력
