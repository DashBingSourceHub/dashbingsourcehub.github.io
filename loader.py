from requests import get

home_url = "https://dashbingsourcehub.github.io/"

def get_url(url:str):
    return(get(url).content.decode("utf-8"))

def main():
    print("欢迎使用Dash在线软件索引1.0版本")

if __name__ == "__main__":
    main()
