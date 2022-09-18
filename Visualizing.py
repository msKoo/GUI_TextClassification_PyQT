import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns
import numpy

sns.set(font_scale=0.5)
plt.rcParams['font.family'] = 'AppleGothic'

def displayWordCloud(data = None, width=430, height=250):
    backgroundcolor = 'white'
    # width = 430
    # height = 250
    path = 'src/font/NanumGothic-Regular.ttf'
    wordcloud = WordCloud(font_path = path, stopwords = STOPWORDS,
                        background_color = backgroundcolor,
                        width = width, height = height).generate(data)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    # plt.show()

    wordcloud.to_file('./src/result/wordCloud/wordcloud_w'+str(width)+'.png')

    # plt.savefig('./src/result/wordCloud/img.png')

def displayWordCount(clean_train_reviews):
    train = pd.DataFrame()
    # 단어 수
    train['num_words'] = list(map(lambda x: len(str(x).split()), clean_train_reviews))
    # 중복을 제거한 단어 수
    train['num_unique_words'] = list(map(lambda x: len(set(str(x).split())), clean_train_reviews))

    plt.figure(figsize=(2, 1))
    fig, axes = plt.subplots()

    sns.distplot(train['num_words'], bins=100, ax=axes)
    sns.set(font_scale=3)
    axes.axvline(train['num_words'].median(), linestyle='dashed')  # axvline : 중간 점선 표현
    axes.set_xlabel('num_words', fontsize=8)
    axes.set_facecolor('white')

    plt.legend(labels=["word counts"], fontsize=15)
    plt.figure(figsize=(2, 1))
    fig, axes = plt.subplots()
    sns.distplot(train['num_unique_words'], bins=100, color='g', ax=axes)
    sns.set(font_scale=3)
    axes.axvline(train['num_words'].median(), linestyle='dashed')
    axes.set_xlabel('num_words', fontsize=8)
    axes.set_facecolor('white')

    plt.savefig('./src/result/seaborn/seaborn_numwords_unique.png', transparent=True)\

def dataGraph(clean_train_reviews):
    train = pd.DataFrame()
    train['num_words'] = list(map(lambda x: len(str(x).split()), clean_train_reviews))
    # 중복을 제거한 단어 수
    train['num_unique_words'] = list(map(lambda x: len(set(str(x).split())), clean_train_reviews))

    plt.figure(figsize=(2, 1))


    fig, axes = plt.subplots(ncols=2)
    fig.set_size_inches(3.5, 1.8)
    print('리뷰별 단어 평균 값 : ', train['num_words'].mean())
    print('리뷰별 단어 중간 값 : ', train['num_words'].median())
    sns.distplot(train['num_words'], bins=100, ax=axes[0])
    axes[0].axvline(train['num_words'].median(), linestyle='dashed')  # axvline : 중간 점선 표현
    axes[0].set_title('리뷰별 단어 수 분포')

    print('리뷰별 고유 단어 평균 값 : ', train['num_unique_words'].mean())
    print('리뷰별 고유 단어 중간 값 : ', train['num_unique_words'].median())
    sns.distplot(train['num_unique_words'], bins=100, color='g', ax=axes[1])
    axes[1].axvline(train['num_words'].median(), linestyle='dashed')
    axes[1].set_title('리뷰별 고유한 단어 수 분포')

    # plt.show()
    plt.savefig('./src/result/seaborn/seaborn_numword.png', transparent=True)

def displayResult():
    # y_loss = [2.4723, 2.1723, 2.0219, 1.904, 1.7993,1.7041, 1.6158,1.5331, 1.4556, 1.383]
    # 2.4615, 2.0226, 1.6938, 1.3925, 1.129, 0.9081, 0.7357, 0.6019, 0.5033, 0.4324]
    # y_vloss = [2.3873, 2.3022, 2.2651, 2.2424, 2.2442, 2.2504, 2.2576, 2.2779, 2.3189, 2.3518]
    # 2.4174, 2.4313, 2.5127, 2.6313, 2.7556, 2.8535, 2.9307, 2.9984, 3.053,3.0938]

    y_vloss = [0.13596169148484866, 0.10232374267478785, 0.09159363598103325, 0.08637172984133164,
                 0.09674505230680419, 0.09105636464593311, 0.09010037897935448, 0.09504081677481688,
                 0.09993200332935667, 0.10999317096428277]
    y_loss =  [0.2266461635907491, 0.09062119808826181, 0.0589320162879924, 0.04020388817155165, 0.027329568712951408,
             0.02126024063843199, 0.017342214744481155, 0.013346235364758307, 0.012164281833562482,
             0.009792077704742164]

    # 'val_accuracy': [0.95993334, 0.9709333, 0.9734667, 0.976, 0.9734, 0.9754, 0.9766, 0.9781333, 0.9758667, 0.9764]}

    plt.figure(figsize=(1.8, 0.8))
    x_len = numpy.arange(len(y_loss))
    plt.plot(x_len, y_vloss, marker='.', c='red', label="Validation-set Loss")
    plt.plot(x_len, y_loss, marker='.', c='blue', label="Train-set Loss")

    plt.legend(loc='upper right')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    # plt.show()

    plt.savefig('./src/result/loss.png', transparent=True)