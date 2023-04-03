import json
import config


def read_json(filename):
    filepath = config.file_path("data") + filename

    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def get_data(filename):
    arr = []
    # 读取json文件
    datas = read_json(filename)
    # 调用value()方法 获取json数据的value值，再进行遍历
    for data in datas.values():
        arr.append((data["time_begin"],
                    data["time_end"],
                    data["select"],
                    data["loc_01"],
                    data["loc_02"],
                    data["loc_03"],
                    data["loc_04"]))

    return arr



