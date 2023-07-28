num = 10000
with open('abcnews-date-text.csv', 'r') as fr:
    data = fr.readlines()[:num+1]
with open('abcnews-date-text_%s.csv' % num, 'w') as fw:
    fw.writelines(data)


