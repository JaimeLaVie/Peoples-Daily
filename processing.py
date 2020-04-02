# -*- coding: utf-8 -*-
import os
import thulac
thuseg = thulac.thulac(seg_only=True, filt = False)

filedir = os.getcwd()+'/data'
filenames = os.listdir(filedir)
stopwords = ['，', '的', '。', '、', '：', '和', '在', '朝鲜', '中国', '中', '朝', '国', '了', '是', '“', '”', '为']

def words_frequency(inputfile, outputfile1, outputfile2, stopwords):
    # 获得词频
    wordlist = inputfile.split()
    counted_words = []
    words_count = {}
    for i in range(len(wordlist)):
        if wordlist[i] not in counted_words:
            counted_words.append(wordlist[i])
            words_count[wordlist[i]] = 1
            for j in range(i+1, len(wordlist)):
                if wordlist[i] == wordlist[j]:
                    words_count[wordlist[i]] += 1
    # 合并词与对应频数
    words = []
    counts = []
    for items in words_count:
        words.append(items)
        counts.append(words_count[items])
    combined = list(zip(words, counts))
    # 冒泡法排大小，获得未去除停用词的词频表
    for k in range(len(combined)-1):
        for i in range(len(combined)-1):
            if combined[i][1] < combined[i+1][1]:
                variable = combined[i]
                combined[i] = combined[i+1]
                combined[i+1] = variable
    with open ("{}.txt".format(outputfile1), "w") as file:
        file.write(str(combined))
    # 去除停用词后的词频表
    combined_no_stopwords = []
    for n in range(len(combined)):
        if combined[n][0] in stopwords:
            continue
        combined_no_stopwords.append(combined[n])
    with open ("{}.txt".format(outputfile2), "w") as file:
        file.write(str(combined_no_stopwords))

text_all = ''
for filename in filenames:
    filepath = filedir + '/' + filename
    # print (filepath)
    with open (filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        text = thuseg.cut(text, text=True)
        text_all += text

words_frequency(text_all, 'words_frequency_original', 'words_frequency_no_stopwords', stopwords)

""" with open ('text_all.txt', 'w') as file:
    file.write(text_all) """