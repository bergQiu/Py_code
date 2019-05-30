# condig:utf-8
# 2019/01/03
# 分析raspberry memory log

import re
def analysis(filename):
    with open(filename,'r') as f:
        for line in f.readlines():
            if "Mem" in line:
                content = re.split(' |--',line)
                # print(type(str(cont   ent)))
                if content[1][0:2] == '00':
                    print content[0]+','+content[3]+','+content[4]+','+content[5]
if __name__ == "__main__":
    file_ = "./free.log"
    analysis(file_)