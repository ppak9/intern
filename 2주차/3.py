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