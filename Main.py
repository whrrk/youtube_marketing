import tkinter as tk
from tkinter import ttk

# 메인 화면 생성
root = tk.Tk()
root.title("WhPlus Ver.1")

# 노트북 생성
notebook = ttk.Notebook(root)

# 노트북 탭 생성
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# 프레임을 노트북에 씌움
notebook.add(tab1, text="유지용")
notebook.add(tab2, text="펌핑용")
notebook.add(tab3, text="설정")

# 노트북 위젯을 패킹
notebook.pack(expand=True, fill='both')

# 탭1에 컨텐츠 추가
label1 = tk.Label(tab1, text="This is Tab 1")
label1.pack(pady=20, padx=20)

button1 = tk.Button(tab1, text="Button in Tab 1")
button1.pack(pady=20)

# 탭2에 컨텐츠 추가
label2 = tk.Label(tab2, text="This is Tab 2")
label2.pack(pady=20, padx=20)

entry2 = tk.Entry(tab2)
entry2.pack(pady=20)

# 탭3에 컨텐츠 추가
label3 = tk.Label(tab3, text="This is Tab 3")
label3.pack(pady=20, padx=20)

text_area3 = tk.Text(tab3, height=10, width=30)
text_area3.pack(pady=20)

# Run the application
root.mainloop()