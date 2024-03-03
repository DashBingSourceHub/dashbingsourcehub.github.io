from requests import get
from json import loads

builtin_version = (1,0,0,"")
version = "v%d.%d.%d %s"%builtin_version
home_url = "https://dashbingsourcehub.github.io/"
py_url = home_url + "py/"

class DswStdlib:
    version = version
    builtin_version = builtin_version
    home_url = home_url
    py_url = py_url

value_global = {"DswStdlib":DswStdlib}

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

def printc(char, text):
    print(char, text, "\033[0;37m")

def inputc(char, text):
    print(char, end="")
    return(input(text+"\033[0;37m"))

def get_url (url):
    try:
        return(get(url).content.decode("utf-8"))
    except:
        printc("\033[1;31m", "[错误] 网络异常")
        return(None)

get_onlpy = get_url

def pkg_have(pkg_name):
    try:
        __import__(pkg_name)
    except:
        return(False)
    else:
        return(True)

def main():
    print(title%version)
    pkg_list = {}
    while True:
        print(func_list)
        s = inputc("\033[1;32m", "?> ")
        if s == "1":
            try:
                pkg_list = loads(get_onlpy(home_url+"index_py.json"))
                pkg_list = sorted(pkg_list)
                for i in pkg_list:
                    printc("\033[1;32m", i)
            except:
                printc("\033[1;31m", "[错误] 加载程序运行出错")
        elif s == "2":
            try:
                pkg_list = loads(get_onlpy(home_url+"index_py.json"))
                m = inputc("\033[1;32m", "请输入软件包名称 ?> ")
                if m in pkg_list:
                    temp_values = {}
                    temp_reqs = []
                    for i in pkg_list[m]["req"]:
                        if not pkg_have(i):
                            temp_reqs.append(i)
                    if len(temp_reqs) == 0:
                        try:
                            exec(get_onlpy(py_url+pkg_list[m]["name"]), value_global, temp_values)
                        except:
                            printc("\033[1;31m", "[错误] 程序运行时出错，请联系负责人")
                    else:
                        printc("\033[1;31m", "[错误] 缺少以下依赖库：")
                        for i in temp_reqs:
                            printc("\033[1;31m", i)
                else:
                    printc("\033[1;31m", "[错误] 软件包不存在")
            except:
                printc("\033[1;31m", "[错误] 加载程序运行出错")
        elif s.upper() == "E":
            exit()
        else:
            printc("\033[1;31m", "[错误] 未知的命令“%s”"%s)

main()
