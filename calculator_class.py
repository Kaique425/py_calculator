import re
import tkinter as tk
from typing import List


class Calculator:
    """Documentation"""

    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]],
    ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button["text"]

                if button_text == "C":
                    button.bind("<Button-1>", self.clear_display)

                if button_text in "01234567890.*-+/()":
                    button.bind("<Button-1>", self.add_text_to_display)

                if button_text == "=":
                    button.bind("<Button-1>", self.calculate)

    def _config_display(self):
        pass

    def clean_text(self, text):
        # Substitui tudo que não seja 0123456789./-+*^
        text = re.sub(r"[^\d\.\/\\*\-\+\^e]", r"", text, 0)
        # Substitui sinais repetidos.
        text = re.sub(r"([\.\+\/\*\-\^])\1+", r"\1", text, 0)
        # Remove () ou *() pra nada.
        text = re.sub(r"\*?\(\)", r"", text, 0)

        return text

    def clear_display(self, event=None):
        self.display.delete(0, "end")

    def add_text_to_display(self, event=None):
        """O event retorna exatamente o botão pressionado"""
        self.display.insert(0, event.widget["text"])
        self.display.focus()

    def calculate(self, event=None):
        cleaned_text = self.clean_text(self.display.get())
        print(cleaned_text)
