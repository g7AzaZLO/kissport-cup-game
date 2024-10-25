import random


# Основная функция игры с кастомными print и input для веб-интеграции
def main(custom_print=print, custom_input=input):
    while True:
        # Печатаем заголовок
        custom_print(' ' * 27 + 'CUP')
        custom_print(' ' * 20 + 'CREATIVE COMPUTING')
        custom_print(' ' * 18 + 'MORRISTOWN, NEW JERSEY')
        custom_print('\n' * 3, end='')

        # Задаем случайные значения для L и G
        L = random.randint(1, 60)  # Случайная позиция чашки от 1 до 60
        while L == 1 or L == 60:  # Проверка, чтобы чашка не была на краю
            L = random.randint(1, 60)

        G = random.randint(1, 10)  # Случайное значение гравитации от 1 до 10

        # Печать информации об игре
        custom_print(f"THE CUP IS 30 LINES DOWN AND {L} SPACES OVER.")
        custom_print(f"THE PULL OF GRAVITY IS {G} LINES/SECOND/SECDND.")
        custom_print("WHAT IS THE PUSH YOU WOULD LIKE TO GIVE THE BALL")
        custom_print("ACROSS THE PAPER (IN SPACES/SECOND)? ", end='')

        T_input = custom_input()  # Используем кастомный input для чтения ввода
        try:
            T = float(T_input)
        except ValueError:
            custom_print("PLEASE ENTER A NUMBER.")
            continue  # Возврат в начало цикла для повторного ввода

        custom_print("THE RESULTS MAY TAKE ANYWHERE BETWEEN 30 AND 90 SECONDS.")

        # Инициализация массива S(1..30,1..60) для совместимости с индексами BASIC
        S = [[0] * 61 for _ in range(31)]  # Массив S[0..30][0..60], используем S[1..30][1..60]

        # Set cup position
        S[30][L] = 1
        S[30][L - 1] = 1
        S[30][L + 1] = 1
        S[29][L - 1] = 1
        S[29][L + 1] = 1

        # Initialize variables
        W = 0  # Variable for result
        Z = 1.0
        Z_max = ((60 * G) ** 0.5) / G

        # Main simulation loop
        while Z <= Z_max:
            Y = T * Z * 2
            X = G / 2 * Z ** 2

            if X > 30.5 or X < 0.5 or Y > 60.5 or Y < 0.5:
                break

            IX = int(X)
            IY = int(Y)

            # Check for hitting the cup
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

            # Mark the position of the ball in the array
            if 1 <= IX <= 30 and 1 <= IY <= 60:
                S[IX][IY] = 2

            # Erase previous positions to simulate motion
            if IY >= 6:
                for D in range(1, 6):  # D from 1 to 5
                    if IY - D >= 1:
                        S[IX][IY - D] = 0

            Z += 0.01

        # Restore the cup
        S[30][L] = 1
        S[30][L - 1] = 1
        S[30][L + 1] = 1
        S[29][L - 1] = 1
        S[29][L + 1] = 1

        # Output results
        P = " *."

        # We will print the trajectory first, then print the cup separately with a blank line in between
        custom_print()  # Add empty line before the trajectory

        # Print trajectory (excluding the cup)
        for X in range(1, 29):  # Up to line 28 (excluding cup at lines 29 and 30)
            # Check for non-zero elements in the row
            if all(S[X][Y] == 0 for Y in range(1, 61)):
                continue  # Move to next row if entire row is empty

            line_output = ''
            for Y in range(1, 61):
                line_output += P[S[X][Y]]
            custom_print(line_output.rstrip())

        custom_print()  # Add blank line before the cup

        # Print the cup (lines 29 and 30)
        for X in range(29, 31):
            # Fill with spaces to ensure the line is 60 characters long
            line_output = ''
            for Y in range(1, 61):
                line_output += P[S[X][Y]]
            custom_print(line_output.ljust(60))  # Ensure the line is exactly 60 characters long

        custom_print()  # Add blank line after the cup if needed

        # Check result and offer to play again
        if W == 1:
            custom_print("RIGHT IN!!!")
        elif W == 2:
            custom_print("YOU ALMOST DIDN'T MAKE IT, BUT IT BOUNCED IN.")
        else:
            custom_print("YOU MISSED; TRY AGAIN.")
            continue  # Start over

        custom_print("DO YOU WANT TO PLAY AGAIN?")
        A = custom_input()
        if A.strip().upper().startswith('Y'):
            continue  # Start over
        else:
            break  # End game


if __name__ == "__main__":
    main()
