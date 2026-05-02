import json, base64, os, hashlib, winreg, sys
import tkinter as tk
from cryptography.fernet import Fernet
from tkinter.filedialog import *
from tkinter.messagebox import *

tags_num = 0

def change_text(text_widget: tk.Text,
                tags_dict: dict,
                reg_size: int = 14) \
        -> dict:
    global tags_num
    try:
        start, end = text_widget.tag_ranges("sel")
        tag_name = f"custom_fmt_{tags_num}"
        tags_num += 1
        tags_dict[tag_name] = ["Arial", reg_size, 'italic']
        text_widget.tag_configure(tag_name, font=tags_dict[tag_name])
        text_widget.tag_add(tag_name, start, end)
        return  tags_dict
    except ValueError:
        showerror(title='Нет текста', message= "Выделите сначала текст")
        return tags_dict



def load_file(key: bytes,
              text_widget: tk.Text,
              filepath: str,
              window_widget: tk.Tk | tk.Toplevel = None) \
        -> None|dict:

    global tags_num
    tags_list = {'sel': ' '}
    window_widget.title(os.path.split(filepath)[1])

    with open(filepath, 'rb') as f:
        flag = f.read(1)
        if not flag:
            showerror("Ошибка", "Файл пуст или поврежден.")
            return
        salt = f.read(16) if flag == b'\x01' else b''
        encrypted = f.read()

    password = None
    if flag == b'\x01':
        password = enter_password(safe=False)
        if password is None:
            return

    if password:
        seed = password.encode('utf-8')
    else:
        seed = key.encode('utf-8') if isinstance(key, str) else key

    raw_key = hashlib.pbkdf2_hmac('sha256', seed, salt, 100_000, dklen=32)
    fernet_key = base64.urlsafe_b64encode(raw_key)

    try:
        decrypted = Fernet(fernet_key).decrypt(encrypted).decode('utf-8')
        data = json.loads(decrypted)

        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", data["text"])
        print(data["tags"])
        for tag_name, cfg in data["tags"].items():
            if tag_name != 'sel':
                tags_num += 1
                tags_list[tag_name] = cfg
                text_widget.tag_configure(tag_name, font=cfg)

        for r in data["list_tag"]:
            text_widget.tag_add(r["tag"], r["start"], r["end"])
        return tags_list
    except Exception as e:
        showerror("Ошибка", f"Не удалось расшифровать файл.\nПричина: {e}")
        return None



def save_file(key: bytes,
              text_widget: tk.Text,
              filepath: str,
              tags_list: dict,
              window_widget: tk.Tk | tk.Toplevel,
              password: str = None)  \
        -> None:

    window_widget.title(os.path.split(filepath)[1])
    tag_configs = {}
    for tag in text_widget.tag_names():
        tag_configs[tag] = tags_list[tag]

    tag_ranges = []
    for tag in text_widget.tag_names():
        ranges = text_widget.tag_ranges(tag)
        for i in range(0, len(ranges), 2):
            tag_ranges.append({
                "tag": tag,
                "start": str(ranges[i]),
                "end": str(ranges[i + 1])
            })
    data = {
        "text": text_widget.get("1.0", "end-1c"),
        "tags": tag_configs,
        "list_tag": tag_ranges
    }

    json_bytes = json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8')
    if password:
        salt = os.urandom(16)
        flag = b'\x01'
        raw_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000, dklen=32)
    else:
        salt = b''
        flag = b'\x00'
        base = key if isinstance(key, bytes) else key.encode('utf-8')
        raw_key = hashlib.pbkdf2_hmac('sha256', base, salt, 100_000, dklen=32)

    fernet_key = base64.urlsafe_b64encode(raw_key)
    encrypted = Fernet(fernet_key).encrypt(json_bytes)

    with open(filepath, 'wb') as f:
        f.write(flag + salt + encrypted)

def enter_password(safe:bool=True) -> None | str:
    result = None

    def complete(is_psw:bool = True):
        nonlocal result
        if is_psw:
            pwd = input_.get("1.0", "end-1c").replace(' ', '')

            if pwd == '':
                showerror(title='Ошибка пароля', message='Вы ничего не ввели')
                return

            if askyesno(title='Вы уверены?'):
                result = pwd
                root.destroy()
        else:
            if askyesno(title='Вы уверены?'):
                root.destroy()

    root = tk.Toplevel()
    root.grab_set()
    root.geometry('300x120')
    root.title('Введите пароль')
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", complete)

    tk.Label(root, text='Введите пароль').pack()
    input_ = tk.Text(root, height=2)
    input_.pack()
    tk.Button(root, text='Заершить', command=complete).pack()
    tk.Button(root,text='Без пароля', command=lambda: complete(False)).pack() if safe else None
    root.wait_window()
    return result

if __name__ == '__main__':
    change_text(text_widget=tk.Text(), tags_dict= {})
    load_file(key=b'11', text_widget= tk.Text(), filepath='custom_fmt_')
    save_file(key = b'11', text_widget= tk.Text(), filepath='sm.stdfs', tags_list= {}, window_widget=tk.Tk())
    enter_password()