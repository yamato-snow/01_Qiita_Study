# fortune.py
def get_fortune():
    from random import choice # randamではなく、randomなので注意です
    results = ['大吉', '吉', '小吉', '凶', '大凶', '末吉']
    return choice(results)