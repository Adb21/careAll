# ```
# Constraints :
#     1. 4 elders per young
#     2. Ratings and reviews for both
#     3. Elder's approval for young, i,e request service
#     4. Profile Making
#     5. Money Deposited after service and tip
# testing Constraints :
#     1. Showing who is taken care of older couple
    # 2. Showing all a young chap is currently taken care of.
# ```
class Person:
    
    def __init__(self,pid,name,age,uid,pas):
        self.profile_id = pid
        self.name = name
        self.age = age
        self.rating = []
        self.uid = uid
        self.pas = pas
        self.request = []
        self.accepted = []
        self.review = []
        self.past_takers = []
        self.present_taker = []
        self.count = 0
        self.flag = 0
        

class System:
    Elder_list = []
    Young_list = []
    elder_cnt = 0
    yng_cnt = 0
        
    def addElder(self,cls):
        for i in cls:
            self.Elder_list.append(i)
    
    def addYoung(self,cls):
        for i in cls:
            self.Young_list.append(i)
        
    def show(self,f):
        if f == 0:
            for i in self.Young_list:
                print("the details are :\n{}\n{}\n{}\n{}\n".format(i.profile_id,i.name,i.age,i.rating))
        else:
            for i in self.Elder_list:
                print("the details are :\n{}\n{}\n{}\n{}\n".format(i.profile_id,i.name,i.age,i.rating))


def info():
    pid = int(input("Enter PID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    uid = input("Enter UserID: ")
    pas = input("enter password: ")
    return [pid,name,age,uid,pas]

def Intro():
    org = System()
    print("----------------Welcome to CareAll----------------\n Retired folks make themselves available for care &young can earn by taking care\n\n")

    print("Services are \n1. add Elder\n2. add young Taker\n3. Login for services\n4. Show who are taken care of older couple\n5. Showing all a young chap is currently taking care of\n6. Exit\n Enter your choice:-")
    opt = int(input())
    if opt == 1:
        pid,name,age,uid,pas = info()
        e1 = [Person(pid,name,age,uid,pas)]
        org.addElder(e1)
        print("Entry Added")
        org.show(1)

    elif opt == 2:
        pid,name,age,uid,pas = info()
        e1 = [Person(pid,name,age,uid,pas)]
        org.addYoung(e1)
        print("Entry Added")
        org.show(0)
 
    elif opt == 3:
        ch = int(input("Login as 1) Elder 2) Young :"))
        uid = input("Enter UID: ")
        pas = input("Enter Password: ")
        if ch == 1:
            for i in org.Elder_list:
                if i.uid == uid and i.pas == pas:
                    print("...LOGIN SUCCESS...\nWelcome {}".format(i.name))
                    ser = int(input("Services:\n1. Accept for caretaking\n2. Give rating and review\n3. View all ratings and reviews\n4. Show History: "))
                    if ser == 1:
                        print("select for Young Takers:\n")
                        for j in i.request:
                            print("the details are :\n{}\n{}\n{}\n{}\n".format(j.profile_id,j.name,j.age,j.rating))
                        sel = int(input("Enter Young Taker PID: "))
                        for j in i.request:
                            if j.profile_id == sel and i.flag==0:
                                i.present_taker = [j]
                                i.past_takers.append(j)
                                i.flag==1
                            else:
                                print("You cannot select at this time")
                                
                    elif ser == 2:
                        print("select for Elders:\n")
                        org.show(0)
                        sel = int(input("Enter Young Taker PID: "))
                        for j in org.Young_list:
                            if j.profile_id == sel and j in i.past_takers:
                                rating = int(input("Enter Rating out of 5: "))
                                review = input("Enter your Review:\n")
                                j.review.append(review)
                                j.rating.append(rating)
                                
                    elif ser == 3:
                        print("The ratings are: \n{}\n".format(i.rating))
                        print("The Reviews are: \n{}\n".format(i.review))
                    
                    elif ser == 4:
                        for j in i.present_taker:
                            print("The current care taker details are: \n{}\n{}\n{}\n{}\n".format(j.profile_id,j.name,j.age,j.rating))
                        print("The Past care taker details are: \n")
                        for j in i.past_takers:
                            print("\n{}\n{}\n{}\n{}\n".format(j.profile_id,j.name,j.age,j.rating))
                else:
                    print("No Records Found")
        elif ch == 2:
            for i in org.Young_list:
                if i.uid == uid and i.pas == pas:
                    print("...LOGIN SUCCESS...\nWelcome {}".format(i.name))
                    ser = int(input("Services:\n1. Request for caretaking\n2. Give rating and review\n3. View all ratings and reviews\n4. Show History: "))
                    if ser == 1:
                        print("select for Elders:\n")
                        org.show(1)
                        sel = int(input("Enter Elder PID for request: "))
                        for j in org.Elder_list:
                            if j.profile_id == sel and i.count<5:
                                j.request.append(i)
                                i.present_taker = [j]
                                i.past_takers.append(j)
                                i.count = i.count+1
                                print("Request made Successfully")
                    elif ser == 2:
                        print("select for Elders:\n")
                        org.show(1)
                        sel = int(input("Enter Elder PID: "))
                        for j in org.Elder_list:
                            if j.profile_id == sel and j in i.past_takers:
                                rating = int(input("Enter Rating out of 5: "))
                                review = input("Enter your Review:\n")
                                j.review.append(review)
                                j.rating.append(rating)
                    elif ser == 3:
                        print("The ratings are: \n{}\n".format(i.rating))
                        print("The Reviews are: \n{}\n".format(i.review))
                    elif ser == 4:
                        for j in i.present_taker:
                            print("The current care taker details are: \n{}\n{}\n{}\n{}\n".format(j.profile_id,j.name,j.age,j.rating))
                        print("The Past care taker details are: \n")
                        for j in i.past_takers:
                            print("\n{}\n{}\n{}\n{}\n".format(j.profile_id,j.name,j.age,j.rating))
                else:
                    print("No Records Found")
        else:
            print("incorrect option")
    elif opt == 4:
        print("select for Elders:\n")
        org.show(1)
        sel = int(input("Enter Elder PID for request: "))
        for j in org.Elder_list:
            if j.profile_id == sel:
                print("{} (elder) is taken care by {} (young) ".format(j.name,j.present_taker[0].name))
    elif opt == 5:
        for j in org.Young_list:
            print("{} (young) is taking care of {} (elder) ".format(j.name,j.present_taker[0].name))
    elif opt == 6:
        return 0
    else:
        print("invalid options")
        return -1

opt = -1   
while(True):
    if opt == 0 or opt == 2:
        break
    else:
        opt = Intro()


