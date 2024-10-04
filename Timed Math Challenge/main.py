import tkinter as tk
from start_screen import StartScreen

# Screens - Start (Default), Quiz
def main():
    root = tk.Tk()
    root.title("Math Quiz Game")
    root.geometry("1000x1000")

    StartScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()