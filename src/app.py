from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [

    {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    output = jsonify(todos)
    return output

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_data = json.loads(request_body)
    todos.append(decoded_data)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    return jsonify(todos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)