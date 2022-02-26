import json
from http.client import HTTPConnection
from typing import List


def send_bulk_request(index_names_with_dates: List, data: dict):
    array_data = []

    for index_name in index_names_with_dates:
        index_metadata = {"create": {"_index": index_name}}

        array_data.append(json.dumps(index_metadata))
        array_data.append(json.dumps(data))

    data = "\n".join(array_data)
    data += "\n"

    connection = HTTPConnection(host="127.0.0.1", port=9200, timeout=45)
    connection.request(method="POST", url="_bulk", body=data, headers={"Content-Type": "application/json"})

    print(str(connection.getresponse().read()))
