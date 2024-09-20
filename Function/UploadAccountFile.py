from tkinter import filedialog
import Model.LoginModel as loginml

def upload_file():
    loginml.upload_file_path = filedialog.askopenfilename(
        title="CSV 파일을 선택하세요",
        filetypes=(("Account Files", "*.csv"), ("All Files", "*.*"))
    )