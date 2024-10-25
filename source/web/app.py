from flask import Flask, render_template, request
import sys
from multiprocessing import Process
from time import sleep
import os

sys.path.append("..")
import game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        user_input = request.form.get('direction')
        if user_input:
            write_file('input.txt', user_input)
            sleep(2)  # Небольшая задержка для синхронизации

    game_output = read_file('print.txt')
    return render_template('play.html', text=game_output)

def background_worker():
    def input_override(prompt=""):
        while True:
            sleep(2)
            if os.path.exists('input.txt'):
                inp = read_file('input.txt')
                os.remove('input.txt')
                return inp.strip()

    def print_override(msg="", end="\n"):
        write_file('print.txt', msg + end)

    if os.path.exists('input.txt'):
        os.remove('input.txt')
    if os.path.exists('print.txt'):
        os.remove('print.txt')

    # Запускаем вашу игру с переопределенными функциями ввода/вывода
    game.main(print_override, input_override)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')

if __name__ == '__main__':
    process = Process(target=background_worker)
    process.start()
    app.run(debug=True)
