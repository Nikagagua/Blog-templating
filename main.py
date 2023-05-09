from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        "index.html",
        posts=Post().all_posts,
    )


@app.route('/post/<num>')
def get_post(num):
    return render_template(
        'post.html',
        posts=Post().all_posts,
        num=int(num),
    )


if __name__ == "__main__":
    app.run(debug=True)
