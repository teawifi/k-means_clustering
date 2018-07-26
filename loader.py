from os import listdir
from os.path import isfile, join
from settings import ENCODING
import re
import pandas as pd


def load_data(path_to_dir):
    """
    Data loading

    :param path_to_dir: path to directory that contains files
    :return:            list of string
    """

    data = []
    files = [file for file in listdir(path_to_dir)
             if isfile(join(path_to_dir, file)) and file.endswith(".txt")]

    for file in files:
        with open(join(path_to_dir, file), "r", encoding=ENCODING) as f:
            content = f.read().split('\n')
            data.extend(content)

    filtered_data = []
    for item in data:
        filtered_data.append(filter_data(item))

    return filtered_data


def filter_data(data):
    pattern = "[0-9]+"
    strings = re.findall(pattern, data)
    numbers = [float(i) for i in strings]

    return numbers[:3]


def save_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding=ENCODING, header=['x', 'y', 'z'])

