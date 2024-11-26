# Выполнение:
# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.
# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
# Создайте список названий файлов в соответствии с названиями файлов архива.
# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
# Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool.
# Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время
# выполнения и выведите его в консоль.
import multiprocessing
import threading
import time


def read_info(name):
    all_data = []
    name = 'file4.txt'
    filenames = [{name} for number in range(1, 5)]
    started = time.time()
    with open(name, encoding = 'utf-8') as file:

        for line in file:
            if not line:
                break
            else:
                all_data += line
    ended = time.time()
    elapsed = ended - started
    print(f'Время выполнения: {elapsed}')



thread = threading.Thread(target=read_info('file4.txt'))
thread.start()



if __name__ == '__main__':
    process = multiprocessing.Process(target=read_info('file4.txt'))
    process.start()
