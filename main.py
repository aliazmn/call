from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/back")
def callback():
    with open("./data.txt", "w") as f:
        f.write(f"data:{request.data} , query: {request.query_string}")

    return Response("done !")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
