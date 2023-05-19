import os
import subprocess
import webbrowser

# 獲取當前腳本所在目錄
dirname = os.path.dirname(os.path.abspath(__file__))

# 切換當前工作目錄到腳本所在目錄
os.chdir(dirname)

# 運行 Flask 應用程序
p = subprocess.Popen('python app.py')

# 打開瀏覽器，轉到localhost:5000/index頁面
webbrowser.open('http://localhost:5000/index')