from flask import Flask, jsonify
import random
app = Flask( __name__ )

@app.route('/')
def home():
    return "Welcome to home page"
# rock = 1, paper = 2, scissor = 3  ////    user =1 comp = 2
@app.route('/rps/<int:choice>',methods=['GET'])
def rps(choice):
    comp_choice = random.randint(1,3)
    user_choice = choice
    flag = None
    result = None
    if comp_choice ==  user_choice:
        flag = 0
    else:
        if comp_choice == 1:
            if user_choice == 2:
                flag = 1
            elif user_choice == 3:
                flag = 2
        elif comp_choice == 2:
            if user_choice == 1:
                flag = 2
            elif user_choice == 3:
                flag = 1
        elif comp_choice == 3:
            if user_choice == 1:
                flag = 1
            elif user_choice == 2:
                flag = 2
    if flag == 0:
        result = "draw"
    elif flag ==1:
        result = "user wins"
    elif flag == 2:
        result = "comp wins"
    else:
        result = "must be invalid user input"
    
    return jsonify({ 'computer_choice':comp_choice, 'user_choice':user_choice, 'winner': flag, 'result': result}),200

if __name__ == "__main__":
    app.run(debug=True)















# from flask import Flask
# app = Flask( __name__ )  # flask constructor takes the name of the current module as the argument


# # route function is the decorator which has two parameters it binds the path given in the first parameter with the function 
# # url which is the path of the website and options are the parameters to be passed to the path
# if __name__ == "__main__":
#     app.run(debug = True) # runs the app. all the changes will be updated by the server by debug = true. if it false then for every small change in code we have to restart the app to update the code
