## [5주차 강의]

-----
#### [5주차 강의 순서]

-----

#### 1. [1위부터 10위까지만!] -2,3.py
* 조건문에 대한 기본적인 개념을 소개합니다.
* 사례로 1~10위까지만 뽑아오고 싶을 경우 전체 경우에서 조건을 걸어야지 컴퓨터도 작동할 수 있음을 보입니다.
* 컴퓨터 역시 조건에 따라서 움직일 수 있기에 이 때 필요한 것이 **조건문** 이라 말합니다.
* 조건문에 맞는 논리 연산자를 역시 제시합니다.
* 논리 연산자에 따라 조건을 추가할 수 있음을 보이며 가장 기본인 and,or,not을 설명합니다.
  > 예상시간 : 3분 

#### 2. [확인해보자!] - 4,5.py
* 조건문을 활용해, 실제 데이터가 존재하는지 확인하는 방법을 말합니다.
* 실제 string을 모아 놓은 list을 활용해 조건문의 의의를 설명합니다.
* 4.py가 그 예시입니다.
* 추가적으로 입력 값에 따라 조건이 변화함을 조건문에 대한 조건을 추가하는 방법 + elif까지 설명합니다.
  
> 예상 시간: 5분 (실습 포함)
#### 3. [1위부터 10위까지 진짜로!] 6-1.py
* 실제 조건문을 활용해, 1위부터 10위까지의 데이터만 가지고 오게 만듭니다.
* 조건문을 추가함으로써, 전체가 아닌 부분만을 가지고 옵니다.
* 실제 페이지를 보고 여러가지 논리 연산자를 사용해 검색어를 추출합니다. 
> 예상 시간 : 3분

#### 4. 네이버 쇼핑몰 이미지 가지고 오기

* urllib library를 많이 사용합니다. (urlretrieve, urlopen,quote_plus)
* 보안 작업으로 필요한 라이브러리 ssl을 가지고 온다고 얘기해줍니다.
* 필요에 맞게 적절하게 사용하는 라이브러리임을 보여줍니다.
* 패키지가 아니기에 설치할 필요가 없음도 얘기합니다.
* 0.py에 표시한 middle 1까지는 동등하기에, 별 문제 없이 넘어갑니다.
* 이 기점으로 끝습니다. 주제가 달라지기 보다, 뒤에 부분이 공부할 것이 많기 때문입니다.

> 예상 시간 : 5분
#### 5. 네이버 쇼핑몰 이미지 가지고 오기 2 - 0.py

* 속성 내부에 있는 값을 가지고 오는 방법으로 attrs를 소개합니다.
* 상황에 맞게 넘어가야 할 때, 이 때 attrs을 말합니다.
* 실제 attrs를 통해 넘어가는 데이터가 보여짐을 **print로 통해** 보여줍니다.
* urlopen 과 requests의 차이를 간략히 설명하며, urlopen의 의미를 설명합니다.
* 모든 이미지를 다 가지고 온다는 가정이기에, find_all 함수를 보여줍니다.
* 뒤에 imgUrl 역시 attrs 을 사용하며, **img 태그**에 대한 설명을 다시 합니다.
* retreieve 규칙을 보여주며, 반복문 앞에 변수 지정 이유와 fullname 지정 이유를 설명해줍니다.
* 이미지 파일 앞에 poster를 붙이는 이유를 설명하며, 이 때 필요한 폴더 생성을 설명합니다.
  ```
  fullname = 'poster/'+ str(n) +'.jpg' : poster라는 폴더 필요
  ```

> 예상 시간 : 7분 
> 실습 자체가 복잡하기에, 오래 잡았습니다.

#### 추가 실습 : 내가 원하는 이미지 가지고 오기 - 9.edit.py

* 앞에 실습과 유사하며, url 규칙을 통해서 가지고 올 수 있음을 보여줍니다.
* 본인이 입력한 input 값이 url로 전달되어야 하기에 quote_plus 라이브러리 사용하는 것 역시 언급하며 결과를 보이고 끝냅니다.

> 예상 시간: 3분


