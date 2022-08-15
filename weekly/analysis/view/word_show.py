import matplotlib.pyplot as plt     #图像展示库  pip install matplotlib

def word_show(wc):
    plt.imshow(wc)      #显示词云
    plt.axis('off')     #关闭坐标轴
    plt.show()          #显示图像