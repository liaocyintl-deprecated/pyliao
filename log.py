import datetime


def current_datetime():
    return str(datetime.datetime.now())


def write(str, path = "run.log"):
    f = open(path, 'a')
    str += " " + current_datetime()
    f.write(str + "\n")
    f.close()


def write_with_print(self, str):
    str += " " + current_datetime()
    print(str)
    write(str + "\n")

if __name__ == "__main__":
    write("test", "test/run.log")