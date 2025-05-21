# import tkinter as tk
# from tkinter import ttk

# def convert_currency():
#     try:
#         amount = float(amount_entry.get())
#         currency = currency_var.get()
#         result = amount * exchange_rates[currency]
#         result_label.config(text=f"Result: {result:.2f} {currency}")
#     except ValueError:
#         result_label.config(text="Write the correct number")

# exchange_rates = {
#     "EUR": 1,
#     "JPY": 163.5,
#     "USD": 1.1,
#     "GBP": 0.85,
# }

# root = tk.Tk()
# root.title("Convertor of the money")
# root.geometry("300x200")

# tk.Label(root, text="Write the sum (EUR):").pack()
# amount_entry = tk.Entry(root)
# amount_entry.pack()

# currency_var = tk.StringVar(value="JPY")
# tk.Label(root, text="Choose which countries money do you need:").pack()
# currency_menu = ttk.Combobox(root, textvariable=currency_var, values=list(exchange_rates.keys()))
# currency_menu.pack()

# tk.Button(root, text="Convert", command=convert_currency).pack()

# result_label = tk.Label(root, text="Result: ")
# result_label.pack()

# root.mainloop()



































#teht2

# root = Tk()
# root.title("Calculator")
# root.geometry("300x400")
# button = Button(root, text="+", font="30")
# button.pack(side="right", pady=40)
# button2 = Button(root, text="-", font="30")
# button2.pack(side="right", pady=20, padx=20, )

# button3 = Button(root, text="*", font="30")
# button3.pack(side="right", pady=10, padx="0", )

# button4 = Button(root, text="/", font="30")
# button4.pack(side="right", pady=10, padx="20", )

# def get_input():
#     user_text = entry.get()  # Получаем текст из поля ввода
#     label_result.config(text=f"Write second number")  # Выводим текст в Label

# # Создаём главное окно


# # Поле ввода
# entry = Entry(root, width=30)
# entry.pack(pady=10)

# # Кнопка для ввода
# button = Button(root, text="Ввести", command=get_input)
# button.pack()

# # Метка для вывода введённого текста
# label_result = Label(root, text="")
# label_result.pack(pady=10)

# # Запуск главного цикла Tkinter
# root.mainloop()

   
# root.mainloop()


# #first we enter the first number than second than what we want to do with it


