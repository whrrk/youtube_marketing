import tkinter as tk
from tkinter import ttk
from Function.UploadFile import upload_account_file,upload_proxy_file
from Model.LoginModel import run

class Traffic:
    def display():
        # create mains
        root = tk.Tk()
        root.title("WhTraffic Ver.1")
        root.geometry('500x300')

        # create notebook
        notebook = ttk.Notebook(root)

        # create tab
        continue_tab = ttk.Frame(notebook)
        pump_tab = ttk.Frame(notebook)
        set_tab = ttk.Frame(notebook)

        # frame notebook
        notebook.add(continue_tab, text="Continuing")
        notebook.add(pump_tab, text="Pump")
        notebook.add(set_tab, text="Setting")

        # packing notebook
        notebook.pack(expand=True, fill='both')

        # add content in continue_tab
        continue_start_lbl = tk.Label(continue_tab, text="시작")
        continue_start_lbl.grid(column=0, row=0)
        continue_start_btn = tk.Button(continue_tab, text="Start")
        continue_start_btn.grid(column=1, row=0)

        continue_stop_lbl = tk.Label(continue_tab, text="중지")
        continue_stop_lbl.grid(column=0, row=2)
        continue_stop_btn = tk.Button(continue_tab, text="Stop")
        continue_stop_btn.grid(column=1, row=2)

        continue_exit_lbl = tk.Label(continue_tab, text="초기화")
        continue_exit_lbl.grid(column=0, row=4)
        continue_exit_btn = tk.Button(continue_tab, text="Exit")
        continue_exit_btn.grid(column=1, row=4)

        # add content in pump_tab
        pump_start_lbl = tk.Label(pump_tab, text="시작")
        pump_start_lbl.grid(column=0, row=0)
        punp_start_btn = tk.Button(pump_tab, text="Start", command=run)
        punp_start_btn.grid(column=1, row=0)

        pump_stop_lbl = tk.Label(pump_tab, text="중지")
        pump_stop_lbl.grid(column=0, row=2)
        pump_stop_btn = tk.Button(pump_tab, text="Stop")
        pump_stop_btn.grid(column=1, row=2)

        pump_exit_lbl = tk.Label(pump_tab, text="초기화")
        pump_exit_lbl.grid(column=0, row=4)
        pump_exit_btn = tk.Button(pump_tab, text="Exit")
        pump_exit_btn.grid(column=1, row=4)

        # add content in set_tab
        set_youtube_lbl = tk.Label(set_tab, text="유튜브 링크")
        set_youtube_lbl.grid(column=0, row=1)

        set_youtube_input = tk.Entry(set_tab, width=50)
        set_youtube_input.grid(column=1, row=1)

        # set_youtube_confirm_btn = tk.Button(set_tab, text="확인")
        # set_youtube_confirm_btn.grid(column=3, row=1)
        # set_youtube_modify_btn = tk.Button(set_tab, text="수정")
        # set_youtube_modify_btn.grid(column=5, row=1)

        # 구글 계정 업로드 버튼
        account_file_label_text = tk.StringVar(value="업로드 파일 없음")
        account_file_label = tk.Label(set_tab,textvariable=account_file_label_text)
        account_file_label.grid(column=1, row=2)

        set_account_upload_btn = tk.Button(set_tab, text="구글 계정 파일 업로드", command=lambda: upload_account_file(account_file_label_text))
        set_account_upload_btn.grid(column=0, row=2)        

        # 프록시 IP 업로드 버튼
        proxy_file_label_text = tk.StringVar(value="업로드 파일 없음")
        proxy_file_label = tk.Label(set_tab,textvariable=proxy_file_label_text)
        proxy_file_label.grid(column=1, row=3)
        set_proxy_upload_btn = tk.Button(set_tab, text="프록시 IP 파일 업로드", command=lambda: upload_proxy_file(proxy_file_label_text))
        set_proxy_upload_btn.grid(column=0, row=3)

        root.mainloop()

def main_run(cls):
    cls.display()

main_run(Traffic)
