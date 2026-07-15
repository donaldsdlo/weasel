import opencc
import glob
import os

def convertT2S(inputFile, outputFile):
    # 初始化opencc转换器
    converter = opencc.OpenCC('t2s')
    
    # 初始化line_out列表
    line_out = []
    
    # 打开输入文件
    with open(inputFile, 'r', encoding='utf-8') as file:
        for line_in in file:
            try:
                # 尝试将line_in转换为简体中文
                line_out.append(converter.convert(line_in))
            except Exception as e:
                # 如果转换失败，保留原始文本
                line_out.append(line_in)
                print(f"转换错误: {e}")
                
    # 写入输出文件
    with open(outputFile, 'w', encoding='utf-8') as file:
        for line in line_out:
            file.write(line)
            #file.write('\n')  # 添加换行符

# 调用函数
#convertT2S(r'C:\Users\donal\AppData\Roaming\Rime\zrm2000.dicts\zrm2000.super.dict.yaml', r'C:\Users\donal\AppData\Roaming\Rime\zrm2000.dicts\zrm2000.super.dict.yaml.out')

# 定义遍历文件夹并处理文件的函数
def process_yaml_files(folder_path):
    # 遍历指定文件夹下的所有以.yaml结尾的文件
    for filename in glob.glob(os.path.join(folder_path, '*.yaml')):
        # 构建输出文件的路径
        output_path = filename.replace('.yaml', '.out')
        
        # 调用convertT2S函数处理文件
        convertT2S(filename, output_path)
        
        print(f"处理完成: {filename} -> {output_path}")

# 调用函数处理文件
process_yaml_files('C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts')