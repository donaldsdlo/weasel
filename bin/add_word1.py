import os
import json
import pypinyin
from pypinyin import pinyin, Style

# import yaml


def get_home_dir():
    # 获取用户的主目录
    home_dir = os.path.expanduser("~")
    return home_dir


def process_file(file_path, set_a):
    # 处理文件中的每一行
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # print(line)
            if not line.startswith("#"):
                words = line.split()
                # print(words)
                if len(words) > 0:
                    set_a.add(words[0])


def convert_to_double_pinyin(pinyin_str, mapping):
    # 使用自然码双拼的对照转换拼音
    double_pinyin = ""
    for pinyin in pinyin_str.split():
        for key, value in mapping.items():
            if pinyin in key:
                double_pinyin += value
                break
    return double_pinyin


def main():
    # 获取用户的主目录
    # home_dir = get_home_dir()
    home_dir = "C:\\Users\\donal\\AppData\\Roaming\\rime"
    # 定义集合set_all
    set_all = set()

    # 读取home_dir下的zrm2000.dict.yaml文件
    file_path = os.path.join(home_dir, "zrm2000.dict.yaml")
    process_file(file_path, set_all)

    # 读取home_dir下的子目录zrm2000.dicts下的所有yaml文件
    subdir_path = os.path.join(home_dir, "zrm2000.dicts")
    # subdir_path = 'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts'

    for filename in os.listdir(subdir_path):
        print("read {filename} to memory", filename)
        if filename.endswith(".yaml"):
            file_path = os.path.join(subdir_path, filename)
            process_file(file_path, set_all)

    # print("length:",len(set_all))
    # print(set_all)
    while True:
        # 获取用户输入的字符串
        str_a = input("请输入简体中文字符串参数 str_a: ")
        if str_a == "quit":
            break
        # if "罗振铎" in set_all:
        #     print(" 这是个致命错误 ")
        # 检查str_a是否已经在词库中
        if str_a in set_all:
            print(f"{str_a} 已经在词库中。")
        else:
            # 转换str_a的拼音
            # pinyin_str = ' '.join(pypinyin.pinyin(str_a, style=pypinyin.Style.NORMAL))
            pinyin_str = " ".join(
                [" ".join(pinyin) for pinyin in pinyin(str_a, style=Style.NORMAL)]
            )
            # 读取ziranma_mapping.json文件
            ziranma_mapping_file = os.path.join(subdir_path, "ziranma_mapping.json")
            with open(ziranma_mapping_file, "r", encoding="utf-8") as file:
                mapping = json.load(file)

            # 将拼音转换为双拼
            shuangpin_str = convert_to_double_pinyin(pinyin_str, mapping)

            # 将结果追加到home_dir/zrm2000.dicts/zrm2000.user.dict.yaml文件中
            user_dict_path = os.path.join(subdir_path, "zrm2000.user.dict.yaml")

            with open(user_dict_path, "a", encoding="utf-8") as file:
                file.write(str_a)
                file.write("\t")
                file.write(shuangpin_str)
                file.write("\n")


main()
