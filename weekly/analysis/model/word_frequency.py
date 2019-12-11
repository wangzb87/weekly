import collections  #词库统计库，自带模块

def word_frequency(object_list):
    word_counts = collections.Counter(object_list)  #对分词做词频统计
    # word_counts_top = word_counts.most_common(80) #获取前80最高频的词
    return word_counts