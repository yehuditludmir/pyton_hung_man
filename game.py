import regidtr_login
from Client import startGame
from Exception import inputCharInsteadOfaNumber
from Exception import wrongOption
from Client import you_success
from Client import you_fail
from Client import your_history
from Client import getCookie
from Client import start__Game


def playGame():
    start = start__Game()
    print(start)
    if start == 'Not found cookie':
        print("עליך להתחבר תחילה")
        login()

    file1 = open('./logo.txt', 'r')
    for line in file1.readlines():
        print(line.strip())

    print("ועכשיו אפשר להתחיל לשחק---")

    file = open('./Haman.txt', 'r')
    # print(file.readlines())
    ha = list(map(lambda x: x.strip(), file.readlines()))
    nt = False
    while nt == False:
        x = input(print("הכנס מספר"))
        try:
            if x.isnumeric() == False:
                raise inputCharInsteadOfaNumber()
            nt = True
        except inputCharInsteadOfaNumber as e:
            print(e)
        except:
            print("Error!!!")
    x = int(x)
    word1 = startGame(x)
    # print(word1)

    lenOfWord = len(word1)
    theWord = ""
    for i in range(0, lenOfWord, 1):
        # print(word1[i])
        if word1[i] != ' ':
            theWord += "_"
        else:
            theWord += " "

    print(theWord)

    count = 0
    win = False

    i = 0
    while count < 7 and win == False:

        big = True;
        while (big == True):
            tav = input("הכנס תו")
            if (len(tav) == 1):
                big = False
            else:
                print("הזנת ערך לא תקין יש להזין שוב")
        print(tav)
        index = -1
        tafoos = True
        b = False
        twice = False
        while tafoos == True:
            # print('en1')
            # print(f"index{index}")
            v = int(word1.find(tav, index + 1, lenOfWord))
            # print(f"v{v}")
            if v != -1:
                if theWord[v] != '_':
                    index = v
                    # print(index)
                else:
                    index = v
                    theWord = theWord[:v] + tav + theWord[v + 1:]
                    print(theWord)
                    if winner(theWord) == True:
                        win = True
                b = True

            else:
                if b == False:
                    # for line in file.readlines():
                    #     if line.find('-') == -1 and line.find('|') == -1:
                    #         print(f"file.tell(){file.tell()}")
                    #         file.seek(0, 1)
                    #         # file.readline()
                    #         # file.readline()
                    #         # file.close()
                    #         break
                    #     else:
                    #         print(line.strip())

                    # # for ol in ha:
                    # #     if ol!='':
                    # #         print(ol)
                    # #
                    # #
                    # #     else:

                    c = 0
                    ha = ha[i:]
                    count = count + 1
                    # while c <= count:
                    # print(len(ha))
                    # print(f"i{i}")
                    # print(file.tell())
                    for index, value in enumerate(ha, 0):
                        if value.find('-') == -1 and value.find('|') == -1:
                            index = index + 2
                            i = index
                            break
                        else:
                            print(f"{value}")
                    # file.seek(0,0)

                    #     c = c + 1

                    print(f"כמות השגיאות{count}")
                tafoos = False
            # break
        print(f"count{count}")

    if win == True:
        print("נצחת")
        mes = you_success(word1)
        if mes == 'Not found cookie':
            print('אינך מחובר המשחק אינו התעדכן במערכת')
    else:
        print("נכשלת")
        mes = you_fail()
        if mes == 'Not found cookie':
            print('אינך מחובר המשחק אינו התעדכן במערכת')
    nt = False
    while nt == False:
        endB = input("אם ברצונך לשחק שוב הקש 1, להתנתק הקש 2, להסטוריית המשחקים שלך הקש 3")
        try:
            if endB != "1" and endB != "2" and endB != "3":
                raise wrongOption()
            nt = True
        except wrongOption as e:
            print(e)
        except:
            print("Error!!!")
    endB = int(endB)
    if endB == 1:
        playGame()
    elif endB == 2:
        print("סיימנו")
    else:
        print(your_history())


def winner(w: str):
    x = w.find('_', 0, len(w))
    if x == -1:
        return True
    return False


from regidtr_login import login

if __name__ == "__main__":
    playGame()
