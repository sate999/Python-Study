# 1~45번까지 숫자를 중복없이 6개를 뽑아야합니다.
# 6개를뽑고 +1개를 더뽑습니다.
# 처음 뽑은 6개가 일치하면 1등
# 처음 뽑은 6개중 5개가 일치하고 +1개가 일치하면 2등
# 1등과 2등만 계산하겠습니다. 3등 이하는 기분나쁘니까 ㅋ
# 기능 1. 
# 프로그램은 무작위로 6개 + 1개의 숫자를 뽑아 줄 수 있다.
# 뽑은 당첨번호는 프로그램 종료 시까지 혹은, 새롭게 뽑기 전까지 유지
# 기능 2. 
# 프로그램은 사용자가 6개의 숫자를 넣게 되면, 아까 뽑은 당첨번호를 뽑아서 1등인지 2등인지 맞춰줌
# 기능 3.
# 새롭게 당첨번호 6개 + 1개를 뽑을 수 있다.

import random

class Lotto:
    # 생성자
    def __init__(self):
        self.win = set()
        self.bonus = set()
        self.myNum = set()

    # 로또 초기화 함수
    def init(self):
        self.win.clear()    # set 초기화
        self.bonus.clear()
        while len(self.win) < 6:
            self.win.add(random.randrange(1,46))       # 1~45 사이의 숫자를 중복 없이 입력.
            # 집합 자료형이므로 알아서 중복 제외.
        
        while True:
            n = random.randrange(1,46)
            if not(n in self.win):      #이미 뽑은 6개의 당첨번호와 다른 +1 번호를 받아야함.
                self.bonus.add(n)
                break
    # 로또 번호를 입력 받는 함수
    def insert(self):
        self.myNum.clear()
        while len(self.myNum) < 6:
            print(str([len(self.myNum)+1])+"번째 숫자를 입력하세요. (1~45) : ",end="")
            n = int (input())   # 입력받음.
            if(n<=0) or (n>=46)or(n in self.myNum):     # 1~45를 벗어나거나 중복된것 제외
                print("=> 중복된 번호를 넣었거나 잘못된 번호를 넣었습니다. 다시 입력해주세요.")
                continue
            self.myNum.add(n)   # 입력넣기
            print("현재까지 번호 : "+str(list(self.myNum)))

    # 로또 번호 매칭해보는 함수
    def match(self):
        if len(self.myNum) != 6:
            print("=> 2번을 눌러서, 내 번호를 입력해주세요.")
            return
        
        self.print()
        self.printMyNum()
        matchingNum = len(self.win.intersection(self.myNum))
        if matchingNum == 6:
            print("=> [1등] 6개가 다 맞았습니다!!!")
            print("=> 세금 떼고 10억 입니다.")
        elif matchingNum == 5 and self.myNum.intersection(self.bonus):
            print("=> [2등] 5개 + Bonus 가 맞았습니다!!!")
            print("=> 세금 떼고 6천만원 입니다.")
        else:
            print("=> 꽝입니다. 적금이나 하세요~!")
    
    # 내가 입력한 번호 출력
    def printMyNum(self):
        print("내 번호 : ", end="")
        tmp = list(self.myNum)
        tmp.sort()
        print(tmp)

    # 로또 번호 출력 함수
    def print(self):
        print("이번주 번호 : ", end="")
        arr = list(self.win)
        arr.sort()

        print(arr, end="")
        print(" +", list(self.bonus))

print("=> 로또 프로그램을 실행합니다...")
lotto = Lotto()
lotto.init()
while True:
    print("=======================================")
    print("1. 이번주 로또 번호를 봅니다.")
    print("2. 내 로또 번호를 입력합니다.")
    print("3. 새로운 로또 번호를 받습니다.")
    print("4. 이번주 번호와 내 로또번호를 확인합니다.")
    print("5. 프로그램을 종료합니다.")
    print("by.SATE999 ============================")
    num = int(input())
    if num == 1:
        print("이번주 로또 번호를 봅니다...")
        lotto.print()
    elif num == 2:
        print("로또 번호 6자리를 입력해주세요...")
        lotto.insert()
        lotto.printMyNum()
    elif num == 3:
        print("새로운로또 번호를 받습니다...")
        lotto.init()
        lotto.print()
    elif num == 4:
        print("과연 몇등일까요...?")
        lotto.match()
    elif num == 5:
        print("프로그램을 종료합니다...")
        break
    
    print()