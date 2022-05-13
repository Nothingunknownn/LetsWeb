from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gfi2d235jgasdsdsds35jfdsfp12'

menu = [{"name": "VK", "url": "vk-page"},
        {"name": "Telegram", "url": "telegram-page"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
def main():
    return render_template('main.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='Обо мне', menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "nothing" and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Профиль пользователя: {username}"


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404

@app.errorhandler(401)
def unauthorizedUser(error):
    return render_template('page401.html', title="Пожалуйста, авторизуйтесь", menu=menu)

# with app.test_request_context():
#     print(url_for('main'))
#     print(url_for('about'))
#     print(url_for('profile', username="Kirill"))


if __name__ == "__main__":
    app.run(debug=True)
