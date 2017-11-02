# Segmentation and Tagger

## genius: 基於crf++的開源架構, pip install genius

教育部國語辭典 (16萬詞)/萌典,
 
三個字典檔放於 CRF_seg/genius/genius/library/output.dic

## 自定義文件

my_txt: 欲被斷詞的文章

my_output: 斷詞結果

template在 'CRF_seg/genius/genius/template'內,定義在.txt中,包含break, posTag,negTag

## 各.py 意義

csvTodic.py : 用來將字典檔轉成crf 的.dic format, 即.csv to .dic

segment.py: 主程式位置,用來input file and out put answer

langcov.py: 實際做繁簡體轉換

zh_wiki.py: 根據維基百科繁體簡體反轉,互相轉換的字典檔,由langcov.py 使用






