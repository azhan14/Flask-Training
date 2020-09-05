# from flask import Flask, request, jsonify, make_response, abort, redirect
# from flask import *
# app = Flask( __name__ )

# @app.route('/')
# def homepage():
#     return "Welcome to the home page"

# @app.route('/admin')
# def adminlogin():
#     return "hello admin"

# @app.route('/guest/<guestname>')
# def guestlogin(guestname):
#     return f"hello {guestname}"

# @app.route("/user/<name>",methods=['GET'])
# def login(name):
#     if name == 'admin':
#         return redirect(url_for('adminlogin'))
#     if name != 'admin':
#         return redirect(url_for('guestlogin',guestname=name))

# if __name__ == "__main__":
#     app.run(debug=True)