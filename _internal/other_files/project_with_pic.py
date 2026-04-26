from _internal.other_files.other_fuctions import *
from tkinter.constants import HORIZONTAL

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


def project_main_pic(file):
    # Глобальные переменные для хранения последних координат
    '''---------------------------------------------------------------Переменные-------------------------------------------------------------------------------------'''
    global last_x, last_y, pen_draw, width_pen, clk_rubber, pen_color, bg_color, oval_var, cube_var, border_width, shape_color_fill, border_color, fon_now
    im = Image.open(file)
    width, height = im.size





    def cube():
        global cube_var, pen_draw
        cube_var = not cube_var
        pen_draw = False
        btn_pen_open['text'] = 'Взять перо'

    def add_random_circle():
        random_random_circle(canvas=canvas,border_color=border_color,shape_color_fill=shape_color_fill,border_width=border_width)

    def add_project_with_pic():
        add_project_with_pic___(name_window=project_window_with_pic)

    def oval():
        global  oval_var, pen_draw
        oval_var = not oval_var
        pen_draw = False
        btn_pen_open['text'] = 'Взять перо'

    def change_bg_color():
        change_bg_color__(name_window=project_window_with_pic,pen_color=pen_color,canvas=canvas)

    def change_pen_color():
        global pen_color
        pen_color = change_pen_color__(name_window=project_window_with_pic, bg_color=bg_color)

    def set_last_pos(event):
            global last_x, last_y
            last_x, last_y = event.x, event.y

    def editor_main():

        def change_width_shape(bor_new: int):
            global border_width
            border_width = bor_new
            #print(border_width)

        def scale_change__(args):
            global bor
            bor = int(args)
            #print(bor)
        def del_window():
            global border_width
            editor.grab_release()
            editor.destroy()
            change_width_shape(bor)

        def change_fill():
            global shape_color_fill
            editor.grab_set()
            new_color = askcolor()[1]
            if new_color:
                shape_color_fill = new_color
            editor.grab_release()

        def change_border():
            global border_color
            editor.grab_set()
            new_color = askcolor()[1]
            if new_color:
                border_color = new_color
            editor.grab_release()


        editor = tk.Toplevel()
        editor.grab_set()
        editor.geometry('300x300')
        scale_selection = tk.IntVar()
        editor.resizable(False, False)
        editor.title('Редактирование фигур')
        relative_path = os.path.join('_internal', 'IMG', 'ICO', 'MAIN_WINDOW.ico')
        full_path = os.path.abspath(relative_path)
        editor.iconbitmap(full_path)
        editor.protocol("WM_DELETE_WINDOW", del_window)

        border_scale = tk.Scale(from_=0, to=30, orient=HORIZONTAL, master=editor, variable=scale_selection,
                                command=scale_change__, label='Ширина границы фигуры')
        border_scale.pack()

        btn_change_color_shape_contur = tk.Button(master=editor,text='Изменить цвет контура', command=change_border)
        btn_change_color_shape_contur.pack()

        btn_change_color_shape_fill = tk.Button(master=editor, text='Изменить цвет заливки', command=change_fill)
        btn_change_color_shape_fill.pack()

        editor.mainloop()

    def stop_drawing(*args):
        """Отключение режима рисования овала."""
        global oval_var, cube_var
        oval_var = False
        cube_var = False

    def new_file():
        make_new_file(project_window_with_pic, canvas)

    def rubber(*args):
        global pen_draw, clk_rubber
        if clk_rubber is False:
            clk_rubber = True
            pen_draw = False
            btn_pen_open['text'] = 'Взять перо'
        else:
            clk_rubber = False

            selected_option.set(False)

    def save_canvas_():
        save_canvas(name_window=project_window_with_pic, canvas=canvas)

    def save_as_canvas_proj():
        save_as_canvas(project_window_with_pic,canvas)

    def del_():
        canvas.delete('all')
        add_image(file, canvas=canvas, fon_now=fon_now)

    def draw(event):
        #print(1)
        global last_x, last_y, oval_var, cube_var
        result = draw_something(event, pen_draw, clk_rubber, canvas, pen_color, width_pen, bg_color, border_color,
                                shape_color_fill, border_width, last_x, last_y, oval_var, cube_var)
        if pen_draw or clk_rubber:
            last_x, last_y = result
        elif oval_var:
            oval_var = result
        elif cube_var:
            cube_var = result

    def pen_open():
        global pen_draw, clk_rubber
        if pen_draw is True:
            btn_pen_open['text'] = 'Взять перо'
            pen_draw = False

        else:
            btn_pen_open['text'] = 'Опустить перо'
            pen_draw = True

            if clk_rubber is True:
                selected_option.set(False)

    def scale_change(args):
        global width_pen
        width_pen=int(args)

    def close():
        close_window(project_window_with_pic, canvas)

    """---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

    # Загружаем изображение с помощью PIL
    #print(f'Размеры изображения: {width}x{height}')

    # Создаём главное окно Tkinter
    project_window_with_pic = tk.Tk()
    project_window_with_pic.configure(bg='lightblue')
    project_window_with_pic.title('Проект...')
    selected_option = tk.IntVar(value=None)
    selected_option.trace_add('write', rubber)
    scale_var = tk.IntVar()

    difficult_window(project_window_with_pic, save_as_canvas_proj, save_canvas_, new_file, add_project_with_pic, owner, spravka, close)
    # Создаём Canvas для отображения изображения
    canvas = tk.Canvas(master=project_window_with_pic, bg=bg_color, width=700, height=700, borderwidth=2, highlightthickness=0)
    canvas.pack(side=tk.LEFT)

    add_image(file, canvas=canvas, fon_now=fon_now)


    if width >700 or height>700:
        showinfo(title='Ошибка размеров', message='Размер изображения больше холста, поэтому картинка будет обрезана относительно центра')


    btn_pen_open = tk.Button(master=project_window_with_pic, text='Взять перо', command=pen_open, font=font, bg='light grey')
    btn_pen_open.place(x=740, y=10)

    btn_rubber = tk.Radiobutton(project_window_with_pic, text='Ластик', value='python', variable=selected_option, font=font,
                                bg='light grey')
    btn_rubber.place(x=880, y=12)

    scale_width = tk.Scale(master=project_window_with_pic, length=170, orient=HORIZONTAL, from_=1, to=37, command=scale_change,
                           variable=scale_var, sliderlength=10, bg='light grey', label='Ширина рисования', font=font)
    scale_width.place(x=760, y=60)

    btn_color_pen = tk.Button(master=project_window_with_pic, text='Изменить цвет пера', font=font, command=change_pen_color,
                              bg='light grey')
    btn_color_pen.place(x=757, y=140)

    btn_color_bg = tk.Button(master=project_window_with_pic, text='Изменить цвет холста', font=font, command=change_bg_color,
                             bg='light grey')
    btn_color_bg.place(x=747, y=185)

    create_oval_btn = tk.Button(master=project_window_with_pic, text='Создать овал', font=font, background='light grey',
                                command=oval)
    create_oval_btn.place(x=730, y=250)

    bnt_crate_cube = tk.Button(master=project_window_with_pic, text='Создать куб', font=font, command=cube, background='light grey')
    bnt_crate_cube.place(x=860, y=250)

    btn_editor_shape = tk.Button(master=project_window_with_pic, text='Редактировать фигуры', font=font, command=editor_main, background='light grey')
    btn_editor_shape.place(x=750, y=295)

    btn_random_oval = tk.Button(master=project_window_with_pic, text='Создать рандомный круг \n в рандомном месте', font=font,
                                command=add_random_circle, background='light grey')
    btn_random_oval.place(x=740, y=340)

    delete_all_btn = tk.Button(master=project_window_with_pic, text='Удалить все', command=del_, font=font, bg='light grey')
    delete_all_btn.place(x=790, y=450)

    canvas.bind("<Button-1>", lambda event: set_last_pos(event))  # Нажатие кнопки мыши
    canvas.bind("<B1-Motion>", draw)  # Движение мыши при нажатии кнопки
    canvas.bind('<ButtonRelease-1>', stop_drawing)

    project_window_with_pic.mainloop()




if __name__ == "__main__":
    project_main_pic(None)