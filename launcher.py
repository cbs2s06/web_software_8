# -*- coding: utf-8 -*-
import subprocess
import os

print("欢迎使用！")
print("香港理工大學服務學習CBS2S06第八小組出品")
print("正在进行python必备环境检查。")
os.system(f'pip install {"flask"}')
os.system(f'pip install {"openai"}')
os.system(f'pip install {"pdfplumber"}')
os.system(f'pip install {"re"}')
os.system(f'pip install {"webbrowser"}')
os.system(f'pip install {"threading"}')
print("环境初始化成功，即将开始运行。")

subprocess.Popen(['python', 'app.py'])