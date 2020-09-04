
f = open('athletics.csv','w',encoding='UTF-8')
# open으로 파일 생성 옵션 얘기하기
player = ['조던','손흥민','윤성빈','박세리']
events = ['농구','축구','스켈레톤','골프']

for i in range(len(player)):
    f.write(player[i] + ','+ events[i] + '\n')

# comma를 넣는 이유는 csv 특성 때문이고 나머지는 f와 singer가 다 맞음
f.close()

# 복습 강조