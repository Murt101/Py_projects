from _internal.other_files.proj import project_main
from _internal.other_files.other_fuctions import *


def main_open():

    def close():
        close_window(main_window, None)

    def add_project():
        main_window.destroy()
        project_main()

    def add_project_with_pic():
        add_project_with_pic___(name_window=main_window)

    main_window = tk.Tk()
    main_window.geometry('550x550')
    main_window.resizable(False,False)
    main_window.title('Графический редактор Дмитрия Владимировича')
    main_window.iconbitmap('_internal/IMG/ICO/MAIN_WINDOW.ico')
    main_window_text = tk.Label(text='Добро пожаловать в графический редактор \n Ультра Мега 0.0.0.1.beta',font =('COMIC SANS MS', 17))
    main_window_text.place(x = 30, y = 20)

    main_window.config(menu=add_menu(main_window, None, None,add_project, add_project_with_pic, owner, spravka,close))

    btn_pic = tk.Button(text='Редактировать изображение', command=add_project_with_pic, font=('COMIC SANS MS',13), anchor="center")
    btn_pic.place(x=160,y=150)

    btn_proj = tk.Button(text='Начать новый проект', command=add_project, font=('COMIC SANS MS',13))
    btn_proj.place(x=180,y=350)

    btn_owner = tk.Button(text='Информация о владельце', command=owner, font = ('COMIC SANS MS',13))
    btn_owner.place(x =160, y = 250)
    main_window.mainloop()

if __name__ == '__main__':
    main_open()