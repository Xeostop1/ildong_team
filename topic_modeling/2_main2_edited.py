import pandas as pd
import nltk
from nltk.corpus import stopwords

num = 10000

data = pd.read_csv('abcnews-date-text_%s.csv' % num, error_bad_lines=False)
print(len(data))
print(data.head(5))

text = data[['headline_text']]
print(text.head(5))
text2 = text.copy()
text2['headline_text'] = text.apply(lambda row: nltk.word_tokenize(row['headline_text']), axis=1)
print(text2.head(5))

stop = stopwords.words('english')
text3 = text2.copy()
text3['headline_text'] = text2['headline_text'].apply(lambda x: [word for word in x if word not in stop])
print(text3.head(5))

#표제어 추출(현재 동사로 통일)
from nltk.stem import WordNetLemmatizer
text4 = text3.copy()
text4['headline_text'] = text3['headline_text'].apply(lambda x: [WordNetLemmatizer().lemmatize(word, pos='v') for word in x])
print(text4.head(5))

#길이가 짧은 단어 제거
tokenized_doc = text4['headline_text'].apply(lambda x: [word for word in x if len(word) > 3])
print(tokenized_doc[:5])

#역토큰화 (토큰화 작업을 되돌림)
detokenized_doc = []
for i in range(len(text4)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)
text4['headline_text'] = detokenized_doc # 다시 text['headline_text']에 재저장
print(text4['headline_text'][:5])

from sklearn.feature_extraction.text import TfidfVectorizer
#vectorizer = TfidfVectorizer(stop_words='english', max_features=1000) # 상위 1,000개의 단어를 보존
vectorizer = TfidfVectorizer(stop_words='english', max_features=100) # 상위 100개의 단어를 보존
X = vectorizer.fit_transform(text4['headline_text'])

from sklearn.decomposition import LatentDirichletAllocation
lda_model = LatentDirichletAllocation(n_components=10, max_iter=1)
lda_top = lda_model.fit_transform(X)
terms = vectorizer.get_feature_names() # 단어 집합. 100개의 단어가 저장됨.


def get_topics(components, feature_names, n=10):
    for idx, topic in enumerate(components):
        topic_list = topic.argsort()
        topic_list2 = topic_list[:-(n+1):-1]
        print("\nTopic %d:" % (idx+1), end=' ')
        for i in topic_list2:
            print_tuple = (feature_names[i], topic[i].round(2))
            print(print_tuple, end='')
        #print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]])

get_topics(lda_model.components_, terms)
#components_ => 각 토픽에 대해 단어별 비율이 적혀있음

#n_componenets: topic 개수
#max_iter: The maximum number of iterations
'''
https://www.slideshare.net/ssuserf03d2b/lda-latent-dirichlet-allocation-fairies-nlp-series-korean-ver
online, batch: https://stickie.tistory.com/44
'''