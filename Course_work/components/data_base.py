import json


def data_base_load(path, mode='encoding="utf-8"'):
    with open(path, mode) as read_file_json:
        resp = json.load(read_file_json)

    return resp


def data_base_update(path, data):
    with open(path, 'w', encoding='utf-8') as read_file_json:
        read_file_json.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
