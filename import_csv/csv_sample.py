import csv
import os

csv_file = open("./records.csv", "r", encoding="utf_8")

# リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
# # 辞書形式
# f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(f)
i = 1
for row in f:
  txt = open('./text/text_' + str(i).zfill(3) + '.txt', 'w')
  txt.write(row[3])
  # print(row[3])
  txt.close
  i += 1

csv_file.close
a =sorted(os.listdir(path='./text'))
print(a)