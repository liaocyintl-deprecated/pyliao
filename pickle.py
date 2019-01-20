import pickle


def save_pickle(path, obj):
    with open(path, mode='wb') as f:
        pickle.dump(obj, f)


def load_pickle(path):
    with open(path, mode='rb') as f:
        return pickle.load(f)