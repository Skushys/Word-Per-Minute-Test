import tkinter as tk
import time
import random

# List of prompts
prompts = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "Sphinx of black quartz, judge my vow.",
    "How razorback-jumping frogs can level six piqued gymnasts!"
]

# Select a prompt
prompt = random.choice(prompts)
start_time = 0

def start_typing():
    global start_time
    entry.config(state='normal')
    entry.delete(0, tk.END)
    result_label.config(text="")
    countdown_label.config(text="Typing starts in 3...")
    root.after(1000, lambda: countdown_label.config(text="Typing starts in 2..."))
    root.after(2000, lambda: countdown_label.config(text="Typing starts in 1..."))
    root.after(3000, begin_typing)

def begin_typing():
    global start_time
    countdown_label.config(text="Go!")
    entry.focus()
    start_time = time.time()

def check_result(event):
    end_time = time.time()
    typed = entry.get()
    elapsed = max(end_time - start_time, 0.01)
    word_count = len(prompt.split())
    wpm = (word_count / elapsed) * 60
    correct_chars = sum(1 for a, b in zip(typed, prompt) if a == b)
    accuracy = (correct_chars / len(prompt)) * 100
    result_label.config(
        text=f"Time: {elapsed:.2f}s | WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%"
    )

# GUI Setup
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x300")

prompt_label = tk.Label(root, text=prompt, font=("Arial", 14), wraplength=600, pady=20)
prompt_label.pack()

countdown_label = tk.Label(root, text="", font=("Arial", 12))
countdown_label.pack()

entry = tk.Entry(root, font=("Arial", 14), width=60, state='disabled')
entry.pack(pady=10)
entry.bind("<Return>", check_result)

start_button = tk.Button(root, text="Start Test", command=start_typing)
start_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

root.mainloop()