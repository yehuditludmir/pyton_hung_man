import json
class User:

    def __init__(self, nameU, idU, passwordU):
        self.nameU = nameU,
        self.idU = idU,
        self.passwordU = passwordU,
        self.countGamesU = 0
        self.wordsU = {" "}
        self.countWinU = 0

    def __str__(self):
        return f"nameUser :{self.nameU} idUser : {self.idU} passwordUser:{self.passwordU} countGamesUser : {self.countGamesU} wordsUser : {self.wordsU} countWinUser :{self.countWinU}"

    def to_dict(self):
        return {
            "name": self.nameU,
            "number": self.idU,
            "passwordUser": self.passwordU,
            "countGamesUser": self.countGamesU,
            "wordsUser": self.wordsU,
            "countWinUser": self.countWinU
        }


# import requests
# from requests import session
# import time

#u = User("Gila", "12346543", "123")
#print(u)
#r = u.to_dict()
#print(r)
#jsdata = json.dumps({"use111": r})
#print(jsdata)

# u1 = User("ooooo", "12346543", "123")
# userrr = [u, u1]
# for a in userrr:
#     a.passwordU
# from Client import startGame


# print(u.__str__())
# # un = User("Gilannn", "126543", "128653")
# # print(un.__str__())
# basic_url = "http://127.0.0.1:5000"
# un = {'nameU': 'Mriam', 'idU': '98764', 'passwordU': '09'}
#
# def add_user(un):
#     response = session.post(f"{basic_url}/add_User", json=un)
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(f"Error:{response.status_code}")
#
#
# add_user(un)
