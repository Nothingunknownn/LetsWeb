from flask import Flask, render_template

app = Flask(__name__)

menu = ['VK', 'Instagram', 'Telegram']


@app.route('/')
def main():
    return render_template('main.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='Обо мне', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
