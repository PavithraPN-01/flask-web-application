from flask import Flask, request, jsonify

app = Flask(__name__)
users = [
    {'id':1,'name':'abc'},
    {'id':2,'name':'xyz'}
]


#get all the user's data/fetch the user data
@app.route('/users',methods = ['GET'])
def get_users():
    return jsonify(users)


@app.route('/users', methods = ['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201


#update request
@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    print("data", data)
    user = next((u for u in users if u['id'] == user_id), None)
    print("user",user)

    if not user:
        return jsonify({"error","user not found"}), 404
    
    #update the field
    user['name'] = data.get('name',user['name'])

    return jsonify(user)


@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
     user = next((u for u in users if u['id'] == user_id), None)


     if not user:
        return jsonify({"error":"user not found"}), 404
     
     users.remove(user)
     return jsonify({'message':"user deleted succesfully"})
    

if __name__ == '__main__':
    app.run(debug=True)