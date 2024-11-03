import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            result_text = f"Your BMI is {bmi:.2f} (Underweight)"
        elif 18.5 <= bmi < 24.9:
            result_text = f"Your BMI is {bmi:.2f} (Normal weight)"
        elif 25 <= bmi < 29.9:
            result_text = f"Your BMI is {bmi:.2f} (Overweight)"
        else:
            result_text = f"Your BMI is {bmi:.2f} (Obese)"

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()