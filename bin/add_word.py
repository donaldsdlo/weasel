#取windows下的用户目录
import os
import sys
#user_dir = os.path.expanduser('~')
user_dir = os.getenv("APPDATA")

#打开用户目录下的Rime目录
rime_dir = os.path.join(user_dir, 'Rime')

#打开用户目录下的Rime目录下的dict.yaml文件
dict_file = os.path.join(rime_dir, 'zrm2000.dict.yaml')

#打开用户目录下的Rime目录下的user.dict.yaml文件
user_dict_file = os.path.join(rime_dir, 'zrm2000.super.dict.yaml')


#打开用户目录下的Rime目录下的symbols.yaml文件
my_dict_file = os.path.join(rime_dir,'zrm2000.my.dict.yaml')

if __name__ == '__main__':
    #读取命令行参数,第一个参数为中文,第二个参数为拼音
    if len(sys.argv) < 3:
        print('Usage: python add_word.py "中文" "拼音"')
        sys.exit(1)

    chinese = sys.argv[1]
    pinyin = sys.argv[2]
    #dict_file和user_dict_file中中文和拼音使用TAB或者空格分隔
    #判断中文在dict_file和user_dict_file中是否存在,如果存在则不需要添加到my_dict_file中
    found = False
    with open(dict_file, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split('\t')
            if len(words) == 2 and chinese == words[0]:
                found = True
                break
    if not found:
        with open(user_dict_file, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip().split('\t')
                if len(words) == 2 and chinese == words[0]:
                    found = True
                    break
    if not found:
        #如果中文不存在于dict,将中文和拼音以TAB分隔追加到my_dict_file中
        with open(my_dict_file, 'a', encoding='utf-8') as f:
            f.write(chinese + '\t' + pinyin + '\n')
            print('添加成功')
    else:
        print('词条已存在')
