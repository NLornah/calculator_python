import tkinter as tk

window = tk.TK()
window.title = ("simple Calculator")
window.geometry + ("300*400")
window.configure(bg='#f2f2f2')

display = tk.Entry(window, width=16, font=('Arial', 20), bd = 10, insertwidth=4, justify='right' )
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]
for button in buttons :
    tk.Button(window, text.button, width=5, height=2, command=Iambda b=button: on_button_click(b))

 row_val = 1
 col_val = 0

 for button in buttons:
      tk.Button(window, text.button, width=5, height=2, command=Iambda b=button: on_button_click(b))
      col_val += 1
      if col_val > 3:
         col_val = 0
         row_val += 1

 def on_button_click(value):
    current_display = display.get()
    if value == '=':
        try:
            result = eval(current_display)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
         except Exeption as e:   
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.inser(tk.END, value)

 window.mainloop()       


