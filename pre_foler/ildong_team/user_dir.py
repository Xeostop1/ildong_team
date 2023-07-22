import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor
from soynlp.normalizer import *
import pandas as pd
from konlpy.tag import *
# from konlpy.tag import Kkma
import os
import warnings
warnings.simplefilter("ignore")

import konlpy



# okt = Okt()
mecab = Mecab()

#===파일경로 찾기: 이름때문에 오류===
# file_path="./ildong_team/youtube_coment.txt"
# if os.path.isfile(file_path):
#     print("파일 유")
# else:
#     print("무")

comment_file_path ="./ildong_team/youtube_coment.txt"
with open(comment_file_path, "r", encoding="utf-8") as file:
    comment = file.read()

co_morphs=mecab.morphs()
print(co_morphs)

# okt 사용 예제
# print('OKT 형태소 분석 :',okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print('OKT 품사 태깅 :',okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print('OKT 명사 추출 :',okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 





# urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename="2016-10-20.txt")

# # 훈련 데이터를 다수의 문서로 분리
# corpus = DoublespaceLineCorpus("2016-10-20.txt")
# len(corpus)

# word_extractor = WordExtractor()
# word_extractor.train(corpus)
# word_score_table = word_extractor.extract()

#반복되는 단어처리 
#자음, 모음 단일개체=emoticon_normalize
#반복 단어개체repeat_normalize("test",num_repeats=2)


# print(emoticon_normalize('앜ㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠ', num_repeats=2))
# print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠ', num_repeats=2))
# print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠㅠ', num_repeats=2))
# print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠㅠㅠㅠ', num_repeats=2))
