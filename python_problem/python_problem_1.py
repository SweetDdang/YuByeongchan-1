num=0
while num<32:
    while True:
        try:
            a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if 0 < a <4:
                break
            else:
                print("1,2,3 중 하나를 입력하세요")
        
        except:
            print("정수를 입력하세요")

    for i in range(a):
        num+=1
        print("playerA:"+str(num))

        if num == 31:
            
            exit()
        
    while True:
        try:
            a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if 0 < a <4:
                break
            else:
                print("1,2,3 중 하나를 입력하세요")
        
        except:
            print("정수를 입력하세요")

    for i in range(a):
        num+=1
        print("playerB:"+str(num))

        if num == 31:
            
            exit()

