# -*-coding:utf-8-*-
# 2018/06/01
# 刪除腳本注釋行、空，另存文件

import re,os,sys

path = os.getcwd()
# 空行和注釋
prog = re.compile(r'^ *#|^ *$') 

def main(file = sys.argv[1]):
    fel = file.split(".")
    row = [] 
    old_file_path = os.path.join(path,sys.argv[1])
    new_file_name = fel[0] + "_chane." + fel[1]
    new_file_path = os.path.join(path,new_file_name)

    with open(old_file_path,"r") as fp:
        for line in fp.readlines():
            if not prog.match(line):
                row.append(line)

    with open(new_file_path,"w") as f:
        f.writelines(row)

if __name__ == "__main__":
    main()
