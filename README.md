# GoogleTranslate谷歌翻译
谷歌翻译 python3
## 依赖
~~~python
 pip install PyExecJS
 pip install requests
~~~
## 使用
将GoogleTranslate.py放到~Python36\Lib\site-packages目录下<br>
~~~python
import GoogleTranslate
# 英译中
GoogleTranslate.translate('hello world')
# 中译英
GoogleTranslate.translate('你好世界')
~~~
## 说明
1、计算tk的js部分来自https://github.com/cocoa520/Google_TK<br>
