## 문자열을 설명해야 하는 이유
## 그 많은 파이선 문법 중에서도 파이선 문자열을 설명하는 이유
## 크롤링을 할 경우, 대부분이 문자열로 넘어오기에,

## 문자열 그리고 index에 대한 이해

string1= "park jong hyun"
print(string1[0])
print(string1[-1])

## 직접 count 하기 보다 index에 대한 개념이 중요
## 컴퓨터도 문자 형태를 이해하기 위해서는 번호를 부여하면서 기억
## 이것이 index

## 다음 기능을 설명할 경우, 그에 관한 예시 설명이 너무나도 중요
## slicing

print(string1[0:3])

print(string1[:6])

## slicing 할 경우 마지막 숫자에 따른 범위 이해가 필수
## 예시 설명을 통해 오류 발생 과정 설명
## replace 함수 설명


print(string1.replace("hyun","min"))

## strip 까지는 소개

## chaining의 경우에는 소개 식으로

## index에 따른 value 개념이 너무나도 중요 by 문자열 

##list 설명(index 와 value를 시작으로)
## 실습예시1: 친구 다 불러보기

friends =['이범기','연창모','유정한','권영권']
print(friends[0])
print(friends[1])
print(friends[2])

## nope
## 컴퓨터를 배우는 사람으로서 이렇게 처리하지 말자
## index 와 value를 살려서

## in range

## in range도 결국 index 와 그에 대한 value임을 강조해야함
## 나중 딕셔너리 이해하기도 편하게!

# # 1
# print("친구들아 모여라!")
# for i in range(5):
#     print(friends[i])

# ## 2 : len 함수
# print("친구들아 모여라!")
# for i in range(len(friends)):
#     print(friends[i])

## 3 더욱 간단한 방법
print("친구들아 모여라!")
for i in friends:
    print(i) 