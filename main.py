import socket  # 导入 socket 模块

static_dir = "./public"  # 静态资源目录
s = socket.socket()  # 创建 socket 对象
port = 10002  # 设置端口
s.bind(("0.0.0.0", port))  # 绑定端口
s.listen(5)  # 等待客户端连接

print("服务器已启动于 http://127.0.0.1:" + str(port))


# 获取到请求之后进行解析
def router(req_str):
    req_head_arr = req_str.split("\n")

    res_byte = b""  # 响应头的字节流

    if req_head_arr[0][:5] != "GET /":  # 通过读请求头判断是否是http协议
        return res_byte

    req_path = req_head_arr[0].split(" ")[1]  # 根据空格进行切割，拿到请求头上的路径
    print(req_path)  # 打印get请求路径
    if req_path == "/":
        req_path = "/index.html"

    mime_type = ""
    try:
        mime_type = req_path.split(".")[1]  # 截取请求的mime类型
    except:
        mime_type = ""

    content_type = ""  # 响应头的mime类型

    # 设置响应头mime
    if mime_type == "jpg":
        content_type = "image/jpg"
    elif mime_type == "png":
        content_type = "image/png"
    elif mime_type == "gif":
        content_type = "image/gif"
    elif mime_type == "css":
        content_type = "text/css"
    elif mime_type == "js":
        content_type = "text/javascript"
    elif mime_type == "html":
        content_type = "text/html"
    elif mime_type == "json":
        content_type = "application/json"
    elif mime_type == "mp4":
        content_type = "video/mp4"
    elif mime_type == "mp3":
        content_type = "audio/mp3"
    elif mime_type == "ico":
        content_type = "image/vnd.microsoft.icon"
    elif mime_type == "zip":
        content_type = "application/zip"
    elif mime_type == "7z":
        content_type = "application/x-7z-compressed"
    elif mime_type == "rar":
        content_type = "application/vnd.rar"

    # 从磁盘读取文件
    try:
        with open(static_dir + req_path, "rb") as fp:
            res_byte = (
                "HTTP/1.1 200 OK \nContent-Type: " + content_type + "\n\n"
            ).encode() + fp.read()
    except:
        res_byte = (
            "HTTP/1.1 200 OK \nContent-Type: text/plain\n\n 404 not found".encode()
        )
    return res_byte


while True:
    c, addr = s.accept()  # 建立客户端连接
    print("连接地址：", addr)
    str = c.recv(4096).decode()
    c.send(router(str))  # 接受到请求后调用 路由函数进行处理，并发送响应
    c.close()  # 关闭客户端连接
s.close()
