# 50G文件 一行，分隔符{|}
def myreadline(f,newline):
    buf = ""
    while True:
        while newline in buf:
            pos =buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk

with open("input.txt") as f:
    for line in myreadline(f,"|"):
        print(line)


# 一行一行是没问题的
# f = open()
#     for line in f:
#         print(line)