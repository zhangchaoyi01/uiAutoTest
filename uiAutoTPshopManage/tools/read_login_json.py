import json
import config


def read_json(filename):
    filepath = config.file_path("data") + filename

    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def get_data():
    arr = []
    # 读取json文件
    datas = read_json("login.json")
    # 调用value()方法 获取json数据的value值，再进行遍历
    for data in datas.values():
        arr.append((data["username"],
                    data["password"],
                    data["verify_code"],
                    data["expect_result"],
                    data["success"]))
    return arr



