from flask import Flask, request, render_template, jsonify
from utils import ToGet

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["JSON_AS_ASCII"] = False

posts = ToGet("./data/posts.json")
coments = ToGet("./data/comments.json")


@app.route("/")
def page_index():
    """главная страница"""

    all_posts = posts.get_posts_all()
    return render_template("index.html", posts=all_posts)


@app.route("/posts/<post>")
def page_one_post(post):
    """страница с постом, принимает 'pk'"""

    one_post = posts.get_post_by_pk(post)
    comments_of_post = coments.get_comments_by_post_id(post)
    return render_template("post.html", post=one_post, coment=comments_of_post)


@app.route("/search/")
def search_posts():
    """страница с постами найденными по слову"""

    s = request.args.get("s")

    post_from_key = posts.search_for_posts(s)
    count_posts = len(post_from_key)
    all_posts = posts.get_posts_all()
    if s == None:
        return render_template("search.html", posts=all_posts, count=count_posts)
    return render_template("search.html", posts=post_from_key, count=count_posts)


@app.route("/users/<username>")
def user_posts(username):
    """страница с постами пользователя"""

    user_posts = posts.get_posts_by_user(username)
    return render_template("user-feed.html", posts=user_posts, user=username)


@app.route("/api/posts/")
def api_posts():
    """страница выводит все посты в json"""

    posts_js = posts.get_posts_all()
    return jsonify(posts_js)


@app.route("/api/posts/<post_id>")
def api_one_post(post_id):
    """страница выводит один пост json"""

    one_post = posts.get_post_by_pk(post_id)
    return jsonify(one_post)


if __name__ == "__main__":
    app.run()
