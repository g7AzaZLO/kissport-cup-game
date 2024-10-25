import random


def main():
    while True:
        # Print header
        print(' ' * 27 + 'CUP')
        print(' ' * 20 + 'CREATIVE COMPUTING')
        print(' ' * 18 + 'MORRISTOWN, NEW JERSEY')
        print('\n' * 3, end='')

        L = random.randint(1, 60)
        while L == 1 or L == 60:
            L = random.randint(1, 60)

        G = random.randint(1, 10)

        # Print game information
        print(f"THE CUP IS 30 LINES DOWN AND {L} SPACES OVER.")
        print(f"THE PULL OF GRAVITY IS {G} LINES/SECOND/SECDND.")
        print("WHAT IS THE PUSH YOU WOULD LIKE TO GIVE THE BALL")
        print("ACROSS THE PAPER (IN SPACES/SECOND)? ", end='')
        T_input = input()
        try:
            T = float(T_input)
        except ValueError:
            print("PLEASE ENTER A NUMBER.")
            continue

        print("THE RESULTS MAY TAKE ANYWHERE BETWEEN 30 AND 90 SECONDS.")

        # Initialize array S(1..30,1..60) to match BASIC indexing
        S = [[0] * 61 for _ in range(31)]  # S[0..30][0..60], we'll use S[1..30][1..60]

        # Set cup position
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
        A = input()
        if A.strip().upper().startswith('Y'):
            continue
        else:
            break


if __name__ == "__main__":
    main()
