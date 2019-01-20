import json
import numpy as np

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

def save_json(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, cls=MyEncoder)


def load_json(path, encoding="utf-8"):
    with open(path, encoding=encoding) as data_file:
        return json.load(data_file)

def load_file(path):
    f = open(path)
    data = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    return data

def save_file(path, text):
    f = open(path, 'w')  # 書き込みモードで開く
    f.write(text)
    f.close()

def save_file_add(path, text):
    f = open(path, 'a')  # 追加モードで開く
    f.write(text)
    f.close()

def load_csv(path):
    f = open(path)
    lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    lines = [line.replace("\n", "") for line in lines]
    return [line.split(",") for line in lines]

def load_lines(file):
    f = open(file)
    lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    return [a.replace("\n", "") for a in lines]

if __name__ == "__main__":
    save_json("test/test.json", {"file":"test"})
    j = load_json("test/test.json")
    print(j)