from flask import Flask, jsonify, make_response, abort, request

app = Flask( __name__ )
bucketlist = [
    {
        'id':1,
        'objective':'big house',
        'description':'two-storey building'        
    },
    {
        'id':2,
        'objective':'anxiety free',
        'description':'desperately wanted to free of anxiety'        
    }    
]

@app.errorhandler(404)
def notfound(error):
    return make_response(jsonify({'message':'wrong url'})), 404

@app.errorhandler(400)
def nopara(error):
    return make_response(jsonify({'message':'no parameters'})), 400

@app.route("/mybl",methods=['GET'])
def home():
    return jsonify({'message':'welcome to home page'}), 200

@app.route("/mybl/allbl",methods=['GET'])
def getallbl():
    return make_response(jsonify({'bucketlist':bucketlist})), 200

@app.route("/mybl/<int:bl_id>",methods=['GET'])
def getbl(bl_id):
    tempbl = [bl for bl in bucketlist if bl['id'] == bl_id]
    if len(tempbl) == 0:
        abort(404)
    return make_response(jsonify({'bl':tempbl})),200

@app.route("/mybl/add",methods=['POST'])
def addbl():
    if not request:
        abort(404)
    if 'objective' not in request.json:
        abort(400)
    if 'description' not in request.json:
        abort(400)
    newbl = {
        'id': bucketlist[-1]['id'] + 1,
        'objective':request.json['objective'],
        'description':request.json['description']
    } 
    bucketlist.append(newbl)
    return make_response(jsonify({'newbucketlist':newbl})),200

@app.route("/mybl/updatelist/<int:bl_id>",methods=['PUT'])
def updbl(bl_id):
    tempbl = [bl for bl in bucketlist if bl['id'] == bl_id]
    if not request:
        abort(404)
    if 'objective' not in request.json:
        abort(400)
    if 'description' not in request.json:
        abort(400)
    upbl = {
        'id': bl_id,
        'objective':request.json['objective'],
        'description':request.json['description']
    } 
    ind = bucketlist.index(tempbl[0])
    # ind = todos.index(todo[0])
    bucketlist[ind].update(upbl)    
    return make_response(jsonify({'updatedlist':upbl})),200

@app.route("/mybl/del/<int:bl_id>", methods=['DELETE'])
def delbl(bl_id):
    tempbl = [bl for bl in bucketlist if bl['id'] == bl_id]
    if len(tempbl) == 0:
        abort(404)
    bucketlist.remove(tempbl[0])
    return jsonify({'message' : 'bucketlist deleted'}),200    

if __name__ == "__main__":
    app.run(debug=True)