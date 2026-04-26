import os
import tkinter as tk
from PIL import Image, ImageTk
from _internal.other_py import other_funcs as oth
from tkinter import messagebox as ms

data_of_inputs = 'AUTO'
type_file = 'PNG'

def main(exel_path, power_path) -> None:
    "=================Дополнительное окно================="

    def how_make_slides(*args):
        global num, data_of_inputs
        data_of_inputs = {}
        num = 0
        pptx_list = []

        def on_closing():
            global data_of_inputs
            if data_of_inputs == {}:
                btn_auto_names['image'] = radiobtn_yes_image
                btn_person_names['image'] = radiobtn_image
                data_of_inputs = 'AUTO'
            top.destroy()


        def add_new_file(*args):
            global num
            pptx = str(input_pptx.get("1.0", "end-1c"))
            exel = str(input_exel.get("1.0", "end-1c"))
            if pptx.replace(' ', '') != '' and exel.replace(' ', '') != '':
                if pptx.lower().replace(' ', '') not in pptx_list:
                    pptx_list.append(pptx.lower().replace(' ', ''))
                    tk.Label(text=f'{pptx} <<>> {exel}', master=top).place(x=10, y=150+num*20)
                    num += 1
                    data_of_inputs[pptx] = exel
                else:
                    ms.showerror(message='Данное поле в шаблоне pptx ууже используется!')
            else:
                ms.showerror(message='Поля пустые')

        top = tk.Toplevel(main_win)
        top.title("Новое окно")
        top.geometry("450x600")
        top.protocol("WM_DELETE_WINDOW", on_closing)

        text_main = tk.Label(top, text='Сопоставьте поле в презентации(текст в нем) с\nназванием столбца откуда потребуется брать данные для этого поля')
        text_main.pack()

        input_pptx = tk.Text(top, height=1, width=20)
        input_pptx.place(x=10, y=70)
        input_exel = tk.Text(top, height=1, width=20)
        input_exel.place(x=260, y=70)

        text_pptx = tk.Label(top, text='Поле в шаблоне', font=("Arial Bold", 13))
        text_pptx.place(x=10,y=40)
        text_exel = tk.Label(top, text='Столбец в таблице', font=("Arial Bold", 13))
        text_exel.place(x=260,y=40)

        text_arrow = tk.Label(top, text = '<< >>', font=("Arial Bold", 13))
        text_arrow.place(x=190, y=68)

        btn_add_filter = tk.Button(text='Добавить', master=top, font=("Arial Bold", 13), command=add_new_file)
        btn_add_filter.place(x=170, y=100)
        # Захватываем ввод для дочернего окна
        top.grab_set()

    "=================Функции================="

    def on_closing():
        #print(data_of_inputs,type_file, input_name_files.get("1.0", "end-1c"), input_name_dir.get("1.0", "end-1c"), input_name_file.get("1.0", "end-1c"), sep='\n')
        main_win.destroy()

    def png_btn_def(*args):
        global type_file
        type_file = 'PNG'
        btn_png['image'] = png_image_yes
        btn_pdf['image'] = pdf_image

    def pdf_btn_def(*args):
        global type_file
        type_file = 'PDF'
        btn_png['image'] = png_image
        btn_pdf['image'] = pdf_image_yes

    def btn_auto_names_def(*args):
        global data_of_inputs
        btn_auto_names['image'] = radiobtn_yes_image
        btn_person_names['image'] = radiobtn_image
        data_of_inputs = 'AUTO'

    def btn_person_names_def(*args):
        btn_auto_names['image'] = radiobtn_image
        btn_person_names['image'] = radiobtn_yes_image
        how_make_slides()

    def complete_btn(*args):
        if input_name_files.get("1.0", "end-1c") != '' and input_name_dir.get("1.0", "end-1c") != '':
            dir_name = str(input_name_dir.get("1.0", "end-1c"))
            main_name = input_name_files.get("1.0", "end-1c")
            file_name = input_name_file.get("1.0", "end-1c")
            main_win.destroy()
            oth.ender_page____(old_path_pptx=power_path,
                              exel_path=exel_path,
                              file_type=type_file,
                              dir_name=dir_name,
                              main_name_for_file=main_name,
                              new_file_name=file_name,
                              inputs = data_of_inputs
                                  )

        else:
            ms.showerror(message='Не все данные заполнены')


    "=================Настройка окна================="

    main_win = tk.Tk()
    main_win.title("Настройка")
    main_win.geometry("500x800")
    main_win.protocol("WM_DELETE_WINDOW", on_closing)
    main_win.resizable(False, False)

    "=================Переменные================="
    radiobtn_image = ImageTk.PhotoImage(Image.open('_internal/image/radiobtn.png').resize((20, 20)))
    radiobtn_yes_image = ImageTk.PhotoImage(Image.open('_internal/image/radiobtn_yes.png').resize((20, 20)))
    png_image = ImageTk.PhotoImage(Image.open('_internal/image/png_image_btn.png').resize((80, 80)))
    pdf_image = ImageTk.PhotoImage(Image.open('_internal/image/pdf_image_btn.png').resize((80, 80)))
    png_image_yes = ImageTk.PhotoImage(Image.open('_internal/image/png_image_btn_yes.png').resize((80, 80)))
    pdf_image_yes = ImageTk.PhotoImage(Image.open('_internal/image/pdf_image_btn_yes.png').resize((80, 80)))

    "=================Текст================="

    text_title = tk.Label(main_win, text="Настройка создания", font=("Arial", 25))
    text_title.place(x=100,y=5)

    text_info = tk.Label(main_win, text = f'Выбранный файл PowerPoint:\n {'  - "'+os.path.split(os.path.split(power_path)[0])[1]+'/'+os.path.split(power_path)[1]+'"'}\nВыбранный файл Exel:\n {'  - "'+os.path.split(os.path.split(exel_path)[0])[1]+'/'+os.path.split(exel_path)[1]+'"'}', font=("Arial Bold", 13 ), justify="left")
    text_info.place(x=10,y=45)

    "=================Соответствие названий================="

    text_make_slides =  tk.Label(main_win,text='Настройка создания слайдов', font=("Arial", 20))
    text_make_slides.place(x=10,y=130)

    btn_auto_names = tk.Button(main_win, image=radiobtn_yes_image, command=btn_auto_names_def)
    btn_auto_names.place(x=10,y=180)
    btn_person_names = tk.Button(main_win, image=radiobtn_image, command=btn_person_names_def)
    btn_person_names.place(x=10,y=230)

    text_auto_names = tk.Label(main_win,text='Автоматическая вставка в шаблон', font=("Arial", 15))
    text_auto_names.place(x=40,y=180)
    text_person_names = tk.Label(main_win,text='Свои настройки', font=("Arial", 15))
    text_person_names.place(x=40,y=230)

    "=================Имя файла================="

    text_name_file = tk.Label(main_win, text="Название для нового pptx", font=("Arial Bold", 18))
    text_name_file.place(x=10, y=280)

    input_name_file = tk.Text(main_win, height=1, width=20, font=("Arial Bold", 15))
    input_name_file.place(x=10, y=320)

    "=================Назване для файлов================="

    text_name_files = tk.Label(main_win,text="Укажите столбец с названиями слайдов", font=("Arial Bold", 18))
    text_name_files.place(x=10,y=360)

    input_name_files = tk.Text(main_win,height=1, width=20, font=("Arial Bold", 15))
    input_name_files.place(x=10,y=400)

    "=================Папка сохранения================="

    text_name_dir = tk.Label(main_win,text="Название папки для сохранения", font=("Arial Bold", 18))
    text_name_dir.place(x=10,y=460)

    input_name_dir=tk.Text(main_win,height=1, width=20, font=("Arial Bold", 15))
    input_name_dir.place(x=10,y=500)

    "=================Вид сохранения================="

    text_type_save = tk.Label(main_win,text="Тип сохранения слайдов:", font=("Arial Bold", 20))
    text_type_save.place(x=10,y=550)

    btn_png = tk.Button(master=main_win, image=png_image_yes, command=png_btn_def)
    btn_png.place(x=100,y=600)

    btn_pdf = tk.Button(master=main_win, image=pdf_image, command=pdf_btn_def)
    btn_pdf.place(x=300,y=600)

    "=================Конечная кнопка================="

    compl_btn = tk.Button(main_win, height=1, width=7, text = 'Complete',  font=('Arial', 20, 'bold'), command=complete_btn)
    compl_btn.pack()
    compl_btn.place(x=190,y=730)

    main_win.mainloop()




if __name__ == "__main__":
    main("D:/My things/Projects/Проект АвтоГрамоты/Таблица-шаблоны.xlsx","D:/My things/Projects/Проект АвтоГрамоты/Шаблон 1.pptx")