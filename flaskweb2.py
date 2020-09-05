from flask import *
app = Flask( __name__ )

# @app.route('/')
# def home():
#     return "welcome to the home page"

# @app.route('/success/<username>')
# def success(username):
#     return f"Successful login {username}"

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         user = request.form['name']
#         return redirect(url_for('success',username=user))
#     else:
#         user = request.args.get('name')
#         return redirect(url_for('success',username=user))


# first template program
# @app.route('/')
# def home():
#     return "welcome to the home page"

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         user = request.form['name']
#         return render_template('temp1.html',name = user)

# condtional template
# @app.route('/')
# def home():
#     return "welcome to the home page"

# @app.route('/login',methods=['GET','POST'])
# def condtionaltemplate():
#     if request.method == 'POST':
#         user = int(request.form['name'])
#         return render_template('temp1.html',name = user)

# loop template
@app.route('/')
def home():
    return "welcome to the home page"

@app.route('/login')
def condtionaltemplate():
        fruit = {"mango":50, "apple":70, "banana":60}
        return render_template('temp2.html',name = fruit)

if __name__ == "__main__":
    app.run(debug=True)




