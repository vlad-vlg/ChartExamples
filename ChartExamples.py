# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart1

# Функция закратия программмы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry('450x450+300+200')
window.title('Примеры построения графиков')

# Добавление метки заголовка
lblTitle = tk.Label(window, text='Примеры построения графиков', font=('Helvetica', 16, 'bold'), fg='#0000cc')
lblTitle.place(x=55, y=25)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text='График 1', font=('Helvetica', 10, 'bold'), activebackground='gray85', command=chart1.plot_chart )
btnChart1.place(x=40, y=115, width=90, height=30)

lblChart1 = tk.Label(window, text='График синуса matplotlib')
lblChart1.place(x=170, y=122)


# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text='Закрыть', font=('Helvetica', 10, 'bold'), activebackground='gray85', command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
