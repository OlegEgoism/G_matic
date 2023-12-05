import tkinter as tk
import random
import time

counter = 0
total_examples = 0
selected_labels = [None, None]
number_labels = []
answer_given = False


def get_numbers():
    """Указываем диапазон чисел"""
    global start_number, end_number
    start_number = start_number_entry.get()
    end_number = end_number_entry.get()
    if not start_number:
        start_number = 1
    if not end_number:
        end_number = 99
    instructions_window.destroy()
    root.deiconify()


instructions_window = tk.Tk()
instructions_window.title("Иснтрукция")
instructions_window.geometry("400x320")
instructions_window.resizable(False, False)
instructions_label = tk.Label(
    instructions_window,
    text="Задайте диапазон чисел от - до.\n"
         "Нажмите на кнопку 'Следующий'. \n"
         "У вас появятся девять случайных чисел. \n"
         "Найдите сумму двух чисел заданного числа. \n"
         "Выберете два числа, при нажатии на них \n"
         "они будут отмечены желтым цветом. \n"
         "Нажмите на кнопку 'Ответ'. \n"
         "Если ответ правильный жмите кнопку 'Следующий' \n",
    font=("Arial", 12))
instructions_label.pack()
start_number_text = tk.Label(instructions_window, text="От")
start_number_text.pack(side=tk.TOP)
start_number_entry = tk.Entry(instructions_window)
start_number_entry.pack(side=tk.TOP)
end_number_text = tk.Label(instructions_window, text="До")
end_number_text.pack(side=tk.TOP)
end_number_entry = tk.Entry(instructions_window)
end_number_entry.pack(side=tk.TOP)
ok_button = tk.Button(instructions_window, text="OK", command=get_numbers, font=("Arial", 14))
ok_button.pack(side=tk.BOTTOM, pady=10)


def generate_random_numbers():
    """Создание рандомных чисел в полях"""
    global selected_labels, total_examples, answer_given
    answer_given = False
    calculate_button.config(state=tk.NORMAL)
    selected_labels = [None, None]
    for label in number_labels:
        label.config(bg="lightgray")
    random_numbers = [random.randint(int(start_number), int(end_number)) for _ in range(9)]
    print('Случайные числа', random_numbers)
    for i, label in enumerate(number_labels):
        label.config(text=str(random_numbers[i]))
    selected = random.sample(random_numbers, 2)
    print('Выбранные числа', selected)
    print('Сумма ', sum(selected))
    random_sum_label.config(text=f"Сумма: {sum(selected)}", fg='Purple')
    total_examples += 1
    total_examples_label.config(text=f"Всего: {total_examples}")
    sum_label.config(text="Сумма: ")
    correctness_label.config(text="")


def calculate_and_display_sum():
    global counter, answer_given
    selected_numbers = [int(label.cget("text")) for label in selected_labels if label is not None]

    if len(selected_numbers) == 2:
        total_sum = sum(selected_numbers)
        print('Ответ ', total_sum)
        sum_label.config(text=f"Сумма: {total_sum}")
        if total_sum == int(random_sum_label["text"].split(": ")[1]):
            correctness_label.config(text="Правильно", fg='green')
            counter += 1
            counter_label.config(text=f"Правильные: {counter}")
        else:
            correctness_label.config(text="Не верно!!!", fg='red')
        answer_given = True
        calculate_button.config(state=tk.DISABLED)
    elif len(selected_numbers) == 1 and not answer_given:
        sum_label.config(text="Укажи 2 числа", fg='red')
        correctness_label.config(text="")
    else:
        answer_given = True
        calculate_button.config(state=tk.DISABLED)


def select_number(event):
    """Сумма чисел"""
    label = event.widget
    if label not in selected_labels:
        if None in selected_labels:
            idx = selected_labels.index(None)
            selected_labels[idx] = label
            label.config(bg="yellow")
        else:
            sum_label.config(text="Укажи 2 числа", fg='red')
    else:
        selected_labels[selected_labels.index(label)] = None
        label.config(bg="lightgray")
        sum_label.config(text="Сумма: ")


def update_time():
    """Таймер времени в секундах"""
    current_time = int(time.time() - start_time)
    time_label.config(text=f"{current_time} сек.")
    root.after(1000, update_time)


root = tk.Tk()
root.title("Математическая тренировка на сложение")
root.geometry("500x510")
root.resizable(False, False)

for i in range(3):
    for j in range(3):
        label = tk.Label(root, width=10, height=3, relief="solid", font=("Arial", 18), bg="lightgray")
        label.grid(row=i, column=j, padx=10, pady=10)
        label.bind("<Button-1>", select_number)
        number_labels.append(label)

"""Кнопки и поля для отображения"""
generate_button = tk.Button(root, text="Следующий", command=generate_random_numbers)
generate_button.grid(row=3, column=0, pady=5)
random_sum_label = tk.Label(root, text="Сумма: ", font=("Arial", 16))
random_sum_label.grid(row=3, column=1, pady=5)

calculate_button = tk.Button(root, text="Ответ", command=calculate_and_display_sum)
calculate_button.grid(row=4, column=0, pady=5)
sum_label = tk.Label(root, text="Сумма: ", font=("Arial", 16))
sum_label.grid(row=4, column=1, pady=5)
correctness_label = tk.Label(root, text="", font=("Arial", 16))
correctness_label.grid(row=4, column=2, pady=5)

total_examples_label = tk.Label(root, text=f"Всего: {total_examples}", font=("Arial", 16))
total_examples_label.grid(row=5, column=0, pady=5)
counter_label = tk.Label(root, text=f"Решено: {counter}", font=("Arial", 16))
counter_label.grid(row=5, column=1, pady=5)

start_time = time.time()
time_label = tk.Label(root, text=f"{time}", font=("Arial", 10), fg='blue')
time_label.grid(row=6, column=0, pady=5)
root.after(1000, update_time)

prod = tk.Label(root, text=f"Pustovalov®", font=("Arial", 8))
prod.grid(row=8, column=2, pady=2)

root.mainloop()
