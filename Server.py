from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import time
import random
import pickle
from json import dumps as jsonstring
import json
from typing import List
from User import User

# import @wraps
app = Flask(__name__)  # יצירת מופע מהשרת שמקבל את שם המודול
CORS(app, supports_credentials=True)

# Users = List[User]
Users = []


# User1 = [User] = []
def my_decorator(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        p = request.cookies.get('password_name')
        if p:
            return func(*args, **kwargs)
        return "Not found cookie"

    wrapper.__name__ = func.__name__
    return wrapper


@cross_origin(app, supports_credentials=True)
@app.route('/add_User_new', methods=["GET", "POST"])
def add_User_new_func():
    if request.method == "GET":
        return jsonify(len(Users))
    # u = pickle.loads(request.get_data())
    u = request.json
    # Users.append(u)
    # json_str = json.dumps(u, indent=4)
    file = open("newallusers1.txt", "a")
    # file.write("/njjjj")
    print(f"\n{u}", file=file)
    file.close()
    # print(json_str)
    return "welcome"


@cross_origin(app, supports_credentials=True)
@app.route('/add_User', methods=["GET", "POST"])
def add_User_func():
    if request.method == "GET":
        return jsonify(len(Users))
    u = pickle.loads(request.get_data())
    Users.append(u)
    # json_str = json.dumps(u, indent=4)
    file = open("newallusers.txt", "a")
    file.write("/njjjj")
    print("\nSomething", file=file)
    file.close()
    # print(json_str)
    return "welcome"


@cross_origin(app, supports_credentials=True)
@app.route('/start_game', methods=["POST", "GET"])
@my_decorator
def start_game_func():
    if request.method == "GET":
        return "Join with us"
    file1 = open('./allWords.txt', 'r')
    my_list = list(map(lambda x: x.strip(), file1.readlines()))
    random.shuffle(my_list)
    num = request.json
    return my_list[num % len(my_list)]


@cross_origin(app, supports_credentials=True)
@app.route('/you_in', methods=["POST"])
def you_in_func():
    pas = request.json
    paa = ""
    for use in Users:
      if str(use.passwordU)[2:len(str(use.passwordU)) - 3] == pas:
          return jsonify(True)
    return jsonify(False)

    # for use in Users:
    #     # q = str(use.passwordU)[2:len(str(use.passwordU))-3]
    #     # return jsonify(q)
    #     if str(use.passwordU)[2:len(str(use.passwordU)) - 3] == pas:
    #         return jsonify(True)
    # return jsonify(False)



@cross_origin(app, supports_credentials=True)
@app.route('/set_cookie', methods=["POST"])
def set_cookie_func():
    p = request.json
    response = make_response(f"Cookie set! - {p}")
    response.set_cookie('password_name', p, max_age=70, httponly=True, secure=False)
    print(response.headers['Set-Cookie'])

    return response


@cross_origin(app, supports_credentials=True)
@app.route('/get_cookie', methods=['GET'])
@my_decorator
def get_cookie_func():
    pas = request.cookies.get('password_name')
    for u in Users:
        if str(u.passwordU)[2:len(str(u.passwordU)) - 3] == pas:
            return f" Hello to {str(u.nameU)[2:len(str(u.nameU)) - 3]}"


@cross_origin(app, supports_credentials=True)
@app.route('/succses_fail', methods=['POST', 'GET'])
@my_decorator
def succses_func():
    pas = request.cookies.get('password_name')
    for u in Users:
        if str(u.passwordU)[2:len(str(u.passwordU)) - 3] == pas:
            if request.method == "GET":
                u.countGamesU = u.countGamesU + 1
                return "Updatl your faik!!!!!"
            u.countGamesU = u.countGamesU + 1
            u.countWinU = u.countWinU + 1
            u.wordsU.add(request.json)
            return "Update yor win!!!!!"
    return "not found User"


@cross_origin(app, supports_credentials=True)
@app.route('/history', methods=['GET'])
@my_decorator
def history_func():
    pas = request.cookies.get('password_name')
    for u in Users:
        if str(u.passwordU)[2:len(str(u.passwordU)) - 3] == pas:
            return f"countGamesU - {u.countGamesU} countWinU - {u.countWinU}  u.wordsU -{u.wordsU}"
    return "not found User"


if __name__ == "__main__":
    app.run(debug=True)  # 127.0.0
