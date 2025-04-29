# from flask import Flask, jsonify, request, make_response
# from flask_cors import CORS, cross_origin
# import time
#
# app = Flask(__name__)  # יצירת מופע מהשרת שמקבל את שם המודול
# CORS(app, supports_credentials=True)
#
# Users = []
# eee
# @cross_origin(app, supports_credentials=True)
# @app.route('/add_User', methods=["GET", "POST"])
# def add_User_func():
#     if request.method == "GET":
#         return jsonify(Users)
#     u = request.json
#     Users.append(u)
#     return jsonify(Users)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)  # 127.0.0
