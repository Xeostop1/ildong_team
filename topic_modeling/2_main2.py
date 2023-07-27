import pandas as pd
import nltk
from nltk.corpus import stopwords

# data = pd.read_csv('./topic_modeling/abcnews-date-text_10000.csv', error_bad_lines=False)
data = pd.read_csv('./topic_modeling/abcnews-date-text_10000.csv')
print(len(data))
#맨위의 데이터 5개만 보기 간단하게 빨리 볼 수 있게 세팅
print(data.head(5))

#출판일은 필요없어(DMR에서만 사용가능해서 필요없음)
text = data[['headline_text']]
print(text.head(5))
text2 = text.copy()
#행단위로 집계하기 위해  axis=1 사용 
#apply 행또는 열또는 전체 원소에 대해 특정연산을 사용 할 때 사용하는 함수 
text2['headline_text'] = text.apply(lambda row: nltk.word_tokenize(row['headline_text']), axis=1)
print(text2.head(5))

#불용어 제거(스탑워즈) 전치사등 
stop = stopwords.words('english')
text3 = text2.copy()
text3['headline_text'] = text2['headline_text'].apply(lambda x: [word for word in x if word not in stop])
print(text3.head(5))

#표제어 추출(현재 동사로 통일)
from nltk.stem import WordNetLemmatizer
text4 = text3.copy()
#품사만 가져오기 
text4['headline_text'] = text3['headline_text'].apply(lambda x: [WordNetLemmatizer().lemmatize(word, pos='v') for word in x])
print(text4.head(5))

#길이가 짧은 단어 제거
tokenized_doc = text4['headline_text'].apply(lambda x: [word for word in x if len(word) > 3])
print(tokenized_doc[:5])

#역토큰화 (토큰화 작업을 되돌림)
#길이가 짧은 단어를 제거하기 위해 토큰화 했던 작업을 다시 돌리기 위한 역토큰화 작업수 
detokenized_doc = []
for i in range(len(text4)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)
text4['headline_text'] = detokenized_doc # 다시 text['headline_text']에 재저장
print(text4['headline_text'][:5])

#1000개의 단어를 가지고 행렬 만들기 위해 TF-IDF 행렬 생성
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000) # 상위 1,000개의 단어를 보존
X = vectorizer.fit_transform(text4['headline_text'])

from sklearn.decomposition import LatentDirichletAllocation
#토픽의 개수 n_components
lda_model = LatentDirichletAllocation(n_components=10, max_iter=1)
lda_top = lda_model.fit_transform(X)
terms = vectorizer.get_feature_names() # 단어 집합. 1,000개의 단어가 저장됨.



#토픽이 나왔는데 주제가 잘 보인다면 토픽을 줄이고 알파베타를 조정할 필요가 있음 
def get_topics(components, feature_names, n=10):
    for idx, topic in enumerate(components):
        topic_list = topic.argsort()
        #print(topic_list)
        topic_list2 = topic_list[:-(n+1):-1]
        print("\nTopic %d:" % (idx+1), end=' ')
        for i in topic_list2:
            print_tuple = (feature_names[i], topic[i].round(2))
            print(print_tuple, end='')
            #a=12345679
            #[:-n - 1:-1] 뒤에서부터 가져올려고 -1 슬라이딩했음 np,의 argsort() /[start/.end/빈도]
        #print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]])

get_topics(lda_model.components_, terms)


#n_componenets: topic 개수
# preplexity: 혼란도 토픽개수를 늘리면 감소하는 경향  
# 값이 작을 수록 토픽모델이 실제로 잘 보이는 경향성이 존재
# topic conherence 실제로 해석하기에 적합한 평가 척도를 만들기위한 척도 
#max_iter: The maximum number of iterations
'''
https://www.slideshare.net/ssuserf03d2b/lda-latent-dirichlet-allocation-fairies-nlp-series-korean-ver
online, batch: https://stickie.tistory.com/44
'''