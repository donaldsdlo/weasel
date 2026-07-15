import os

# 输入参数 字符串A
A = input("请输入字符串A: ")

# 文件路径
input_file_path = r"C:\Users\donal\AppData\Roaming\Rime\zrm2000.dicts\zrm2000.super.dict.yaml"
output_file_path = r"C:\Users\donal\AppData\Roaming\Rime\zrm2000.dicts\zrm2000.super.dict.yaml"

# 读取文件内容
if os.path.exists(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
else:
    print(f"文件 {input_file_path} 不存在")
    exit(1)

# 分割文件内容到list_a, list_b, list_c
list_a = lines[:34]
list_b = [line for line in lines[34:] if A in line]
list_c = [line for line in lines[34:] if A not in line]

# 合并list_a, list_b, list_c为一个列表
output_lines = list_a + list_b + list_c

# 写入到新文件中
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(output_lines)

print("处理完成，已按要求输出到新文件中。")
