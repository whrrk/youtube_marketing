from tkinter import filedialog
import Model.LoginModel as loginml

def upload_account_file(label_text):
    acocunt_file_path = filedialog.askopenfilename(
        title="CSV 파일을 선택하세요",

        filetypes=(("Account Files", "*.csv"), ("All Files", "*.*"))
    )

    if acocunt_file_path:
        loginml.upload_account_file_path = acocunt_file_path
        acocunt_file_name = acocunt_file_path.split('/')[-1]
        label_text.set(acocunt_file_name)


def upload_proxy_file(label_text):
    proxy_file_path = filedialog.askopenfilename(
        title="CSV 파일을 선택하세요",
        filetypes=(("Account Files", "*.csv"), ("All Files", "*.*"))
    )

    if proxy_file_path:
        loginml.upload_proxy_file_path = proxy_file_path
        proxy_file_name = proxy_file_path.split('/')[-1]
        label_text.set(proxy_file_name)
