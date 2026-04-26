import tkinter as tk
from _internal.other_py import red_window as rw
from tkinter import filedialog as fd
from tkinter import messagebox as mbox

def main():
    global ex, pw, power_file_path, exel_file_path
    #power_path = 'D:/My things/Projects/Проект АвтоГрамоты/Шаблон 1.pptx'
    #exel_path = 'D:/My things/Projects/Проект АвтоГрамоты/Таблица-шаблоны.xlsx'

    main_win = tk.Tk()
    main_win.geometry("400x300")
    main_win.resizable(width=False, height=False)
    main_win.title('Автограмоты 0.1 Beta')
    ex = 0
    pw = 0
    exel_file_path = ''
    power_file_path = ''

    def exel_load(*args):
        global ex, exel_file_path
        exel_file_path = fd.askopenfilename(
            title="Выберите Excel файл",
            filetypes=[
                ("Excel Files", "*.xlsx *.xls"),  # Описание и маски файлов
            ]
        )

        if exel_file_path:
            ex = 1
            load_exel_btn['text'] = 'Exel-файл выбран'
            load_exel_btn['state'] = 'disabled'
        else:
            mbox.showerror(message='Файл не выбран')

    def power_load(*args):
        global pw, power_file_path
        power_file_path = fd.askopenfilename(
            title="Выберите Excel файл",
            filetypes=[
                ("PowerPoint Files", "*.pptx *.ppt *.pptm"),  # Описание и маски файлов
            ]
        )


        if power_file_path:
            pw = 1
            load_power_btn['text'] = 'PowerPoint-файл выбран'
            load_power_btn['state'] = 'disabled'
        else:
            mbox.showerror(message='Файл не выбран')

    def all_load(*args):

        if ex + pw == 2:
            main_win.destroy()
            rw.main(power_path = power_file_path, exel_path=exel_file_path)
        else:
            mbox.showerror(message='Не все файлы загружены')

    main_title = tk.Label(main_win, text='Создание множества грамот из бд в exel и \nшаблона powerpoint', font=('Arial', 12, 'bold'))
    main_title.place(x=25, y=10)

    load_exel_btn = tk.Button(main_win,height=2,width=20 , text='Добавить Exel\nфайл', command=exel_load)
    load_exel_btn.place(x=30,y=80)
    load_power_btn = tk.Button(main_win,height=2,width=20, text='Добавить PowerPoint\nфайл', command=power_load)
    load_power_btn.place(x=210,y=80)
    load_complete_btn = tk.Button(main_win,height=2,  text="Перейти к следующему этапу", command=all_load)
    load_complete_btn.place(x=100,y=150)

    main_win.mainloop()

if __name__ == '__main__':
    main()