# encoding=utf-8

import genius

input_file = 'my_txt'
output_file = 'my_output'
def main():

    list = []
    ''' input your file '''
    print('寫入你想斷詞file : %s' % input_file)
    with open(input_file, 'r') as f:
        ''' open your txt data  '''
        for line in f.readlines():
            text = line.strip()
            seg_list = genius.seg_text(text,
                use_combine=True,  # 結合原先三個字典檔
                use_pinyin_segment=True,  # 引入斷詞
                use_tagging=True,  # 詞性標記
                use_break=True)  # 暫停字詞使用

            stri = '\n'.join(['%s\t%s' % (word.text, word.tagging) for word in seg_list])
            list.append(stri)

    print('輸出斷詞結果 : %s' % output_file)
    with open(output_file, 'w') as o:
        ''' write your txt data  '''
        for i in list:
            o.write(i)
    print('successful!')

if __name__ == '__main__':
    main()





