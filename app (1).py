'''
rock - paper == paper
paper - scissor == scissor
scissor - rock == rock
draw
'''
from flask import Flask,jsonify
import random

app = Flask(__name__)

@app.route('/<int:user_selection>',methods=['GET'])
def check(user_selection):
    comp_choice = random.randint(1, 3)
    usr_choice = user_selection
    flag = None  # 0 for draw, 1 for comp, 2 for user
    print(comp_choice)

    if (comp_choice == usr_choice):
        flag = 0
    elif (comp_choice == 1):
        if (usr_choice == 2):
            flag = 2
        elif (usr_choice == 3):
            flag = 1
    elif (comp_choice == 2):
        if (usr_choice == 1):
            flag = 1
        elif (usr_choice == 3):
            flag = 2
    elif (comp_choice == 3):
        if (usr_choice == 1):
            flag = 2
        elif (usr_choice == 2):
            flag = 1
    comment = ''
    if flag == 0:
        comment = "draw"
    elif flag == 1:
        comment = "comp wins"
    elif (flag == 2):
        comment = "user wins"

    return jsonify({
        "user choice" : user_selection,
        "computers choice" : comp_choice,
        "winner" : flag,
        "comment" : comment
    }),200

if __name__ =="__main__":
    app.run(debug=True)
