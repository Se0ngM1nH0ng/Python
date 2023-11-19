✔️ sorted() 함수

  ▪️ 정렬할 때 사용하는 함수 

​

  ▪️ reverse 옵션 (reverse 파라미터)

 해당 파라미터를 이용하면 오름차순으로 정렬할지 내림차순으로 정렬할지 정할 수 있습니다.

디폴트로는 reverse=False로 오름차순으로 정렬이 됩니다.

sorted( ~~ , reverse=True)로 입력하게 되면 내림차순으로 정렬하여 반환합니다.

​

  ▪️ key 옵션 (key 파라미터)

sorted 함수의 key 파라미터는 어떤 것을 기준으로 정렬할 것인가? 에 대한 기준입니다.

즉, key 값을 기준으로 비교를 하여 정렬을 하겠다는 것인데, 이것을 정해 줄 수 있는 파라미터입니다.

sorted( ~~ , key=뭐뭐)로 입력하게 되면 해당 키를 기준으로 정렬하여 반환합니다.

​

​

✔️ enumerate() 함수

  ▪️ 리스트의 원소에 순서값을 부여해주는 함수 <br/>    

<br/>

​✔️ sum() 함수

✔️ max() , min() 함수 <br/>
<br/>


✔️ index() 함수 

▪️ 인덱스 번호 위치를 찾아주는 함수 

▪️ 가장 최근의 것을 찾아준다. 

​

⭐ index() 함수를 이용한 해결 

▪️ index는 바로 앞에 있는 값을 찾아내기 때문에 사용할 수 없었다 

▪️ index라는 함수 자체가 어디서 부터 어디까지 보겠다 ! 이런건 되는데  무조건 앞에서 부터 본다.

​

#reverse() 내장함수를 활용하여 해결 

​