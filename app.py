from flask import Flask,jsonify,request,abort,make_response

app = Flask(__name__)

bucket_list =[
    {
        'id' : 1,
        'name' : 'sky diving',
        'description' : 'jump from 35000 ft'
    },
    {
        'id' : 2,
        'name' : 'bungee jumping',
        'description' : 'The last resort',
    },
    {
        'id' : 3,
        'name' : 'drive a McLaren P1',
        'description' : 'drive on swiss mountains'
    },
    {
        'id' : 4,
        'name' : 'cliff jumping',
        'description' : 'jump from a 1000mt high cliff mountain'
    }
]

#error handling 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message':'missing or invalid data'})) , 404

#method to create bucket list
@app.route('/bl',methods=['POST'])
def create_bl_item():
    if not request:
        abort(404)
    if not 'name' in request.json:
        abort(404)
    if not 'description' in request.json:
        abort(404)

    bl_item ={
    'id' : bucket_list[-1]['id'] + 1,
    'name' : request.json['name'],
    'description' : request.json['description']
    }
    
    bucket_list.append(bl_item)
    
    return jsonify({'bucket list item' : bl_item }), 201


#method to update bucket list item
@app.route('/bl/<int:bl_id>',methods=['PUT'])
def edit(bl_id):
    bl_item = [item for item in bucket_list if item['id'] == bl_id]
    if len(bl_item) == 0:
        abort(404)
    if not request:
        abort(404)
    if not 'name' in request.json:
        abort(404)
    if not 'description' in request.json:
        abort(404)
    
    item = {
        'id' : bl_id,
        'name' : request.json['name'],
        'description' : request.json['description']
    }

    ind = bucket_list.index(bl_item[0])
    bucket_list[ind].update(item)
    return jsonify({'updated item': item}),201

#method a bucket list item
@app.route('/bl/<int:bl_id>',methods=['DELETE'])
def delete_item(bl_id):
    bl_item = [item for item in bucket_list if item['id'] == bl_id]
    if len(bl_item) == 0:
        abort(404)
    bucket_list.remove(bl_item[0])
    return jsonify({'message' : 'item deleted'}),201

#method to read bucket list
@app.route('/bl',methods=['GET'])
def get_bl():
    return jsonify({'bucket list' : bucket_list}),200

#method to read specified item from bucket list
@app.route('/bl/<int:bl_id>',methods=['GET'])
def get_bl_item(bl_id):
    bl_item = [item for item in bucket_list if item['id'] == bl_id]
    if len(bl_item) == 0:
        abort(404)
    return jsonify({'item' : bl_item}),200

@app.route('/')
def index():
    return "HELLO WORLD.....!!!"

if __name__ =="__main__":
    app.run(debug=True)