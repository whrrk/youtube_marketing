from tkinter import filedialog
from Parser.ParsingAccount import ParsingAccount
import tkinter as tk
from multiprocessing import shared_memory
import numpy as np

file_path = None
def upload_file():
    file_name = filedialog.askopenfilename(
        title="CSV 파일을 선택하세요",
        filetypes=(("Account Files", "*.csv"), ("All Files", "*.*"))
    )

    global file_path
    file_path = file_name

    return file_path

def get_file_path():
    return file_path
