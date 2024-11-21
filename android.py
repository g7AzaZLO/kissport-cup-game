import random
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class ConsoleWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsoleWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Поле для вывода (консоль)
        self.output = TextInput(readonly=True, font_size=14)
        self.add_widget(self.output)

        # Поле для ввода
        self.input = TextInput(multiline=False, font_size=14)
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

        self.input_disabled = True
        self.input.disabled = True  # Отключаем ввод до тех пор, пока не потребуется
        self.input_buffer = ''
        self.input_callback = None

    def write(self, text):
        # Обновляем вывод в главном потоке
        Clock.schedule_once(lambda dt: self._update_output(text))

    def _update_output(self, text):
        self.output.text += text

    def flush(self):
        pass

    def on_enter(self, instance):
        if not self.input_disabled and self.input_callback:
            self.input_buffer = self.input.text
            self.input.text = ''
            self.input_disabled = True
            self.input.disabled = True
            callback = self.input_callback
            self.input_callback = None
            callback(self.input_buffer)


class CupGameApp(App):
    def build(self):
        self.console = ConsoleWidget()
        sys.stdout = self.console
        sys.stdin = self
        # Запускаем игру
        Clock.schedule_once(lambda dt: self.run_game())
        return self.console

    def run_game(self):
        # Начинаем генератор основной функции
        self.game_iter = main(self)
        # Выполняем первый шаг
        self.run_next_step(None)

    def run_next_step(self, input_value):
        try:
            # Выполняем до следующего запроса ввода
            prompt = self.game_iter.send(input_value)
            # Если требуется ввод, показываем поле ввода
            self.console.write(prompt)
            self.console.input_disabled = False
            self.console.input.disabled = False
            self.console.input.focus = True
            self.console.input_callback = self.run_next_step
        except StopIteration:
            pass

    def input(self, prompt=''):
        # Этот метод теперь не используется
        pass


def main(app):
    while True:
        # Вывод заголовка
        print(' ' * 27 + 'CUP')
        print(' ' * 20 + 'CREATIVE COMPUTING')
        print(' ' * 18 + 'MORRISTOWN, NEW JERSEY')
        print('\n' * 3, end='')

        L = random.randint(1, 60)
        while L == 1 or L == 60:
            L = random.randint(1, 60)

        G = random.randint(1, 10)

        # Вывод информации об игре
        print(f"THE CUP IS 30 LINES DOWN AND {L} SPACES OVER.")
        print(f"THE PULL OF GRAVITY IS {G} LINES/SECOND/SECDND.")
        print("WHAT IS THE PUSH YOU WOULD LIKE TO GIVE THE BALL")
        T_input = yield "ACROSS THE PAPER (IN SPACES/SECOND)? "
        try:
            T = float(T_input)
        except ValueError:
            print("PLEASE ENTER A NUMBER.")
            continue

        print("THE RESULTS MAY TAKE ANYWHERE BETWEEN 30 AND 90 SECONDS.")

        # Инициализация массива S(1..30,1..60)
        S = [[0] * 61 for _ in range(31)]  # S[0..30][0..60]

        # Установка позиции чашки
        S[30][L] = 1
        S[30][L - 1] = 1
        S[30][L + 1] = 1
        S[29][L - 1] = 1
        S[29][L + 1] = 1

        W = 0
        Z = 1.0
        Z_max = ((60 * G) ** 0.5) / G

        while Z <= Z_max:
            Y = T * Z * 2
            X = G / 2 * Z ** 2

            if X > 30.5 or X < 0.5 or Y > 60.5 or Y < 0.5:
                break

            IX = int(X)
            IY = int(Y)

            if (IX == 29 and IY == L) or \
                    (IX + 1 == 29 and IY + 1 == L) or \
                    (IX == 29 and IY == L - 1) or \
                    (IX + 1 == 29 and IY + 1 == L - 1):
                W = 1
                S[29][L] = 2
                break

            if (IX == 29 and IY == L + 1) or \
                    (IX + 1 == 29 and IY + 1 == L + 1):
                W = 2
                S[29][L] = 2
                break

            if 1 <= IX <= 30 and 1 <= IY <= 60:
                S[IX][IY] = 2

            if IY >= 6:
                for D in range(1, 6):
                    if IY - D >= 1:
                        S[IX][IY - D] = 0

            Z += 0.01

        S[30][L] = 1
        S[30][L - 1] = 1
        S[30][L + 1] = 1
        S[29][L - 1] = 1
        S[29][L + 1] = 1

        P = " *."

        print()

        for X in range(1, 29):
            if all(S[X][Y] == 0 for Y in range(1, 61)):
                continue

            line_output = ''
            for Y in range(1, 61):
                line_output += P[S[X][Y]]
            print(line_output.rstrip())

        print()

        for X in range(29, 31):
            line_output = ''
            for Y in range(1, 61):
                line_output += P[S[X][Y]]
            print(line_output.ljust(60))

        print()

        if W == 1:
            print("RIGHT IN!!!")
        elif W == 2:
            print("YOU ALMOST DIDN'T MAKE IT, BUT IT BOUNCED IN.")
        else:
            print("YOU MISSED; TRY AGAIN.")
            continue

        print("DO YOU WANT TO PLAY AGAIN?")
        A = yield ''
        if A.strip().upper().startswith('Y'):
            continue
        else:
            break

    # Игра окончена
    print("THANK YOU FOR PLAYING!")
    App.get_running_app().stop()


if __name__ == '__main__':
    CupGameApp().run()
