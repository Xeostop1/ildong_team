import MeCab
import pandas as pd
from collections import Counter
from statistics import mode


def top_n_words(text: str, n: int) -> list[tuple[str, int]]:
    words = text.split()
    counter = Counter(words)
    return counter.most_common(n)


def pos_filter(text: str, target_pos: list[str]) -> str:
    mecab = MeCab.Tagger(
        'C:\\Users\\coms\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\mecab-0.996-ko-0.9.2\\mecab-ko-dic')
    mecab.parse("")  # 버그로 형태소 분석 시 첫 문장을 제대로 인식하지 못하는 문제 해결
    nodes = mecab.parseToNode(text)
    result = []

    while nodes:
        features = nodes.feature.split(",")
        pos = features[0]

        if pos in target_pos:  # 명사, 형용사, 동사 형태 확인
            result.append(nodes.surface)

        nodes = nodes.next

    return " ".join(result)


with open("h_q_ver1.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 명사(NNG), 동사(VV), 형용사(VA)
filtered_text = pos_filter(text, ['NNG', 'VV', 'VA'])
# print(filtered_text)

top_200_words = top_n_words(filtered_text, 200)
for word, count in top_200_words:
    # print(f"{word}: {count}")
    # 데이터 프레임 생성
    df = pd.DataFrame(top_200_words, columns=['Word', 'Count'])

# 데이터 프레임을 엑셀 파일로 저장
df.to_excel('top_200_words.xlsx', index=False)

# 상위 200개의 단어 중 최빈값 찾기
top200_words_list = [word for word, count in top_200_words]
mode_top200 = mode(top200_words_list)
print(f"최빈값: {mode_top200}")

# 엔그램


def generate_ngrams(text, n):
    words = text.split()
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]
    return ngrams


def top_n_ngrams(ngrams, n):
    counter = Counter(ngrams)
    return counter.most_common(n)


# Generate n-grams (e.g., 2-grams)
n = 2
ngrams = generate_ngrams(filtered_text, n)

# Get top 200 n-grams
top_200_ngrams = top_n_ngrams(ngrams, 200)
for ngram, count in top_200_ngrams:
    # print(f"{ngram}: {count}")

    # Create a DataFrame and save to Excel
    df_ngrams = pd.DataFrame(top_200_ngrams, columns=['N-gram', 'Count'])
df_ngrams.to_excel('ngrams_top_200.xlsx', index=False)
