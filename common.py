import os























def get_all_folders(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]


try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


def get_hostname_from_url(url):
    parsed_uri = urlparse(url)
    return parsed_uri.hostname


def is_path_exists(path):
    return os.path.exists(path)


if __name__ == "__main__":
    print(get_hostname_from_url("http://docs.python.jp/2/library/urlparse.html"))
