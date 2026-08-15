#표준입력:1.jpg 10.png 11.png 2.jpg 3.png
#표준입력:97.xlsx 98.docx 99.docx 100.xlsx 102.docx
files = input().split()
print(list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1], files)))
