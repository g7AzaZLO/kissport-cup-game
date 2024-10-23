def main():
    while True:
        # Print header
        print(' ' * 27 + 'CUP')
        print(' ' * 20 + 'CREATIVE COMPUTING')
        print(' ' * 18 + 'MORRISTOWN, NEW JERSEY')
        print('\n' * 3, end='')

        # Set constants for L and G
        L = 30  # Cup position
        G = 5   # Gravity

        # Print game information
        print(f"THE CUP IS 30 LINES DOWN AND  {L}  SPACES OVER.")
        print(f"THE PULL OF GRAVITY IS  {G}  LINES/SECOND/SECDND.")
        print("WHAT IS THE PUSH YOU WOULD LIKE TO GIVE THE BALL")
        print("ACROSS THE PAPER (IN SPACES/SECOND)? ", end='')  # Добавлен пробел после вопроса
        T_input = input()
        try:
            T = float(T_input)
        except ValueError:
            print("PLEASE ENTER A NUMBER.")
            continue  # Return to the beginning of the loop to re-input

        print("THE RESULTS MAY TAKE ANYWHERE BETWEEN 30 AND 90 SECONDS.")

        # Initialize array S(1..30,1..60) to match BASIC indexing
        S = [[0] * 61 for _ in range(31)]  # S[0..30][0..60], we'll use S[1..30][1..60]

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
        print()  # Add empty line before the trajectory

        # Print trajectory (excluding the cup)
        for X in range(1, 29):  # Up to line 28 (excluding cup at lines 29 and 30)
            # Check for non-zero elements in the row
            if all(S[X][Y] == 0 for Y in range(1, 61)):
                continue  # Move to next row if entire row is empty

            line_output = ''
            for Y in range(1, 61):
                line_output += P[S[X][Y]]
            print(line_output.rstrip())

        print()  # Add blank line before the cup

        # Print the cup (lines 29 and 30)
        for X in range(29, 31):
            # Fill with spaces to ensure the line is 60 characters long
            line_output = ''
            for Y in range(1, 61):
                line_output += P[S[X][Y]]
            print(line_output.ljust(60))  # Ensure the line is exactly 60 characters long

        print()  # Add blank line after the cup if needed

        # Check result and offer to play again
        if W == 1:
            print("RIGHT IN!!!")
        elif W == 2:
            print("YOU ALMOST DIDN'T MAKE IT, BUT IT BOUNCED IN.")
        else:
            print("YOU MISSED; TRY AGAIN.")
            continue  # Start over

        print("DO YOU WANT TO PLAY AGAIN?")
        A = input()
        if A.strip().upper().startswith('Y'):
            continue  # Start over
        else:
            break  # End game

if __name__ == "__main__":
    main()
