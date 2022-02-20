from flask import jsonify, Flask

app = Flask(__name__)


@app.route("/blogs")
def blogs():
    blogs = (
        {
            "id": 1,
            "title": "Tips & Trik liburan di masa pandemi",
            "category": "Tips & Trick",
            "author": "Eric Julianto",
            "thumbnail": "https://raw.githubusercontent.com/algonacci/Free-CDN/main/Freeducation-CDN/sekolah.jpg"
        },
        {
            "id": 2,
            "title": "Tips & Trik liburan di masa pandemi",
            "category": "Tips & Trick",
            "author": "Eric Julianto",
            "thumbnail": "https://raw.githubusercontent.com/algonacci/Free-CDN/main/Freeducation-CDN/sekolah.jpg"
        }
    ),

    return jsonify(blogs)


if __name__ == "__main__":
    app.run()
