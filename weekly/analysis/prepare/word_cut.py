import jieba        #结巴分词
def word_cut(string_data):
    seg_list_exact = jieba.cut(string_data,cut_all=False)   #精确模式分词
    object_list = []
    remove_words = [u'的',u'，',u'。',u'“',u'”',u'能',u'如果',u'通常',u'我们',u'需要',u'随着',u' ',u'在',u'了',u'、',u'是',u'上',u'有',u'从']      #自定义去除词库
    
    for word in seg_list_exact: #循环读出每个分词
        if word not in remove_words:    #如果不在去除词库中
            object_list.append(word)    #分词追加到列表
    return object_list