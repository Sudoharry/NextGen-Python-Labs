from flask import Flask, request, jsonify

app = Flask(__name__) 


# @app.route("/")
# def home():
#     return "Home" 


@app.route("/get-user/<user_id>")

def get_user(user_id):
    """ Use link for access the web: http://127.0.0.1:5000/get-user/123?extra="hello" """
    user_data = {
        "user-id": user_id,
        "name" : "Harry",
        "email": "harendrabarot19@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200



@app.route("/create-user", methods=["POST"])

def create_user():
    data  = request.get_json()
    
    return jsonify(data), 200 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

  