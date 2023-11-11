from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
from pprint import pprint

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)


@app.route("/")
def index():
    text = "Hello, World!"
    return render_template("index.html", text=text)


@app.route("/news")
def news():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    top_story_ids = response.json()[:10]
    stories = []
    for story_id in top_story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        story_data = story_response.json()
        title = story_data.get("title")
        url = story_data.get("url")
        stories.append({"title": title, "url": url})
    return render_template("news.html", stories=stories)


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


@socketio.on("message")
def handle_message(data):
    print("Received message:", data)
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{data}")
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
    else:
        pprint(response)
        data = "Error: " + str(response.status_code)
    # Now you can access the data in the JSON response
    print(data)
    emit("message", data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app)
