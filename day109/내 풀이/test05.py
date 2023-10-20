# 예외 처리
# 모든 프로그램은 비정상 종료가 되면 안된다.

##Traceback (most recent call last):
##  File "<pyshell#1>", line 1, in <module>
##    2/0
##ZeroDivisionError: division by zero

# line 1 어디에서 예외가 발생했는지
# zero ~ 어떤 에러가 났는지
# division by zero
# 3가지

##try:
##    예외가 발생할 수도 있는 코드
##except:
##    예외발생시 수행할 코드 

##try:
##    num=int(input('정수입력: '))
##    print('입력한 정수는 %d입니다.' % (num,10/num))
##except:
##    print('정수만 입력 !!') # 모든 예외에 대해 이렇게 나온다
##
###우리는 정수 입력하래서 0 입력했는데 정수 입력 !! 이라는 에러가 또 나온다 .
###이걸 막기 위해 에러에 해당하는 문법을 따로 적어준다.
##
##try:
##    num=int(input('정수입력: '))
##    print('입력한 정수는 %d입니다.' % (num,10/num))
##except ValueError:
##    print('정수만 입력 !!')
##except ZeroDivisionError:
##    print('0으로는 나누기를 진행 할 수 없습니다.')
##except Exception:
##    print('처리하지 못하는 에러입니다....')
##finally:
##    print('프로그램을 종료합니다.') # 항상 수행되는 문장을 finally 에 넣을수 있다

'''
# 문제
test.txt에 정수 1개 입력된 상황
읽어들일 파일의 이름을 입력>> apple
test.txt를 읽어들였습니다.
apple.txt는 없는 파일입니다!

1~100>> 50
DOWN!
1~49>> 25
UP!
26~49>> 32
32! 정답입니다! :D
test.txt
 3번만에 정답을 맞추셨습니다! :D

1~100>> 500
1~100이 아닙니다. 다시 입력해주세요!
(카운트에 포함되지않음)
'''

cnt = 0  # 카운트 횟수
L = 1
H = 100

try:
    fileName = input('읽어들일 파일의 이름을 입력>> ')

    with open(f'{fileName}.txt', 'rt') as file:
        fileNumber = int(file.read())

    while True:
        try:
           
            inputNumber = int(input('%d~%d까지 중 입력해주세요: ' % (L,H)))
            cnt += 1

            if (inputNumber < L) or (inputNumber > H):
                print('%d~%d이 아닙니다. 다시 입력해주세요!'% (L,H))
                continue

            if inputNumber > fileNumber:
                print('DOWN!')
                H = inputNumber 
                continue
            elif inputNumber < fileNumber:
                print('UP!')
                L = inputNumber 
                continue
            elif inputNumber == fileNumber:
                print(f'{fileNumber}! 정답입니다!')
                break

        except ValueError:
            print('정수만 입력해주세요')

    with open('test.txt', 'a') as file:
        file.write('\n' + f'{cnt}번만에 정답을 맞추셨습니다! :D')
        print('파일 입력 완료!')

except FileNotFoundError:
    print(f'{fileName}.txt는 없는 파일입니다.')
finally:
    print('프로그램을 종료합니다.')


else: # 예외가 아니라면 ~ 진행해주세요 ~ 라고 쓸 수 있다.
    # 안에 썼으면 없는파일 입니다가 밑으로 계속 내려가서
    #가독성이 안좋아지기 때문에 else를 써야 가독성이 좋아짐 

    

