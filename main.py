from flask import Flask, redirect, request
import json

app = Flask(__name__)
with open("config.json", "r") as json_file:
    json_data = json_file.read()
data_dict = json.loads(json_data)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_to_lmao(path):
    user_input_path = request.path[1:]
    return redirect(f"https://github.com/{data_dict['user']}/{user_input_path}", code=301)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=data_dict['port'])
