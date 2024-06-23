# 使用python socket 实现的web服务器

目前支持托管静态文件夹


运行方法：

`python main.py`

### bug
***
暂时发现一个bug，URL中不能有中文，否则会被浏览器默认编码成%xx的格式，在匹配时出现错误
解决办法：识别url中的%编码