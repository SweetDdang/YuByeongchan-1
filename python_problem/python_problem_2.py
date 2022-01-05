##############  Variables

student_data = {}


##############  menu 1
def Menu1(name,mid_score,final_score) :
    #사전에 학생 정보 저장하는 코딩 
    global student_data
    student_data[name]=[mid_score,final_score]

##############  menu 2
def Menu2() :
    #사전에 학생 정보 저장하는 코딩 
    global student_data
    student_names = list(student_data.keys())
    for i in range(len(student_names)):
        student_scores = student_data[student_names[i]]
        if len(student_scores) == 3:
            continue
        else:
            student_scores.append(int(sum(student_scores)/2))



##############  menu 3
def Menu3() :
    #출력 코딩
    global student_data
    student_names = list(student_data.keys())
    print('---------------------')
    print('name mid final grade')
    print('---------------------')
    for i in range(len(student_data)):
        print(student_names[i]+" "+str(student_data[student_names[i]][0]) +" "+str(student_data[student_names[i]][1])+" "+str(student_data[student_names[i]][2]))
    
##############  menu 4
def Menu4(name):
    #학생 정보 삭제하는 코딩\
    global student_data
    del(student_data[name])
    print(name + "student information is deleted.")
    

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name,mid_score,final_score = input("Enter name mid-score final-score : ").split()
            if name in student_data:
                print("Already exist name!")
            else:
                try:
                    mid_score = int(mid_score)
                    final_score = int(final_score)

                    if  (0 <= mid_score <= 100) and (0<=final_score<=100) :
                        Menu1(name,mid_score,final_score)
                    else:
                        print("Scores should be 0 to 100")                    
                except:
                    print("mid-score or final-score should be int")
        except ValueError:
            print('Num of data is not 3!')
    elif choice == "2" :
        
        if len(student_data) == 0:
            print("No student data!")
        else:
            print("Grading to all students.")
            Menu2()

    elif choice == "3" :
        
        if len(student_data) == 0:
            print("No student data!")
        else:
            if len(sum(student_data.values(),[]))%3 != 0:
                print("There is a student who didn't get grade.")
            else:
                Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        isname = input("Enter the name to delete : ")

        if isname in list(student_data.keys()):
            Menu4(isname)
        else:
            print("Not exist name!")


    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break
    else :
        print("Wrong number. Choose again.")