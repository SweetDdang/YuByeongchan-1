import random

num=0

def brGame(player1, player2):
    while True:
        try:
            if player1 =="computer":
                a = random.randint(1,3)
            else:
                a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))    
                
            if 0 < a <4:
                    break
            else:
                print("1,2,3 중 하나를 입력하세요")
        
        except:
            print("정수를 입력하세요")

    for i in range(a):
        global num
        num+=1
        print(player1+" : "+str(num))

        if num == 31:
            print(player2+" win!")
            exit()
    

while num<32:
    brGame("computer","player")
    brGame("player","computer")
