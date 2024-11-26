import os
from dotenv import load_dotenv

def resolve_env(*keys: str) -> set:
    load_dotenv()
    return set([val for key in keys for val in list(os.getenv(key))])

def output(words: set):
    if len(words) == 0 :
        return
    with open('required-word.txt', 'w', encoding='utf-8') as file:
        for word in words:
            if word and not word.isspace():
                file.write(word + ' ')

# ttf字体压缩
# 1. 生成正在使用的字符清单(python font_subset.py)
# 2. 安装pip install fonttools
# 3. pyftsubset Pacifico-Regular-all.ttf --text-file=required-word.txt --output-file=Pacifico-Regular.ttf
if __name__ == '__main__':
    words = resolve_env('VITE_SITE_URL', 'VITE_DESC_HELLO', 'VITE_DESC_HELLO_OTHER')
    output(words)