from _internal import red_window as rw
from _internal.functions import *

key = b'-m4k8hx8IY1NHQ0sZOYtJXVcqXAXJFRuUlrmDKF0f2c='

def register_file_association(
        ext: str = ".stdfs",
        prog_id: str = "SecretText.DocumentFiles",
        app_name: str = "Main_Py",
        exe_path: str | None = None,
        icon_path: str | None = None
) -> None:
    """Создаёт ассоциацию расширения с вашей программой в реестре Windows."""

    # Если путь не указан, берём путь к текущему исполняемому файлу
    if not exe_path:
        exe_path = sys.executable

    exe_path = os.path.abspath(exe_path)
    if icon_path:
        icon_path = os.path.abspath(icon_path)

    try:
        # 1. Связываем расширение с ProgID
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{ext}") as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, prog_id)

        # 2. Создаём описание ProgID (отображается в свойствах файла)
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}") as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, app_name)

        # 3. (Опционально) Иконка файла
        if icon_path:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}\DefaultIcon") as key:
                # Формат: "путь_к_иконке",0
                winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'"{icon_path}",0')

        # 4. Команда открытия (самое важное)
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"Software\Classes\{prog_id}\shell\open\command") as key:
            # "%1" = путь к открытому файлу. Кавычки обязательны для путей с пробелами.
            cmd = f'"{exe_path}" "%1"'
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, cmd)

        print(f"✅ Ассоциация {ext} успешно создана для {exe_path}")

    except PermissionError:
        print("❌ Нет прав на запись в реестр. Запустите от имени пользователя или администратора.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
register_file_association()

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    print(f"📂 Программа запущена с файлом: {file_path}")
    rw.red_window_def(key = key, path_to_file=file_path)

else:
    first_win = tk.Tk()
    first_win.geometry("700x700")
    first_win.title("Secret Text Editor")
    first_win.resizable(width=False, height=False)

    def new_file():
        first_win.destroy()
        rw.red_window_def(key = key)

    def open_file():
        first_win.destroy()
        rw.red_window_def(key = key, path_to_file=askopenfilename(title='Выберете файл', filetypes = [('STDFS Files', '.stdfs')]))

    main_text = tk.Label(first_win, text="Добро пожаловать в\nваш секретный редактор.", font=("Dela Gothic One", 26))
    main_text.pack()

    open_file_btn = tk.Button(text='Открыть файл', command=open_file)
    open_file_btn.pack()

    new_file_btn = tk.Button(text='Новый файл', command=new_file)
    new_file_btn.pack()


    first_win.mainloop()