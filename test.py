import sys
from urllib import request
import bili

headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
    "Accept": "text/html",
    "Cookie": ""
}

# 检查是否有命令行参数提供
if len(sys.argv) > 1:
    # sys.argv[1] 是第一个命令行参数
    query = request.pathname2url(sys.argv[1])
    bili.search(query)
else:
    print("没有提供命令行参数。")

