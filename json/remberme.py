import json

filename = "username.json"

def get_newuser_name():
    """提示新用户输入name"""
    username = input("please input your name:")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username

def get_stored_name():
    """从文件读取username"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户"""
    username = get_stored_name()
    if username:
        print("welcome back, "+ username)
    else:
        username = get_newuser_name()
        print("we will rember your name when you back, " + username + " !")

greet_user()
