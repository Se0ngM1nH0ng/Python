#C:\Users\08aaa\AppData\Local\Programs\Python\Python312
#D:\HONG2\python

#파일 입출력
##파일 객체 = open('파일명.확장자','모드')
##file=open('test.txt','wt')
### 'wt' write text 절대경로와 상대경로를 지원한다. 내가 아예 지정하고 싶으면 앞에 c: 를 붙이면 됨
##wt 파일 쓰기 모드 ## 덮어쓰기 됨 
##rt 파일 읽기 모드
##at 파일 이어쓰기 모드
##file.close()
#열었던 파일을 닫는거라서 메서드를 사용 열었으면 닫아야함
#없는 파일을 요청하게 되면 하나 txt 를 만들어줌

#파이썬에서는 파일을 열면 닫는게 세트인데 합치는게 좋지 않을까 ?

##with 문
##with open('파일명','모드') as 파일객체:
##    파이썬에서 많이 사용되는 문법 , 자동으로 다끝나면 닫아줌

##with open('test.txt','at') as file:
##    file.write('줄\n 바꿈')

##with open('test.txt','at') as file:
##    while True: #언제 멈출지는 사용자 마음 
##        tmp=input('입력: ')
##        if not tmp: # 입력할 수 없을 때 멈출거다 
##            break
##        file.write(tmp)
##        file.write('\n') # 파일write 자동 줄바꿈을 지원하지 않기 때문에 입력


##aList=['사과',12000,'바나나',3900,'키위',5400]
##aList.txt를 생성해주세요.
##사과는(은) 12000원입니다.

##with open('aList.txt','wt') as file:
##    aList=['사과',12000,'바나나',3900,'키위',5400]
##    for i in range(0,len(aList),2):
##        file.write(f"{aList[i]} 는(은) {aList[i + 1]} 원입니다.\n")
##        #file.write("%s는(은) %d원입니다.\n" % (aList[i], aList[i + 1]))



####bList.txt 파일이 있습니다.
####[홍길동][남]
####[아리][여]
####[쉔][남]
####[모르가나][여]
####.
####.
####.
##
##print('이름과 성별을 입력하세요 !')
##print('더이상 입력하지 않으려면 빈칸으로 남겨주세요')
##with open('bList.txt','wt') as file:
##    while True:
##        tmp1=input('이름입력: ')
##        tmp2=input('성별입력: ')
##        if not tmp1 and not tmp2:
##            break
##        file.write('[ %s ] [ %s ]\n' % (tmp1,tmp2))

print('문제 2번')
with open('bList.txt','rt') as file: # bList 를 일단 읽어옴
        content = file.read()
        print(content)
cnt1 = 0  # 남자일때
cnt2 = 0  # 여자일때

lines = content.split('\n')

for line in lines:
    if '남' in line:
        cnt1 += 1
    elif '여' in line:
        cnt2 += 1

print('\n')
print('남자는 %d 명, 여자는 %d 명 입니다.' % (cnt1,cnt2))
##파이썬 쉘 화면에서
##남자는 ㅁ명, 여자는 ㅁ명입니다.
    


