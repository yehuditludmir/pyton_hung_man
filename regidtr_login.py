from Client import add_user
from Client import all_user
from Client import check_you_in
from User import User
from Exception import inputNumInsteadOfaString
from Exception import inputCharInsteadOfaNumber
from Client import setCookie
from Client import getCookie
import json
from Client import add_user_new



def register():
    print("הרשמה")
    nt = False
    while nt == False:
        name1 = input("your name:")
        try:
            for i in name1:
                if i.isdigit():
                    raise inputNumInsteadOfaString()
            nt = True
        except inputNumInsteadOfaString as e:
            print(e)
        except:
            print("Error!!!")
    nt = False
    while nt == False:
        id1 = input("your id:")
        try:
            if id1.isnumeric() == False:
                raise inputCharInsteadOfaNumber()
            nt = True
        except inputCharInsteadOfaNumber as e:
            print(e)
        except:
            print("Error!!!")
    password1 = input("your password:")
    t = check_you_in(password1)
    rashoom = False
    while rashoom == False:
        # print(f"t = {t}")
        if t == False:
            user1 = User(name1, id1, password1)
            # print(user1.__str__())
            # x = user1.to_dict()
            # print(x)
            # jsdata = json.dumps({"use111": x})
            # add_user(jsdata)
            #x = user1.to_dict()
            #print(x)
            #jsdata = json.dumps({"use111": x})
            #add_user_new(jsdata)
            # jsdata = json.dumps({"use111": x})
            add_user(user1)
            add_user_new(user1)
            rashoom = True
        else:
            print("סיסמא תפוסה יש לבחור סיסמא אחרת")
            password1 = input("your password:")
            print(password1)
            t = check_you_in(password1)



def login():
    print("התחברות")
    nt = False
    while nt == False:
        name1 = input("your name:")
        try:
            for i in name1:
                if i.isdigit():
                    raise inputNumInsteadOfaString()
            nt = True
        except inputNumInsteadOfaString as e:
            print(e)
        except:
            print("Error!!!")
    pp = input("password R")
    t = check_you_in(pp)
    if t == True:
        # print(f"Hello to {n}")
        print(setCookie(pp))
        print(getCookie())
    else:
        print("עליך להרשם תחילה...")
        register()
        login()

# def register1():
#     print("הרשמה")
#     nt = False
#     while nt == False:
#         name1 = input("your name:")
#         try:
#             for i in name1:
#                 if i.isdigit():
#                     raise inputNumInsteadOfaString()
#             nt = True
#         except inputNumInsteadOfaString as e:
#             print(e)
#         except:
#             print("Error!!!")
#     nt = False
#     while nt == False:
#         id1 = input("your id:")
#         try:
#             if id1.isnumeric() == False:
#                 raise inputCharInsteadOfaNumber()
#             nt = True
#         except inputCharInsteadOfaNumber as e:
#             print(e)
#         except:
#             print("Error!!!")
#     password1 = input("your password:")
#     t = check_you_in(password1)
#     rashoom = False
#     while rashoom == False:
#             print(f"t = {t}")
#             user1 = User(name1, id1, password1)
#             print(user1.__str__())
#             x = user1.to_dict()
#             print(x)
#             jsdata = json.dumps({"use111": x})
#             add_user_new(jsdata)
#             # add_user(user1)
#             rashoom = True


if __name__ == "__main__":
    register()


