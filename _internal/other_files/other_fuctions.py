import webbrowser
import tkinter as tk
from tkinter.messagebox import *
import os
from tkinter.filedialog import *
from tkinter.colorchooser import *
from PIL import ImageGrab, Image, ImageTk
import time
from random import *
import sys

last_x, last_y = None, None
width_pen = 1
border = 10
pen_draw = False
font = ('COMIC SANS MS', 13)
clk_rubber = False
pen_color = "#000000"
bg_color = 'grey'
oval_var = False
cube_var = False
border_width = border
shape_color_fill = ''
border_color = 'black'
fon_now = ''




user_name = os.getlogin()
current_time = time.localtime()


def close_window(name_window, canvas):      # Функция по закрытию окна
    from Paint_Dmitriy import main_open
    def save_project():
        answer = askyesno(title="Сохранить проект?", message="Вы хотите сохранить изменения?")
        if answer:
            save_as_canvas(name_window, canvas)
    title = name_window.title()
    if title != 'Графический редактор Дмитрия Владимировича':
        response = askquestion(title="Закрыть окно", message="Вернуться в главное меню?")
        if response == 'yes':
            save_project()
            name_window.destroy()
            main_open()
        else:
            response = askquestion(title="Полное закрытие", message="Вы хотите закрыть программу?")
            if response == 'yes':
                save_project()
                name_window.destroy()
                sys.exit()
            else:
                showinfo(message='Ну ок')
    else:
        response = askquestion(title="Полное закрытие", message="Вы действительно хотите выйти из программы?")
        if response == 'yes':
            name_window.destroy()
            sys.exit()

def difficult_window(name_window , save_as_canvas_proj, save_canvas_, new_file, add_project_with_pic, info_owner_func, spravka_func, close_func):  # Шаблон базового рабочего окна
    name_window.geometry(f'1000x700')
    name_window.resizable(False, False)
    relative_path = os.path.join('_internal', 'IMG', 'ICO', 'MAIN_WINDOW.ico')
    full_path = os.path.abspath(relative_path)
    name_window.iconbitmap(full_path)
    name_window.config(bg='lightblue' ,menu=add_menu(name_window, save_as_canvas_proj, save_canvas_, new_file, add_project_with_pic, info_owner_func, spravka_func, close_func) )
    name_window.title('Проект...')

def spravka():  # Простая ссылка на сайт
    webbrowser.open_new("https://murt101.github.io/dc_project/")

def owner():  # Код окна с данными владельца

    def copy_mail():
            window_owner.clipboard_clear()
            window_owner.clipboard_append('akzigitovmarati@gmail.com')


    def copy_tg():

        window_owner.clipboard_clear()
        window_owner.clipboard_append('https://t.me/murat_kkk')


    def copy_site():

        window_owner.clipboard_clear()
        window_owner.clipboard_append("https://murt101.github.io/dc_project/")

    window_owner = tk.Tk()
    window_owner.geometry('320x130')
    window_owner.resizable(False,False)
    relative_path = os.path.join('_internal', 'IMG', 'ICO', 'MAIN_WINDOW.ico')
    full_path = os.path.abspath(relative_path)
    window_owner.iconbitmap(full_path)
    window_owner.title('Информация о владельце')

    main_lbl = tk.Label(text='Здесь представлена вся доступная \nинформация о владельце\n(Кнопки сохраняют ссылки в буфер обмена)', master=window_owner)
    main_lbl.pack()
    btn_mail  = tk.Button(text = 'Почта', command=copy_mail, master=window_owner)
    btn_mail.pack()
    btn_tg = tk.Button(text = 'Telegram', command=copy_tg, master=window_owner)
    btn_tg.pack()
    btn_site = tk.Button(text = 'Сайт', command=copy_site, master=window_owner)
    btn_site.pack()
    window_owner.mainloop()

def add_menu(name_window:vars, save_as_func:vars, save_func:vars, new_file_func:vars, open_img_func:vars, info_owner_func:vars,spravka_func:vars, close_func):  #Функция, которая добавляет главное меню
    menu_bar = tk.Menu(master=name_window)
    file_menu = tk.Menu(menu_bar, tearoff=0)

    if name_window.title() != 'Графический редактор Дмитрия Владимировича':

        file_menu.add_command(label="Сохранить как", command=save_as_func)
        file_menu.add_command(label="Сохранить", command=save_func)
        file_menu.add_separator()
        file_menu.add_command(label='Создать новый файл', command=new_file_func)
        file_menu.add_command(label='Открыть новое изображение', command=open_img_func)
        file_menu.add_separator()
        file_menu.add_command(label="Выход")

        menu_bar.add_cascade(label="Файл", menu=file_menu)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='Информация о владельце', command=info_owner_func)
    help_menu.add_command(label='Как пользоваться', command=spravka_func)
    help_menu.add_separator()
    help_menu.add_command(label='Выход')

    menu_bar.add_cascade(label="Помощь", menu=help_menu)

    menu_bar.add_command(label='Закрыть', command=close_func)

    return menu_bar

