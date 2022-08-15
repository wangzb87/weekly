import wordcloud    #词云展示库，pip install wordcloud

def word_cloud(word_counts):
    wc = wordcloud.WordCloud(background_color="black",  # 设置背景颜色
               max_words=200,  # 设置最大显示的字数
               font_path="Hiragino Sans GB.ttc",  # 设置中文字体，词云默认字体是“DroidSansMono.ttf字体库”，不支持中文
               max_font_size=50,  # 设置字体最大值
               random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
               )
    wc.generate_from_frequencies(word_counts)   #从字典生成词云
    return wc