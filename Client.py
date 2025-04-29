import requests
from requests import session
import time
from User import User
import json
import pickle

basic_url = "http://127.0.0.1:5000"
session = session()


def all_user():
    response = session.get("http://127.0.0.1:5000/add_User")
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error!!!!!!:{response.status_code}")


# un = User("Gilannn", "126543", "128653")
# print(un.__str__())


un = {'nameU': 'shalva', 'idU': '98764', 'passwordU': '09'}


# print(unn)


def add_user(u):
    data = pickle.dumps(u, protocol=2)
    response = session.post(f"{basic_url}/add_User", data=data)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error:{response.status_code} - {response.text}")


def add_user_new(z):
    def serialize_sets(obj):
        if isinstance(obj, set):
            return list(obj)

        return obj

    json_str = json.dumps(z.wordsU, default=serialize_sets)
    z.wordsU=json_str
    x = z.to_dict()
    u = json.dumps({"use111": x})
    # print(f'client ---{u}')
    # data = pickle.dumps(u, protocol=2)
    response = session.post(f"{basic_url}/add_User_new", json=u)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error:{response.status_code} - {response.text}")


def startGame(x):
    response = session.post(f"{basic_url}/start_game", json=x)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error:{response.status_code}"


def start__Game():
    response = session.get(f"{basic_url}/start_game")
    if response.status_code == 200:
        return response.text
    else:
        return f"Error:{response.status_code}"


def check_you_in(p):
    response = session.post(f"{basic_url}/you_in", json=p)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error:{response.status_code}"


def setCookie(p):
    response = session.post(f"{basic_url}/set_cookie", json=p)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error :{response.status_code}"


def getCookie():
    # cookies = cook
    # print(f"Cookie: {cookies}")
    response = session.get(f"{basic_url}/get_cookie")
    if response.status_code == 200:
        return response.text
    else:
        return f"Error{response.status_code}"


def you_success(w):
    response = session.post(f"{basic_url}/succses_fail", json=w)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error :{response.status_code}"


def you_fail():

    response = session.get(f"{basic_url}/succses_fail")
    if response.status_code == 200:
        return response.text
    else:
        return f"Error :{response.status_code}"


def your_history():
    response = session.get(f"{basic_url}/history")
    if response.status_code == 200:
        return response.text
    else:
        return f"Error :{response.status_code}"


# def getCookie(cook):
#     cookies = cook
#     print(f"Cookie: {cookies}")
#     response = session.get(f"{basic_url}/get_cookie", cookies=cookies)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return f"Error{response.status_code}"

# # cookies = response.cookies.get_dict()  # חילוץ העוגיות מהבקשה הקודמת
# # print(f"Cookie: {cookies}")
# response = session.get(f'{basic_url}get_cookie') # , cookies=cookies
# print(response.text)
#
# # המתנה של 10 שניות כדי לראות שהעוגיה נמחקה
# # time.sleep(10)
# # אפשר גם למחוק את העוגייה
# response = session.delete(f"{basic_url}delete_cookie")
# print(response.text)
#
# # ניסיון לגשת לעוגייה
# response = session.get(f'{basic_url}get_cookie')
# print(response.text)
#


if __name__ == "__main__":
    all_user()
    # a = User
    # unn = json.dumps(a.__dict__)
    add_user()
    all_user()
    startGame()

# def add_user(u):
# basic_urlu = "http://127.0.0.1:5000"  # שמירת כתובת הבסיס- הכתובת עליה השרת רץ
# response = session.get(f"{basic_url}/say_hello")  # יצירת בקשת get
# if response.status_code == 200:  # אם הבקשה הצליחה
#     print(response.json())  # הדפסת התוכן- הפעולה ההפוכה מהכנסה ל-json
# else:
#     print(f"Error: {response.status_code}")
#
# message = {'name': 'Sara'}  # יצירת האובייקט אותו נרצה לשלוח בבקשה
# # json=message כדי לשלוח את האובייקט בבקשה נשתמש ב:
# response = session.post(f"{basic_url}/say_hello", json=message)  # בקשת post
# if response.status_code == 200:  # אם הבקשה הצליחה
#     print(response.json())  # הדפסת התוכן
# else:
#     print(f"Error: {response.status_code}")
