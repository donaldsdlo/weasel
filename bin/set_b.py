# Initialize an empty set to hold unique lines from all files
set_a = set()

# Process C:\Users\donal\AppData\Roaming\Rime\zrm2000.dict.yaml
with open('C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dict.yaml', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines[52:]:  # Line number starts from 0, so subtract 1
        set_a.add(line)

# Process C:\Users\donal\AppData\Roaming\Rime\zrm2000.dicts files
files = [
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.sogou.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.tencent.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.animal.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.caijing.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.car.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.chengyu.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.diming.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.food.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.it.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.law.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.lishimingren.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.medical.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.thuocl.poem.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.user.dict.yaml',
        'C:\\Users\\donal\\AppData\\Roaming\\Rime\\zrm2000.dicts\\zrm2000.zhwiki.dict.yaml'
         ]
for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[33:]:  # Line number starts from 0, so subtract 1
            set_a.add(line)

# Initialize empty lists to hold unique and duplicate lines
list_a = []
list_duplicates = []

# Process F:\dicts\Sougou_dict_spider\data\zrm2000.super.dict.yaml.2.txt
with open('F:\\dicts\\Sougou_dict_spider\\data\\zrm2000.super.dict.yaml.2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines[33:]:  # Line number starts from 0, so subtract 1
        if line in set_a:
            list_duplicates.append(line)
        else:
            list_a.append(line)

# Write unique lines to F:\dicts\Sougou_dict_spider\data\zrm2000.super.dict.yaml.a.txt
with open('F:\\dicts\\Sougou_dict_spider\\data\\zrm2000.super.dict.yaml.a.txt', 'w', encoding='utf-8') as file:
    file.writelines(list_a)

# Append duplicate lines to F:\dicts\Sougou_dict_spider\data\duplicates.txt
with open('F:\\dicts\\Sougou_dict_spider\\data\\duplicates.txt', 'a', encoding='utf-8') as file:
    file.writelines(list_duplicates)