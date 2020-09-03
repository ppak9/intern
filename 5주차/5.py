# 2,3,4,5 는 하나로(조건문에 대한 이해)
players =['마이클 조던','하승진','전태풍','손흥민','김연아']

check = input('선수 이름을 쓰시오')

if check in players:
    print("대표 선수가 맞습니다.")
else:
    print("잘못 입력하셨군요")