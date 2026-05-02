from _internal.functions import *


def red_window_def(key = None, path_to_file=None):
    reg_size = 14


    tags = {
        "sel": ' ',
    }
    def change_tags_list():
        nonlocal tags
        tags = change_text(text_widget=main_input,
                      tags_dict=tags,
                      reg_size=reg_size)

    def enter_size(event):
        nonlocal reg_size
        try:
            reg_size = int(change_size_input.get('1.0', tk.END))
            return  "break"
        except ValueError as e:
            showerror()
            print(e)
            change_size_input.delete('1.0', tk.END)
            change_size_input.insert(tk.END, str(reg_size))
            return  "break"
        finally:
            print(reg_size)
            change_size_input.tag_remove("sel", "1.0", "end")
            main_input.mark_set("sel", "1.0")
            main_input.focus_set()

    def click_on_main_input(event):
        if change_size_input.get('1.0', tk.END) != reg_size:
            change_size_input.delete('1.0', tk.END)
            change_size_input.insert(tk.END, str(reg_size))

    red_win = tk.Tk()
    red_win.geometry('1000x800')
    red_win.title("*New File")
    red_win.resizable(False, False)

    main_input = tk.Text(red_win, font=('Arial', 14), bg='white', fg='black', borderwidth=0, height=30, width=91)
    main_input.place(x=0, y=100)
    main_input.bind('<Button-1>', click_on_main_input)
    if path_to_file:
        tags = load_file(key=key, text_widget=main_input, filepath=path_to_file, window_widget=red_win)
        print(tags)




    btn1 = tk.Button(text='Save', command=lambda: save_file(key = key,
                                                            text_widget=main_input,
                                                            filepath= askopenfilename(title='Выберете файл', filetypes = [('STDFS Files', '.stdfs')]),
                                                            tags_list= tags,
                                                            password = enter_password(),
                                                            window_widget = red_win
                                                            )
                     )
    btn1.place(x=0, y=0)
    btn2 = tk.Button(text='Load', command=lambda: tags == load_file(key = key,
                                                       text_widget=main_input,
                                                       filepath=askopenfilename(title='Выберете файл', filetypes = [('STDFS Files', '.stdfs')]),
                                                       window_widget=red_win
                                                       )
                     )
    btn2.place(x=50, y=0)

    bt3 = tk.Button(text='format', command=change_tags_list)
    bt3.place(x=100, y=0)

    tk.Button(text='', command=lambda: print(tags)).place(x=150, y=0)
    change_size_input = tk.Text(red_win, height=1, width=3, )
    change_size_input.insert(tk.END, '14')
    change_size_input.bind('<Return>', enter_size)
    change_size_input.place(x=150, y=0)
    red_win.mainloop()

if __name__ == '__main__':
    red_window_def()