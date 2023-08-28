# Примеры построения графиков

import tkinter as tk

# Функция закратия программмы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry('450x450+300+200')
window.title('Примеры построения графиков')

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text='Закрыть', font=('Helvetica', 10, 'bold'), activebackground='gray80', command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
