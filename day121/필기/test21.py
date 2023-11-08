import pandas as pd

## 행중심인지 , 열중심인지 이걸 구분 잘 해줘야 한다. 

# 2차원 배열 데이터가 존재하는 상황
# dict


# 실험이 나왔을때 완성 데이터
# 2차원 배열 데이터는 어떻게 달라지냐에 따라 

# dict
data={ 'Name':['Alice','Bob','David'],
       'Score':[30,88,59],
        'City':['Chicago','New York','Los Angeles'] }
# 특정 열을 출력
# 특정 행 출력 df.loc[0]
df=pd.DataFrame(data)
print(df)
print()
print()
print()
print(df['Name']) # 특정 열을 출력
print(df.loc[0]) # 특정 행을 출력
print(df[ df['Score']>=50 ]) # 조건만족하는 데이터만 추출



#특정 데이터만 뽑아서 보고 싶을때
# 조건 만족하는 데이터만 추출 가능



#새로운 속성을 추가 할 수 있다. 나이 같은거
df['Age']=[20,22,21]
print(df)

# 이름은 뭐고 점수는 몇이고 도시는 어떻고  나이는
ndata={'Name':'Anna','Score':85,'City':'Seoul','Age':30}
# 인덱스를 재설정해서 새로운 행이 최신 행으로 추가될수있음


# 데이터를 만들었으면 추가 해주면 된다.
df=df.append(ndata,ignore_index=True)
# 인덱스를 재설정해서 새로운 행이 최신 행으로 추가 될수 있음
# _ignore_index 를 True 로 바꿔줘야 한다.

print(df)
