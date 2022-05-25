from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/back/")
def callback():
    with open("data.txt", "w") as f:
        f.write(f"data:{request.data} , query: {request.query_string}")

    return Response("done !")
