import os

# 定义路径和文件名
base_path = "C:\\Users\\donal\\AppData\\Roaming\\Rime\\"
dict_file = "zrm2000.dict.yaml"
dicts_directory = "zrm2000.dicts"
output_directory = "C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\t\\"

# 确保输出目录存在
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 要处理的文件列表
dict_files = [
    # ... (如之前所列的文件列表)
    "zrm2000.thuocl.animal.dict.yaml",
    "zrm2000.thuocl.caijing.dict.yaml",
    "zrm2000.thuocl.car.dict.yaml",
    "zrm2000.thuocl.chengyu.dict.yaml",
    "zrm2000.thuocl.diming.dict.yaml",
    "zrm2000.thuocl.food.dict.yaml",
    "zrm2000.thuocl.it.dict.yaml",
    "zrm2000.thuocl.law.dict.yaml",
    "zrm2000.thuocl.lishimingren.dict.yaml",
    "zrm2000.thuocl.medical.dict.yaml",
    "zrm2000.thuocl.poem.dict.yaml",
    "zrm2000.zhwiki.dict.yaml",
    "zrm2000.tencent.dict.yaml",
    "zrm2000.sogou.dict.yaml",
    "zrm2000.user.dict.yaml",
]


# 从特定行开始读取文件的函数
def read_from_line(file_path, start_line):
    with open(file_path, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i >= start_line - 1:  # 调整为从第start_line行开始
                yield line.strip()


# 读取主词典文件的第53行到文件结尾，并存入集合seta
seta = set(read_from_line(os.path.join(base_path, dict_file), 53))

# 处理每个文件
for filename in dict_files:
    listb = []
    # 读取当前文件的第34行到结尾
    for line in read_from_line(os.path.join(base_path, dicts_directory, filename), 34):
        # 如果此行不在seta中，则添加到listb和seta
        if line not in seta:
            listb.append(line)
            seta.add(line)

    # 如果listb不为空，则保存文件的前33行加上listb的内容
    if listb:
        with open(
            os.path.join(base_path, dicts_directory, filename), "r", encoding="utf-8"
        ) as file:
            lines = file.readlines()
            first_33_lines = "".join(lines[:33])

        with open(
            os.path.join(output_directory, filename), "w", encoding="utf-8"
        ) as file:
            file.write(first_33_lines)
            file.write("\n".join(listb))
