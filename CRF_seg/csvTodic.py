csv_file = 'dic.csv'
txt_file = 'output.dic'

text_list = []

'''
    用來將三個字典檔轉成dic,
    餵給crf++定義格式
'''

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",")
        text_list.append(" ".join(line))

with open(txt_file, "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write(line)
    print('File Successfully written.')

