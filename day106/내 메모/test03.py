# 모듈 module == 라이브러리,클래스 랑 비슷한 역할 
# .py 파이썬 파일 # 모듈이란 파이썬 파일을 말한다.
# 누군가 기능을 바로 사용할 수 있게 미리 구현해둔 파일 == 약간 라이브러리랑 비슷느낌 

# 자바는 객체 지향언어 이다 보니 math 라는 클래스에 원주율이 들어가 있는데
# 파이썬은 모듈단위의 스크립터 이다보니 math 라는 모듈에 들어가있다.

##import 모듈명

# 별도의 추가 없이 바로 사용할 수 있는 모듈 == 표준 모듈
# 파이썬에 기본적으로 존재하는 모듈
# 별도의 설치가 필요없음

##<-> 반대가 외부모듈(패키지, package, 설치필요)
import math
##모듈명.함수명()
print(math.pi)
print(math.pow(2,10))

##from 모듈명 import 함수명 #어떤 모듈에 정확히 들어있는 함수하나 가져올래 
from random import randrange #random이라는 모듈안에 randrange
##from random import * # 드물지만 존재는 한다.
# 위에는 모듈명.함수를 사용하였는데 
print(randrange(10))#0~9 #선언하고 나면 바로 함수를 사용할 수 있다.
print(randrange(1,10)) #1~9
print(choice([10,11,13,15,23]))

#별칭(alias) as
#import 모듈명 as 별칭(alias)
import random as r
r.randrange(10)
from random import randrange as rr
rr(1,10)

