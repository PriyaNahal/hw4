def allcaps(func):
    def wrapper():
        ans = func()
        return ans.upper()
    return wrapper



