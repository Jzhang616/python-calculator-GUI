import tkinter as tk
from tkinter import messagebox

def click_btn(btn_text):
    global expression

    if btn_text == "CLEAR":
        expression = ""
        result_text.set("")
    elif btn_text == "DEL":
        expression = expression[:-1]
        result_text.set(expression)
    elif btn_text == "CALC":
        try:
            result_text.set(eval(expression))
            expression = str(eval(expression))
        except:
            messagebox.showerror("Error", "Invalid Input.")
            result_text.set("")
            expression = ""
    else:
        expression += btn_text
        result_text.set(expression)

expression = ""
root = tk.Tk()
root.title("Calculator")

result_text = tk.StringVar()
result_text.set("")

result_field = tk.Entry(root, textvariable=result_text, justify=tk.RIGHT, width=30)
result_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("0", 4, 0)
]

for button_text, row, column in buttons:
    btn = tk.Button(root, text=button_text, width=5, height=2, command=lambda text=button_text: click_btn(text))
    btn.grid(row=row, column=column)

operators = [("*", 1, 3), ("/", 2, 3), ("+", 3, 3), ("-", 4, 3)]

for operator, row, column in operators:
    btn = tk.Button(root, text=operator, width=5, height=2, command=lambda op=operator: click_btn(op))
    btn.grid(row=row, column=column)

parentheses = [("(", 4, 1), (")", 4, 2)]

for paren, row, column in parentheses:
    btn = tk.Button(root, text=paren, width=5, height=2, command=lambda p=paren: click_btn(p))
    btn.grid(row=row, column=column)

btn_clear = tk.Button(root, text="CLEAR", width=7, height=2, command=lambda: click_btn("CLEAR"))
btn_clear.grid(row=5, column=0)
btn_calculate = tk.Button(root, text="CALC", width=7, height=2, command=lambda: click_btn("CALC"))
btn_calculate.grid(row=5, column=1)
btn_delete = tk.Button(root, text="DEL", width=7, height=2, command=lambda: click_btn("DEL"))
btn_delete.grid(row=5, column=2)

root.mainloop()
