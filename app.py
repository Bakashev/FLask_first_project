from settings import db, app
from models import Post
from flask import render_template, request, flash, url_for, redirect
from datetime import datetime


@app.route('/')
def home():
    all_post: list[Post] = Post.query.all()
    #проверяем какого типа all_post и что в нем находиться
    print(type(all_post))
    print(all_post)
    return render_template('home.html', posts=all_post)


@app.route('/create', methods=['GET', 'POST'])
def createpost():
    if request.method == 'POST':
        title = request.form['zagolovok']
        content = request.form['soderjimoe']
        if not title or not content:
            flash("Не заполнено поле")
        else:
            post = Post(
                title=title,
                content=content,
                created=datetime.now()
            )
            db.session.add(post) # Добавляем в таблицу
            db.session.commit() # подтверждаем
    return render_template('create_post.html')


@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    post: Post = db.get_or_404(Post, post_id, description='Не найдено значение')
    return render_template('show_post.html', post=post)


@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id: int):
    post: Post = db.get_or_404(Post, post_id, description='Значение не найдено')
    if request.method == 'POST':

        title = request.form['zagolovok']
        content = request.form['opisanije']
        if not title or not content:
            flash('Не заполнено поле')
        else:
            post.title = title
            post.content = content
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('show_post', post_id=post.id))

    return render_template('edit_post.html', post=post)


@app.route('/post/<int:post_id>/delete', methods=['GET','POST'])
def delete_post(post_id):
    post: Post = db.get_or_404(Post, post_id, description='Значение не найдено')
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('delete_post.html', posts=post)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
