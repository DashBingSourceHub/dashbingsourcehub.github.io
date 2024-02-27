from requests import get
from json import loads

home_url = "https://dashbingsourcehub.github.io/"
py_url = home_url + "py/"

def get_url(url:str):
    return(get(url).content.decode("utf-8"))

def main():
    print("欢迎使用Dash在线软件索引1.0版本")
    pkg_list = loads(get_url(home_url+"index_py.json"))
    exec(get_url(py_url+pkg_list[input("口令: ")]), {}, {})

main()
