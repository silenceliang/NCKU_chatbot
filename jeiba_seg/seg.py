#encoding=utf-8

import jieba
jieba.load_userdict("mydict")
import jieba.posseg as pseg

test_sent = (
"#靠北高師大12201\n近日 傳情活動甚多\n但是ㄈㄗ對此心如死灰\n然而想給各魯一點溫暖\n"
"想贈送 自己做的巧克力蛋糕\n"
"給 三個最先留言說想要Der 的人\n"
"條件 一定要是魯魯\n"
"支持同婚\n"
"但其實我也沒做過巧克力蛋糕 呵呵"
)

words = jieba.cut(test_sent, HMM=True)
print('/'.join(words))

result = pseg.cut(test_sent)
for w in result:
    print(w.word, "_", w.flag, ',', end=' ')

