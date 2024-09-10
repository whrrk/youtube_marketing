import tkinter as tk

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
tk.Label(root, text="Number 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Number 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

add_button = tk.Button(root, text="Add", command=add)
add_button.pack(pady=5)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack(pady=5)

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=20)

# Run the application
root.mainloop()