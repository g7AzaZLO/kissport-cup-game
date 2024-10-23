# cup.py

import random
import math


def main():
    while True:
        print(' ' * 27 + 'CUP')
        print(' ' * 20 + 'CREATIVE COMPUTING')
        print(' ' * 18 + 'MORRISTOWN, NEW JERSEY')
        print('\n' * 3, end='')  # Исправлено количество пустых строк

        # Инициализация массива S(30,60)
        S = [[0 for _ in range(60)] for _ in range(30)]

        # Линии 30-40: Генерация позиции чашки L
        while True:
            L = int(60 * random.random()) + 1
            if L != 1 and L != 60:
                break

        # Линия 50: Генерация силы гравитации G
        G = int(10 * random.random()) + 1

        print(f"THE CUP IS 30 LINES DOWN AND {L:>3}  SPACES OVER.")
        print(f"THE PULL OF GRAVITY IS {G:>2}  LINES/SECOND/SECDND.")
        print("WHAT IS THE PUSH YOU WOULD LIKE TO GIVE THE BALL")
        print("ACROSS THE PAPER (IN SPACES/SECOND)", end='')
        T = float(input())

        print("THE RESULTS MAY TAKE ANYWHERE BETWEEN 30 AND 90 SECONDS.")

        # Линия 120: Инициализация массива S
        for S1 in range(30):
            for S2 in range(60):
                S[S1][S2] = 0

        # Линия 130: Установка позиции чашки
        # Корректировка индексов для Python (0-индексация)
        S[29][L - 1] = 1
        S[29][L - 2] = 1
        S[29][L] = 1
        S[28][L - 2] = 1
        S[28][L] = 1

        # Линия 140: Основной цикл симуляции
        Z = 1.0
        Z_max = math.sqrt(60 * G) / G
        W = 0  # Инициализация переменной W

        while Z <= Z_max:
            Y = T * Z * 2
            X = G / 2 * Z ** 2

            if X > 30.5 or X < 0.5 or Y > 60.5 or Y < 0.5:
                break  # Переход на линию 300

            IX = int(X)
            IY = int(Y)

            # Проверка попадания в чашку
            if ((IX == 29 and IY == L - 1) or
                    (IX + 1 == 29 and IY + 1 == L - 1) or
                    (IX == 29 and IY == L - 2) or
                    (IX + 1 == 29 and IY + 1 == L - 2)):
                W = 1
                S[28][L - 1] = 2  # Линия 335
                break  # Переход на линию 335

            if ((IX == 29 and IY == L) or
                    (IX + 1 == 29 and IY + 1 == L)):
                W = 2
                S[28][L - 1] = 2  # Линия 335
                break  # Переход на линию 335

            # Линия 240: Отметка позиции мяча
            if 0 <= int(X) < 30 and 0 <= int(Y) < 60:
                S[int(X)][int(Y)] = 2

            # Линии 250-280: Стирание следа за мячом
            for D in range(1, 6):
                if Y < 6:
                    break  # Переход на линию 290
                if int(Y) - D >= 0 and 0 <= int(X) < 30:
                    S[int(X)][int(Y) - D] = 0

            Z += 0.01  # Шаг цикла Z

        # Линия 340: Если мяч не попал в чашку
        if W == 0:
            pass  # Ничего не делаем
        # Линия 345: Продолжаем

        P = " *."

        # Восстановление чашки (линии 360-365)
        S[29][L - 1] = 1
        S[29][L - 2] = 1
        S[29][L] = 1
        S[28][L - 2] = 1
        S[28][L] = 1

        # Линии 370-510: Вывод поля
        for X in range(30):
            line_output = ''
            for Y in range(60):
                if S[X][Y] != 0:
                    # Линия 430: Вывод символа
                    line_output += P[S[X][Y]]

                    # Логика для задержки вывода (опционально)
                    # Здесь мы можем добавить логику для задержки, если необходимо

            if line_output:
                print(line_output)

        print()

        # Линии 530-600: Проверка результата и предложение сыграть снова
        if W == 1:
            print("RIGHT IN!!!")
        elif W == 2:
            print("YOU ALMOST DIDN'T MAKE IT, BUT IT BOUNCED IN.")
        else:
            print("YOU MISSED; TRY AGAIN.")
            continue  # Переход на линию 60

        print("DO YOU WANT TO PLAY AGAIN?")
        A = input()
        if A.strip().upper().startswith('Y'):
            continue  # Переход на линию 30
        else:
            break  # Конец игры


if __name__ == "__main__":
    main()
