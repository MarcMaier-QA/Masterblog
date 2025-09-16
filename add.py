from flask import Flask, render_template, request, redirect, url_for
from utils import load_posts, save_posts

app = Flask(__name__)

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        posts = load_posts()
        new_post = {
            "id": len(posts) + 1,
            "author": request.form['author'],
            "title": request.form['title'],
            "content": request.form['content']
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
