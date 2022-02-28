# Press the green button in the gutter to run the script.
import uuid
from typing import List
from random import choice
import string

from elasticsearch_client import send_bulk_request


def get_random_text(length=8, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])


def prepare_indexes_names(indexes_name, dates) -> List:
    final_indexes_names = []

    for index in indexes_name:
        for date in dates:
            final_indexes_names.append(index + ".logs-" + date)
    return final_indexes_names


def run():
    dates = ["2022.02.23", "2022.02.24", "2022.02.25", "2022.02.26", "2022.02.27", "2022.02.28"]

    indexes_name = ["customer1"]
    final_indexes_names = prepare_indexes_names(indexes_name, dates)

    data = {}
    for i in range(1, 20):
        data["key" + str(i)] = str(uuid.uuid4())
    send_bulk_request(final_indexes_names, data)

    indexes_name = ["customer4"]
    final_indexes_names = prepare_indexes_names(indexes_name, dates)

    data = {}
    for i in range(1, 20):
        data["key" + str(i)] = str(uuid.uuid4())
        data["text" + str(i)] = get_random_text(10, string.digits) + get_random_text(50, string.ascii_letters)
    send_bulk_request(final_indexes_names, data)

    indexes_name = ["customer5"]
    final_indexes_names = prepare_indexes_names(indexes_name, dates)

    data = {}
    for i in range(1, 50):
        data["key" + str(i)] = str(uuid.uuid4())
        data["text" + str(i)] = get_random_text(100, string.digits) + get_random_text(500, string.ascii_letters)
    send_bulk_request(final_indexes_names, data)


if __name__ == '__main__':
    run()
