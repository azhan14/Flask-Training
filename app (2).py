from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

#''.join(str(uuid.uuid1()).split('-'))
#/getall
#/todo/id ------get
#/todo    ------post
#/todo/id ------update
#/todo/id ------delete

todos = [
    {
        'id' : 1,
        'title' : 'Learn Python',
        'description' : '12:30 to 04:30, todo api and oop',
        'done' : False
    },
    {
        'id' : 2,
        'title' : 'Go Out',
        'description' : 'just chill',
        'done' : False
    }
]

#abort for 400
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'message' : 'please pass data'}))

#abort method
@app.errorhandler(404)
def not_found1(error):
    return make_response(jsonify({'message':'invalid or missing data'}))

#method to get all data
@app.route('/getall',methods=['GET'])
def get_all_todos():
    return jsonify({'todos' : todos }),200

#method to get to from id
@app.route('/todo/<int:todo_id>',methods=['GET'])
def get_todo_with_id(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        #return jsonify({'message' : 'Not Found'}),404
        abort(404)
    return jsonify({'todo':todo[0]}),200


#method to post a todo
@app.route('/todo',methods=['POST'])
def create_item():
    if not request:
        abort(404)
    if not 'title' in request.json:
        abort(404)
    if not 'description' in request.json:
        abort(404)
    
    todo = {
        'id' : todos[-1]['id'] + 1,
        'title' : request.json['title'],
        'description' : request.json['description'],
        'done' : False
    }
    todos.append(todo)
    return jsonify({'new todo' : todo}),201

#method to delete todo
@app.route('/todo/<int:todo_id>',methods=['DELETE'])
def delete_todo(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    todos.remove(todo[0])
    return jsonify({'message' : 'todo deleted'}),201

#method to update
@app.route('/todo/<int:todo_id>',methods=['PUT'])
def update(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    
    if len(todo) == 0:
        abort(404)
    if not request:
        abort(404)
    if not 'done' in request.json:
        abort(404)
    new_todo = {
        'id' : todo_id,
        'title' : todo[0]['title'],
        'description' : todo[0]['description'],
        'done' : request.json['done']
    }
    ind = todos.index(todo[0])
    todos[ind].update(new_todo)
    return jsonify({'update todo' : new_todo}),201

if __name__ == "__main__":
    app.run(debug=True)