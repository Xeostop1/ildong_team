import MeCab
import pandas as pd
from collections import Counter


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
print(filtered_text)


top_200_words = top_n_words(filtered_text, 200)
for word, count in top_200_words:
    print(f"{word}: {count}")


# 데이터 프레임 생성
df = pd.DataFrame(top_200_words, columns=['Word', 'Count'])

# 데이터 프레임을 엑셀 파일로 저장
df.to_excel('top_200_words.xlsx', index=False)
