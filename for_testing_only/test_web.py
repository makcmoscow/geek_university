def countdown(n):
    def next():
        nonlocal n
        r = n
        n-=1
        return r
    return next

a = countdown(12)
while True:
    v = a()
    if not v:break
