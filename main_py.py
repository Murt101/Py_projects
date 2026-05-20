from _internal.other_py import red_window as rw
from _internal.other_py.functions import *
import sys, winreg
from tkinter import filedialog as fd

key = b'-m4k8hx8IY1NHQ0sZOYtJXVcqXAXJFRuUlrmDKF0f2c='

def register_file_association(
        ext: str = ".stdfs",
        prog_id: str = "SecretText.DocumentFiles",
        app_name: str = "Main_Py",
        exe_path: str | None = None,
        icon_path: str | None = None
) -> None:

    # Если путь не указан, берём путь к текущему исполняемому файлу
    if not exe_path:
        exe_path = sys.executable

    exe_path = os.path.abspath(exe_path)
    if icon_path:
        icon_path = os.path.abspath(icon_path)

    try:
        # 1. Связываем расширение с ProgID
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{ext}") as key_:
            winreg.SetValueEx(key_, "", 0, winreg.REG_SZ, prog_id)

        # 2. Создаём описание ProgID (отображается в свойствах файла)
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}") as key_:
            winreg.SetValueEx(key_, "", 0, winreg.REG_SZ, app_name)

        # 3. (Опционально) Иконка файла
        if icon_path:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}\DefaultIcon") as key_:
                # Формат: "путь_к_иконке",0
                winreg.SetValueEx(key_, "", 0, winreg.REG_SZ, f'"{icon_path}",0')

        # 4. Команда открытия (самое важное)
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}\shell\open\command") as key_:
            # "%1" = путь к открытому файлу. Кавычки обязательны для путей с пробелами.
            cmd = f'"{exe_path}" "%1"'
            winreg.SetValueEx(key_, "", 0, winreg.REG_SZ, cmd)


    except PermissionError:
        pass
    except Exception as e:
        pass

#register_file_association()

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    print(f"📂 Программа запущена с файлом: {file_path}")
    rw.red_window_def(key = key, path_to_file=file_path)

else:
    first_win = tk.Tk()
    first_win.geometry("600x800")
    first_win.title("Secret Text Editor")
    first_win.resizable(width=False, height=False)
    first_win.configure(bg="#6155F5")

    def new_file():
        first_win.destroy()
        rw.red_window_def(key = key)

    def open_file():
        first_win.destroy()
        rw.red_window_def(key = key, path_to_file=fd.askopenfilename(title='Выберете файл', filetypes = [('STDFS Files', '.stdfs')]))

    main_text = tk.Label(first_win, text="Секретный\nредактор", font=("Dela Gothic One", 26), bg="#6155F5", fg="white")
    main_text.place(relx=0.5, y = 100, anchor="center")

    open_file_btn = tk.Button(text='Открыть файл', command=open_file, bg = '#D4A843', font = ('Dela Gothic One', 16))
    open_file_btn.place(relx=0.5, y = 300, anchor="center")

    new_file_btn = tk.Button(text='Создать новый файл', command=new_file, bg = '#D4A843', font = ('Dela Gothic One', 16))
    new_file_btn.place(relx=0.5, y = 400, anchor="center")



    first_win.mainloop()
