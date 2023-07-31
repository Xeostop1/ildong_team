import openpyxl


def find_cells_with_words(input_file, output_file, main_word, sub_word):
    wb = openpyxl.load_workbook(input_file)
    ws = wb.active

    # 도미나를 포함하고 도미나스를 포함하지 않는 셀 값을 찾습니다.
    without_sub_word_results = []
    with_sub_word_results = []
    for row in ws.iter_rows():
        for cell in row:
            if main_word in str(cell.value):
                without_sub_count = str(cell.value).count(main_word) - str(cell.value).count(sub_word)
                if sub_word not in str(cell.value):
                    without_sub_word_results.append((cell.coordinate, cell.value, without_sub_count))
                else:
                    with_sub_word_count = str(cell.value).count(sub_word)
                    with_sub_word_results.append((cell.coordinate, cell.value, with_sub_word_count))

    # 결과를 새 TXT 파일로 저장하고 인코딩을 UTF-8로 지정합니다.
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{main_word}를 포함하고 {sub_word}를 포함하지 않는 셀:\n")
        for coordinate, value, count in without_sub_word_results:
            f.write(f"{coordinate}: {value} ({count}개)\n")
        
        f.write(f"\n{sub_word}를 포함하는 셀:\n")
        for coordinate, value, count in with_sub_word_results:
            f.write(f"{coordinate}: {value} ({count}개)\n")


# 사용 예
main_word = "아이"
sub_word = "아이크림"
input_file = "C:\\Users\\user\\Desktop\\BigdataClass\\git clone\\ildong_team\\pre_folder\\gimi_origin.xlsx"
output_file = f"{main_word}-{sub_word}.txt"

find_cells_with_words(input_file, output_file, main_word, sub_word)
print("완료")
