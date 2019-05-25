from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from postForm import PostForm


app = Flask(__name__)

file_path = os.path.abspath(os.getcwd()) + "/blog.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path

db = SQLAlchemy(app)


class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)    


@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


'''

@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit(id):
    # Create cursor
    cur = db.connection.cursor()

    # Get post by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    post = cur.fetchone()
    cur.close()
    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(title)
        # Execute
        cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))

return render_template('edit_article.html', form=form)
'''


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('edit.html', post=post)


@app.route('/editpost/<int:post_id>', methods=['GET', 'POST'])
def editpost(post_id):
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    updated = Blogpost.query.filter_by(id=post_id).update({Blogpost.title: post.title})
    updated = Blogpost.query.filter_by(id=post_id).update({Blogpost.subtitle: post.subtitle})
    updated = Blogpost.query.filter_by(id=post_id).update({Blogpost.author: post.author})
    updated = Blogpost.query.filter_by(id=post_id).update({Blogpost.content: post.content})

    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    Blogpost.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)