def save_as_canvas(name_window:vars, canvas:vars):   #Функция для базового сохранения файлов
    file_types = [("Image file", '.jpeg'), ("PNG", '.png'),("ICO", '.ico')]
    file_path_save = asksaveasfilename(filetypes=file_types, defaultextension=file_types , initialfile='Проект(1)', title='Сохранение')
    name_window.title(os.path.split(file_path_save)[1])
    if file_path_save == '':
        showerror(title='Ошибка',message='Вы ничего не выбрали')
    else:
        x = name_window.winfo_rootx() + canvas.winfo_x()
        y = name_window.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        # Захватываем область экрана с содержимым Canvas
        image = ImageGrab.grab().crop((x, y, x1, y1))
        image.save(file_path_save)

def save_canvas(name_window:vars, canvas:vars):  #Функция дающая выбор как и куда сохранить файлы
    if not os.path.exists(
            f'C:/Users/{user_name}/Downloads/Muart_Paint'):
        os.makedirs(
            f'C:/Users/{user_name}/Downloads/Muart_Paint')
    x = name_window.winfo_rootx() + canvas.winfo_x()
    y = name_window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Захватываем область экрана с содержимым Canvas
    image = ImageGrab.grab().crop((x, y, x1, y1))
    image.save(f'C:/Users/{user_name}/Downloads/Muart_Paint/fail_{time.strftime('%H-%M-%S', current_time)}.jpg')
    name_window.title(f"fail_{time.strftime('%H-%M-%S', current_time)}.jpg")

def change_pen_color__(name_window:vars, bg_color:vars):   #Изменяет цвет пера
    pen_color = ''
    name_window.grab_set()
    new_color = askcolor()[1]
    if new_color and new_color != bg_color:
        pen_color = new_color
    elif new_color == bg_color:
        showerror(title='Выбор цвета для пера', message='У вас не может быть цвет такой же, как и цвет фона')
    name_window.grab_release()
    return pen_color

def change_bg_color__(name_window:vars, pen_color:vars, canvas:vars): #Изменяет цвет холста
    name_window.grab_set()
    bg_color = ''
    new_color = askcolor()[1]
    if new_color and new_color != pen_color:
        canvas['bg'] = new_color
        bg_color = new_color
    elif new_color == pen_color:
        showerror(title='Выбор цвета для фона', message='У вас не может быть цвет такой же, как и цвет для рисования')
    name_window.grab_release()
    return bg_color

def random_random_circle( canvas:vars, border_color:vars, shape_color_fill, border_width ): #В рандомном месте создает круг
    x_o, y_0 = randint(50, 600), randint(50, 600)
    b = randint(10, 100)
    canvas.create_oval(x_o, y_0, x_o + b, y_0 + b, outline=border_color, fill=shape_color_fill, width=border_width)

def add_project_with_pic___(name_window:vars):
    from _internal.other_files.project_with_pic import project_main_pic
    file_types = [("Images", "*.png;*.jpg;*.gif;*.jpeg")]
    file_path = askopenfilename(filetypes=file_types, title="Выбери себе файл")
    if file_path == '':
        showinfo('Ошибка файла', 'Лее брат. Файл кто не выбрал?')
    else:
        name_window.destroy()
        project_main_pic(file_path)

def draw_something(event, pen_draw:bool, clk_rubber:bool, canvas:vars, pen_color, width_pen, bg_color, border_color, shape_color_fill, border_width , last_x, last_y, oval_var, cube_var): #Функция для рисования
    x, y = event.x, event.y

    if pen_draw: # Функция для рисования линии
        canvas.create_line([last_x, last_y, x, y], fill=pen_color, width=width_pen)
        last_x, last_y = x, y
        return last_x, last_y

    elif clk_rubber: # Функция для стирания
        canvas.create_line([last_x, last_y, x, y], fill=bg_color, width=width_pen)
        last_x, last_y = x, y
        return last_x, last_y

    elif oval_var: # Функция для рисования
        if oval_var:
            canvas.delete(oval_var)
        rect_coords = [last_x, last_y, event.x, event.y]
        oval_var = canvas.create_oval(rect_coords, outline=border_color, fill=shape_color_fill, width=border_width)
        return oval_var

    elif cube_var: #Функция для рисования прямоугольника
        if cube_var:
            canvas.delete(cube_var)
        rect = [last_x,last_y,event.x,event.y]
        cube_var = canvas.create_rectangle(rect, outline=border_color, fill=shape_color_fill, width=border_width )
        return cube_var

def add_image(path:str, canvas:vars, fon_now):       #Можно добавить изображение по центру
    if fon_now:
        canvas.delete(fon_now)# Сохранение ссылки на изображение
    img = Image.open(path)
    img_bg = ImageTk.PhotoImage(img)  # Создаем фотоизображение
    fon_now = canvas.create_image(350, 350, image=img_bg)
    canvas.lower(fon_now)
    canvas.img_bg = img_bg
    return fon_now

def make_new_file(name_window:vars, canvas:vars):  #
    from _internal.other_files.proj import project_main
    if askyesno(title='Уверены что сохранились?', message='Сохранить проект?'):
        save_as_canvas(name_window, canvas)
    if askyesno(message='Создаем новый проект?'):
        name_window.destroy()
        project_main()


if __name__ == '__main__':
     owner()
     spravka()
     save_as_canvas(None,None)
     close_window('gg', None)
     add_image('None',None,None)