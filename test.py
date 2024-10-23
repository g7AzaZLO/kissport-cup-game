# test_cup.py

import subprocess
import time
import sys

def process(command):
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True,
        universal_newlines=True
    )

def read_until(proc, prompt):
    """Читает вывод процесса до появления заданного промпта."""
    output = ''
    while True:
        char = proc.stdout.read(1)
        if not char:
            break
        output += char
        if output.endswith(prompt):
            break
    return output

def write_input(proc, text):
    """Передает ввод процессу."""
    proc.stdin.write(f'{text}\n')
    proc.stdin.flush()

def test():
    print("Запуск процессов...")
    try:
        # Команды для запуска программ
        bas_cmd = 'cup_norm.bas'
        py_cmd = 'python cup_norm.py'

        # Запуск процессов
        bas_proc = process(bas_cmd)
        py_proc = process(py_cmd)

        # Ожидание приветствия
        bas_output = read_until(bas_proc, "ACROSS THE PAPER (IN SPACES/SECOND)")
        py_output = read_until(py_proc, "ACROSS THE PAPER (IN SPACES/SECOND)")

        # Сравнение приветствий
        if bas_output != py_output:
            print("Различия в приветствии:")
            print("BASIC вывод (с отображением спецсимволов):")
            print(repr(bas_output))  # Вывод с отображением спецсимволов
            print("Python вывод (с отображением спецсимволов):")
            print(repr(py_output))  # Вывод с отображением спецсимволов
            print("Тест провален.")
            return
        else:
            print("Приветствия совпадают. [+] ТЕСТ 1 - ПРОЙДЕН")

        # Вводим значение T
        T_value = '4.5'  # Вы можете изменить значение по своему усмотрению

        write_input(bas_proc, T_value)
        write_input(py_proc, T_value)

        # Ожидание следующего вывода
        bas_output += read_until(bas_proc, "DO YOU WANT TO PLAY AGAIN?")
        py_output += read_until(py_proc, "DO YOU WANT TO PLAY AGAIN?")

        # Сравнение остального вывода
        if bas_output != py_output:
            print("Различия в выводе после ввода значения T:")
            print("BASIC вывод (с отображением спецсимволов):")
            print(repr(bas_output))  # Вывод с отображением спецсимволов
            print("Python вывод (с отображением спецсимволов):")
            print(repr(py_output))  # Вывод с отображением спецсимволов
            print("Тест провален.")
            return
        else:
            print("Выводы совпадают после ввода значения T. [+] ТЕСТ 2 - ПРОЙДЕН")

        # Вводим ответ на вопрос о повторной игре
        replay_answer = 'N'  # Или 'Y' для продолжения

        write_input(bas_proc, replay_answer)
        write_input(py_proc, replay_answer)

        # Ожидаем завершения процессов
        bas_proc.communicate()
        py_proc.communicate()

        print("Тест успешно пройден. Выводы обеих программ совпадают.")

    except Exception as ex:
        print(f"Тест завершился с ошибкой: {ex}")

if __name__ == "__main__":
    test()
