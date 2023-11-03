import csv
import matplotlib.pyplot as plt
import numpy as np

while True:
    with open('korea.csv','r') as file:
        data=csv.reader(file)
        header=next(data)
        
        print() 

    
    
    
        area=input('동 이름 입력>> ')
        city=[]
        
        for row in data:
            if area in row[0]:
                city.append(row[0])
                sample=np.array(row[3:], dtype=int)
                print(row[0])
                
        if not city:
            print('해당 이름을 가진 동은 없습니다.')
        elif len(city) ==1:
            break
        else:
            print('해당 이름을 가진 동이 여러개입니다!')
            print('정확하게 입력해주세요!')
         
        
plt.plot(sample)
plt.show()
