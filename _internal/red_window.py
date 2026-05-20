from tkinter import ttk
import tkinter.font as tkfont
from _internal.other_py.functions import *
from tkinter.filedialog import *


def red_window_def(key = None, path_to_file=None):
    reg_size = 14
    tags = {
        "sel": ' ',
    }
    font = "Arial"

    def change_type(type_):
        list_types[type_][0] = not list_types[type_][0]
        if  list_types[type_][0]:
            list_types[type_][1].config(borderwidth=4)
        else:
            list_types[type_][1].config(borderwidth=2)


    def change_tags_list():
        nonlocal tags
        tags = change_text(text_widget=main_input,
                      tags_dict=tags,
                      reg_size=reg_size,
                      list_types=list_types,
                      family_font=font
                           )

    def enter_size(event):
        nonlocal reg_size
        try:
            reg_size = int(change_size_input.get('1.0', tk.END))
            return  "break"
        except ValueError as e:
            showerror()

            change_size_input.delete('1.0', tk.END)
            change_size_input.insert(tk.END, str(reg_size))
            return  "break"
        finally:
            change_size_input.tag_remove("sel", "1.0", "end")
            main_input.mark_set("sel", "1.0")
            main_input.focus_set()

    def click_on_main_input(event):
        if change_size_input.get('1.0', tk.END) != reg_size:
            change_size_input.delete('1.0', tk.END)
            change_size_input.insert(tk.END, str(reg_size))

    def apply_font(event=None):
        nonlocal font
        selected = combo_of_fonts.get().strip()
        if selected in all_fonts:
            font = selected
        else:
            current = combo_of_fonts['values']
            if current:
                print(selected)

    red_win = tk.Tk()
    red_win.geometry('600x800')
    red_win.title("*New File")
    red_win.configure(bg="#6155F5")
    red_win.resizable(False, False)

    all_fonts = sorted(tkfont.families())

    main_input = tk.Text(red_win, font=('Arial', 14), bg='black', fg='white', borderwidth=0, height=30, width=55)
    main_input.place(x=0, y=50)
    main_input.bind('<Button-1>', click_on_main_input)

    btn1 = tk.Button(text='Сохранить', font=("Arial", 14, "bold"), bg = '#D4A843', command=lambda: save_file(key = key,
                                                            text_widget=main_input,
                                                            filepath= asksaveasfilename(title='Выберите место сохранения', filetypes = [('STDFS Files', '.stdfs')]),
                                                            tags_list= tags,
                                                            window_widget = red_win
                                                            )
                     )
    btn1.place(x=100, y=735)
    btn2 = tk.Button(text='Загрузить файл', font=("Arial", 14, "bold"),  bg = '#D4A843'  , command=lambda: tags == load_file(key = key,
                                                       text_widget=main_input,
                                                       filepath=askopenfilename(title='Выберете файл', filetypes = [('STDFS Files', '.stdfs')]),
                                                       window_widget=red_win
                                                       )
                     )
    btn2.place(x=350, y=735)

    bt3 = tk.Button(text='Изменить текст', command=change_tags_list)
    bt3.place(x=500, y=25, anchor='center')

    bold_btn = tk.Button(text='Ж',font=('Arial', 10, 'bold'), command= lambda: change_type('bold') )
    bold_btn.place(x=100, y=25, anchor='center')

    italic_btn = tk.Button(text='К',font=('Arial', 10, 'italic'), command= lambda: change_type('italic') )
    italic_btn.place(x=130, y=25, anchor='center')

    underline_btn = tk.Button(text='Н',font=('Arial', 10, 'underline'), command= lambda: change_type('underline') )
    underline_btn.place(x=160, y=25, anchor='center')

    combo_of_fonts = ttk.Combobox(red_win, values=all_fonts, state="normal", width=30, font=("Arial", 10))
    combo_of_fonts.place(x=200, y =15)
    combo_of_fonts.set('Arial')
    combo_of_fonts.bind("<<ComboboxSelected>>", apply_font)
    combo_of_fonts.bind("<Return>", apply_font)
    combo_of_fonts.bind("<FocusOut>", apply_font)

    change_size_input = tk.Text(red_win, height=1, width=3, font=('Dela Gothic One', 15))
    change_size_input.insert(tk.END, '14')
    change_size_input.bind('<Return>', enter_size)
    change_size_input.place(x=8, y=8)
    if path_to_file:
        tags, password = load_file(key=key, text_widget=main_input, filepath=path_to_file, window_widget=red_win)

    list_types = {
        "bold" : [False, bold_btn],
        "italic" : [False, italic_btn],
        "underline" : [False, underline_btn],
    }

    red_win.mainloop()

if __name__ == '__main__':
    red_window_def()
