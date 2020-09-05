from flask import Flask, jsonify, make_response, abort, request

app = Flask( __name__ )

todos = [
    {
        'id':1,
        'title':'to learn todo api',
        'progress':'not done'
    },
    {
        'id':2,
        'title':'intern project case study',
        'progress':'not done'
    },
    {
        'id':3,
        'title':'aptitude preparation',
        'progress':'not done'
    }
]
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message':'file do not exist or wrong url'})),404

@app.errorhandler(400)
def no_parameter(error):
    return make_response(jsonify({'message':"parameters not passed"})),400

@app.route("/todo/get",methods=['GET'])
def gettodo():
    return make_response(jsonify({'todos':todos})),200

@app.route("/todo/<int:todo_id>",methods=['GET'])
def getonetodo(todo_id):
    todo =[todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    return make_response(jsonify({'todos':todo})),200

@app.route("/todo/inserttodo",methods=['POST'])
def createtodo():
    if not request:
        abort(404)
    if not "title" in request.json:
        abort(400)
    if not "progress" in request.json:
        abort(400)
    newtodo = {
        'id':todos[-1]['id'] + 1,
        'title': request.json['title'],
        'progress': request.json['progress']
    }
    todos.append(newtodo)
    return make_response(jsonify({'newtodo':newtodo})),200

@app.route("/todo/updatetodo/<int:get_id>",methods=['PUT'])
def updatetodo(get_id):
    todo = [todo for todo in todos if todo['id'] == get_id]
    if not request:
        abort(404)
    if len(todo) == 0:
        abort(404)    
    if not 'progress' in request.json:
        abort(400)
    updatedtodo = {
        'id':get_id,
        'title': todo[0]['title'],
        'progress': request.json['progress']
    }
    ind = todos.index(todo[0])
    todos[ind].update(updatedtodo)
    return make_response(jsonify({'updatedtodo':updatedtodo})),200

@app.route("/todo/deltodo/<int:get_id>",methods=['DELETE'])
def deltodo(get_id):
    todo = [todo for todo in todos if todo['id'] == get_id]
    if len(todo) == 0:
        abort(404)
    todos.remove(todo[0])
    return jsonify({'message' : 'todo deleted'}),201

if __name__ == "__main__":
    app.run(debug=True)