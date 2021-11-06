import os

from krwordrank.sentence import summarize_with_sentences
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from .txttodic import *
import sys



def summary_convert(file_name):
    # 개인 경로로 하세요
    stt_path = "stt/"  # stt 파일 폴더
    save_keyword_path = 'keyword/' # 키워드 저장 위치
    save_summary_path = "summary/"  # 요약된 문장 위치
    save_image_path = "media/image/"  # 키워드 wordCloud 저장

    # stopwords와 dacayingfacotr 수정
    stop_words_path = 'quickstart/'  # stopwords 파일
    decaying_factor_path = 'quickstart/'  # 가중치를 더 줄 파일

    # WordCloud 초기화
    font_path = 'NanumGothic.ttf'

    krwordrank_cloud = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white"
    )

    # 거를 글자들 리스트
    stop_words_file = open(stop_words_path + "summarised_stopwords.txt", "r", encoding="UTF8")
    stop_words = {''}
    stop_words_list = stop_words_file.read().split('\n')
    for s in stop_words_list:
        stop_words.add(s)
    stop_words_file.close()

    # 가중치를 더 줄 글자들 리스트
    decaying_factor = to_dict(decaying_factor_path + 'summarised_keywords.txt')

    fig = plt.figure(figsize=(50, 50))

    sents = []

    stt_file = open(stt_path + file_name + ".txt", "r", encoding="UTF8")
    contents = stt_file.read().strip()
    contents = contents.split(". ")
    for j in range(len(contents)):
        contents[j] = contents[j].replace("\r\n", "")
        contents[j] = contents[j].replace("\n", "")

    # 코사인 벡터값이 제일 높은 문장 15개 저장
    keywords, sents = summarize_with_sentences(
        contents,
        # penalty=penalty,
        stopwords=stop_words,
        diversity=0.3,
        num_keywords=100,
        num_keysents=15,
        verbose=False,
        bias=decaying_factor,
        beta=0.3
    )

    file = open(save_keyword_path + file_name + '.txt', "w", encoding="UTF8")
    for word, r in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:100]:
        print('%8s:\t%.4f' % (word, r))
        file.write(word + '\n')

    print('-----------------\n\n\n')

    file = open(save_summary_path + file_name + '.txt', "w", encoding="UTF8")
    for s in sents:
        print(s)
        file.write(s + '\n')
    print('-----------------\n\n\n')
    file.close()

    krwordrank_cloud = krwordrank_cloud.generate_from_frequencies(keywords)

    plt.imshow(krwordrank_cloud, interpolation="bilinear")

    fig.savefig(save_image_path + file_name + '.png', bbox_inches='tight')


