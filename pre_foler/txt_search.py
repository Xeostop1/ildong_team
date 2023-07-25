import openpyxl


def find_cells_with_two_words(input_file, output_file, word1, word2):
    # 입력 파일을 엽니다.
    wb = openpyxl.load_workbook(input_file)
    ws = wb.active

    # 두 단어를 포함하는 셀의 좌표 및 값을 찾습니다.
    results = []
    for row in ws.iter_rows():
        for cell in row:
            if word1 in str(cell.value) and word2 in str(cell.value):
                results.append((cell.coordinate, cell.value))

    # 두 단어를 포함하는 셀 정보와 셀 개수를 새 TXT 파일로 저장하고 인코딩을 UTF-8로 지정합니다.
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"총 개수: {len(results)}\n\n")
        for coordinate, value in results:
            f.write(f"{coordinate}: {value}\n")


# 사용 예
word1 = "한의원"
word2 = "기미"  
input_file = "./pre_foler/gimi_origin.xlsx"  #원본 엑셀 파일 경로
output_file = f"{word1}_{word2}.txt"  # 출력 TXT 파일 경로

find_cells_with_two_words(input_file, output_file, word1, word2)
print("완료")
