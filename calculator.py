import tkinter as tk
import sympy as sp

# Function to update expression and insert at cursor position
def press(value):
    current = equation.get()
    if current == "Error":
        equation.set(str(value))
    else:
        try:
            cursor_pos = text_field.index(tk.INSERT)
            text_field.insert(cursor_pos, str(value))
        except Exception:
            equation.set(current + str(value))

# Function to evaluate the final expression symbolically (Casio-style)
def equalpress(event=None):
    try:
        expr = equation.get()
        
        # Translate visual math symbols to SymPy executable syntax
        expr = expr.replace('√', 'sqrt')
        expr = expr.replace('^', '**')
        
        # Parse and symbolically evaluate the expression using SymPy
        result = sp.sympify(expr)
        
        # Format the result nicely
        equation.set(str(result))
        text_field.icursor(tk.END)
    except Exception:
        equation.set("Error")

# Function to clear the contents
def clear():
    equation.set("")

# Main window setup
root = tk.Tk()
root.title("First Program ")
root.geometry("500x680")
root.configure(bg="#301934")
root.resizable(True, True)

# Configure window grid scaling
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

equation = tk.StringVar()

# Display screen frame
display_frame = tk.Frame(root, bg="#301934")
display_frame.pack(pady=20, padx=20, fill="x")

text_field = tk.Entry(
    display_frame, 
    textvariable=equation, 
    font=('Segoe UI', 26, 'bold'), 
    justify='right', 
    bg="#221126", 
    fg="#ffffff", 
    bd=0,
    insertbackground="#ffffff"
)
text_field.pack(ipady=15, fill="x")

# Buttons frame that expands flexibly
buttons_frame = tk.Frame(root, bg="#301934")
buttons_frame.pack(padx=20, pady=5, fill="both", expand=True)

# Make grid rows/columns expandable
for i in range(6):
    buttons_frame.rowconfigure(i, weight=1)
for j in range(4):
    buttons_frame.columnconfigure(j, weight=1)

# Button layout definition: (Text, Row, Col, Background Color, Text Color)
buttons = [
    ('C', 0, 0, "#4a2c59", "#ff8080"),
    ('(', 0, 1, "#4a2c59", "#80bfff"),
    (')', 0, 2, "#4a2c59", "#80bfff"),
    ('/', 0, 3, "#5c3a70", "#ffaa80"),

    ('7', 1, 0, "#3d1a4c", "#ffffff"),
    ('8', 1, 1, "#3d1a4c", "#ffffff"),
    ('9', 1, 2, "#3d1a4c", "#ffffff"),
    ('*', 1, 3, "#5c3a70", "#ffaa80"),

    ('4', 2, 0, "#3d1a4c", "#ffffff"),
    ('5', 2, 1, "#3d1a4c", "#ffffff"),
    ('6', 2, 2, "#3d1a4c", "#ffffff"),
    ('-', 2, 3, "#5c3a70", "#ffaa80"),

    ('1', 3, 0, "#3d1a4c", "#ffffff"),
    ('2', 3, 1, "#3d1a4c", "#ffffff"),
    ('3', 3, 2, "#3d1a4c", "#ffffff"),
    ('+', 3, 3, "#5c3a70", "#ffaa80"),

    ('0', 4, 0, "#3d1a4c", "#ffffff"),
    ('.', 4, 1, "#3d1a4c", "#ffffff"),
    ('^', 4, 2, "#4a2c59", "#80ffaa"),  # Power button
    ('√', 4, 3, "#4a2c59", "#80ffaa"),  # Square root button
]

# Create standard grid buttons with sticky expansion
for (text, row, col, bg_col, fg_col) in buttons:
    if text == '√':
        cmd = lambda: press('√(')  # Inserts clean root symbol instead of code text
    elif text == '^':
        cmd = lambda: press('^')
    elif text == 'C':
        cmd = clear
    else:
        cmd = lambda t=text: press(t)

    btn = tk.Button(
        buttons_frame, 
        text=text, 
        font=('Segoe UI', 16, 'bold'), 
        bg=bg_col, 
        fg=fg_col, 
        bd=0,
        activebackground="#6c3a80",
        activeforeground=fg_col,
        command=cmd
    )
    btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

# Equals button spanning across the bottom row
equal_btn = tk.Button(
    buttons_frame, 
    text="=", 
    font=('Segoe UI', 18, 'bold'), 
    bg="#ffaa80", 
    fg="#301934", 
    bd=0,
    activebackground="#ffc4a3",
    activeforeground="#301934",
    command=equalpress
)
equal_btn.grid(row=5, column=0, columnspan=4, padx=4, pady=4, sticky="nsew")

# Bind Enter key on keyboard to trigger equalpress
root.bind('<Return>', equalpress)

# Glowing darkish purple signature label at the bottom right corner
signature_label = tk.Label(
    root, 
    text="made by Ibrahim", 
    font=('Segoe UI', 10, 'bold italic'), 
    bg="#301934", 
    fg="#000000"  # Luminous glowing dark purple / violet
)
signature_label.pack(side="bottom", anchor="se", padx=15, pady=8)

root.mainloop()