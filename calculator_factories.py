import tkinter as tk

body_default_color = '#363636'


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx=10, pady=10, background=body_default_color)
    root.resizable(False, False)
    return root


def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text="Sem contas no momento",
        anchor='e', justify='right', background=body_default_color
    )
    label.grid(row=0, column=0, columnspan=5)
    return label
