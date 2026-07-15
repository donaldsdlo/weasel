import os

# 文件路径
input_file_path = r"F:\dicts\Sougou_dict_spider\data\zrm2000.super.dict.yaml.a.txt"
output_file_path = r"F:\dicts\Sougou_dict_spider\data\zrm2000.super.dict.yaml.a.txt.out"

# 读取文件内容
if os.path.exists(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
else:
    print(f"文件 {input_file_path} 不存在")
    exit(1)

# 分割文件内容到list_a和set_a
#list_a = lines[:34]
set_a = set(lines)

# 将list_a和set_a中的数据合并为一个列表
#output_lines = list_a + sorted(set_a)
output_lines = sorted(set_a)
# 写入到新文件中
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(output_lines)

print("处理完成，已按要求输出到新文件中。")
