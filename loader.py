from requests import get
from json import loads

version = "v1.0.0"
home_url = "https://dashbingsourcehub.github.io/"
py_url = home_url + "py/"

title = '''\033[1;32m ____            _   \033[1;31m     ____         __ _
\033[1;32m|  _ \  __ _ ___| |__ \033[1;31m   / ___|  ___  / _| |___      ____ _ _ __ ___
\033[1;32m| | | |/ _` / __| '_ \ \033[1;31m  \___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \\
\033[1;32m| |_| | (_| \__ \ | | | \033[1;31m  ___) | (_) |  _| |_ \ V  V / (_| | | |  __/
\033[1;32m|____/ \__,_|___/_| |_| \033[1;31m |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|\033[0;37m

\033[1;32mDash\033[1;31mSoftware\033[1;33m 在线软件加载器 \033[1;35m%s\033[0;37m
'''

func_list = '''\033[1;32m _______________________
\033[1;32m/\\                       \\
\033[1;32m\\_|      \033[1;31m功能列表:\033[1;32m        |
\033[1;32m  | \033[1;33m输入1: 查询所有软件包\033[1;32m |
\033[1;32m  |   \033[1;33m输入2: 加载程序\033[1;32m     |
\033[1;32m  |   \033[1;33m输入E: 退出程序\033[1;32m     |
\033[1;32m  |   ____________________|_
\033[1;32m   \\_/______________________/\033[0;37m'''

value_global = {}

def printc(char, text):
    print(char, text, "\033[0;37m")

def inputc(char, text):
    print(char, end="")
    return(input(text+"\033[0;37m"))

def get_url(url:str):
    return(get(url).content.decode("utf-8"))

def main():
    print(title%version)
    pkg_list = {}
    while True:
        print(func_list)
        s = inputc("\033[1;32m", "?> ")
        if s == "1":
            try:
                pkg_list = loads(get_url(home_url+"index_py.json"))
                for i in pkg_list:
                    printc("\033[1;32m", i)
            except:
                printc("\033[1;31m", "[错误] 网络异常")
        elif s == "2":
            try:
                pkg_list = loads(get_url(home_url+"index_py.json"))
                m = inputc("\033[1;32m", "请输入软件包名称 ?> ")
                if m in pkg_list:
                    temp_values = {}
                    exec(get_url(py_url+pkg_list[m]), value_global, temp_values)
                else:
                    printc("\033[1;31m", "[错误] 软件包不存在")
            except:
                printc("\033[1;31m", "[错误] 网络异常")
        elif s.upper() == "E":
            exit()
        else:
            printc("\033[1;31m", "[错误] 未知的命令“%s”"%s)

main()
