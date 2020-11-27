from os import listdir

from majority_digraph import MajorityDigraph
from utils import read_json, read_and_parse_text


def test_json():
    path = 'profiles/json/'
    for file in listdir(path):
        file_path = path + file
        profile = read_json(file_path)
        save_file = "plots/json/normal/" + file.replace(".json", ".png")
        save_file_weighted = "plots/json/weighted/" + file.replace(".json", ".png")
        mj = MajorityDigraph(profile)
        mj.plot(False, save_file, show=False)
        mj.plot(True, save_file_weighted, show=False)


def test_txt():
    path = 'profiles/txt/'
    for file in listdir(path):
        file_path = path + file
        profile = read_and_parse_text(file_path)
        save_file = "plots/txt/normal/" + file.replace(".txt", ".png")
        save_file_weighted = "plots/txt/weighted/" + file.replace(".txt", ".png")
        mj = MajorityDigraph(profile)
        mj.plot(False, save_file, show=False)
        mj.plot(True, save_file_weighted, show=False)


test_json()
test_txt()
