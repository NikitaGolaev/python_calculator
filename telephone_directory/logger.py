def export_logger(data):
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{data}\n')
