import re       #正则表达式  自带模块
def prepare_text(string_data):
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  #定义正则表达式匹配模式
    string_data = re.sub(pattern,'',string_data)        #将符合模式的字符去除
    return string_data