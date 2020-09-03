## [입문자를 위한 web-crawling]

[참조 강의](https://book.coalastudy.com/data_crawling/) 
-----
```
참조 강의와 같이 할 수 없습니다. 따라서 가장 주차마다
핵심요소를 간추리고 이에 맞게 예시를 찾아보고 변형합니다.

핵심요소를 통해서 이와 잘 부합하는 강의로 다시 재구성합니다.
실습의 경우 유사하기 때문에, 각각마다 가장 유사한 것을 찾아
이와 비슷한 예시를 주차마다 목표로 삼습니다.
재구성 이후 찾은 자료들과 비교해 커리를 다시 새로 내 놓습니다.
```

[참조자료](https://media.fastcampus.co.kr/insight/why-beginners-should-master-them/)

1.
```
모든것은 구름 내 IDE 사용한다는 가정입니다.
```
2.
```
가안 설계 이후, 초보자들도 스스로 납득 가능한지를 봐야 합니다.
iteration 반복 및 user_test 거쳐보기
```
```
커리큘럼 준비 시 깨달은 점
1. 다음 기능을 설명할 경우, 해당 기능이 어떤 상황에서 쓰이는 지 예시를 정확히 들어야 함
2. 반복적인 작업을 줄이기 위해서 컴퓨터를 사용한다고 얘기해야함
3. 현재 진행 정도가 어느 정도이며, 전체 커리큘럼에서 어느 단계에 있음을 인지시키는 것
4. 중요한 개념의 경우, 반복적으로 얘기하고 쉽게 전달할 수 있어야 함
```
## 강좌 커리큘럼

### 1주차

-----

* 1주차: HTML 그게 뭐지?!
  
  * [크롤링 전, 우리가 알아야 할 것은? HTML]
    * HTML을 왜 알아야 하는지, 그 이유에 대해서 설명합니다.
    * 크롤링이란 웹에서 존재하는 데이터를 가져와야 하기 때문에, 따라서 웹 페이지에 대한 이해가 충분 해야함을 어필합니다. 
  > 예상 강의 시간: 2~3 분
  * [자기소개 웹 페이지 만들기!]
    * 기본 개념 설명(기본 태그 + img, textarea.. )
    * 실제 크롤링에 필요한 태그들을 찾아 옵니다. 즉, 사이트를 구성하는데 있어서 몇 가지 필요한 태그들을 소개합니다. textarea,H 태그 등 기본이 되는 개념들을 핵심만 간략히 소개합니다.
  > 예상 강의 시간: 7분~10분

  * [과제 1: 자기 소개 웹 페이지 만들기]
    * 이후 자기소개 웹 페이지를 활용해 태그 찾는 설명들을 찾아봅니다.
  
  * [실제 사이트 태그 찾기]

    * 먼저 지난 번 과제를 활용합니다.
    * 지난 번 과제에서 태그를 찾는 방법을 소개합니다.
      * chrome 을 통한 검사 방식+ F12
    * [실습예제: 쇼핑몰 태그 찾기]
      * 간단한 쇼핑몰을 구현해 놓아, 배포한 후 실제 어떻게 태그로 이루어졌는지 찾아봅니다.
      * 추가적으로 원하는 정보를 구분 못하는 경우 id,class를 설명합니다
    * [실습예제 2: 네이버 연예 동영상이나 카카오 TV를 통해 태그 찾아보기]
      * 카카오 TV나 다른 서비스들의 소스코드를 분석해 어떤 태그가 속해있는지 확인합니다.
    
    > 예상 강의 시간: 5~7분
    
    * [실습 예제 3: 실습 예제 이후 순위나 업로드 한 사람들을 태그를 통해 찾아봅니다.]

---
### 2주차

*[계산기 만들기(feat.파이썬)]
    * 실습 환경 구축(이미 구축)
  * 계산기 만들기
    * 계산기 만들기 위해 화면에 보여질 것과 동시에 입력 가능한 칸이 존재해야함을 보여야 함
    * print, input 설명
    * print 와 input이 제대로 되기 위해서는 자료형이 맞아야 함을 설명
    * 상황 예시(우리 계산기 만들어야 한다.)
    * 매번 칠 수 없으니 변수 저장을 통해서 한다고 지난번에 언급한 것을 가지고 옴
    * 논리 연산에 대한 설명(main point:논리 연산은 기능 결국 자료형이 맞아야 하며, 이를 변수로서 연산 가능해야 함을 쉽게 설명)
    * 기능보다 자료 형태에 대한 설명(feat. 수학에 대한 기본 원리 강조)
* [친구들 불러보기(feat.파이썬)]
  * 강좌 목표 , index와 value에 대한 주제 강조
  * 그 이후 상황에 따른 기능 이해
  * 문자열에 대한 이해
  * replace,slicing, strip
  * in range -> index에 따른 value 이해 시키기
* [실습 과제: 내 친구들 youtube 관리해주기]
  * 조회수 데이터를 가지고 와서, 실제 조회수 처리해보기
  * 예시자료는 강의자료에
>예상 강의 시간 : 10분 
