# 文件路径
input_file_path = r"F:\dicts\Sougou_dict_spider\data\zrm2000.super.dict.yaml.a.txt"
output_file_path = r"F:\dicts\Sougou_dict_spider\data\zrm2000.super.dict.yaml.a.txt"

# 读取文件内容
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 复制前34行
first_34_lines = lines[:34]

# 对剩余的行进行排序，长度大的排在后面
#sorted_lines = sorted(lines[34:], key=len, reverse=True)
sorted_lines = sorted(lines[34:])
# 合并两部分内容
output_lines = first_34_lines + sorted_lines

# 写入到新文件中
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(output_lines)

print("处理完成，已按要求输出到新文件中。")
