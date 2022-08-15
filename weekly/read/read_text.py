
def read_text(group_path):
    f_all=''
    for f in group_path:
        data = open(f,encoding='utf-8')
        f_all=f_all+data.read()
    return f_all
