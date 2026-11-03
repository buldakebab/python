import tkinter as tk
from tkmacosx import Button
from tkinter import messagebox
import random

class SimonSaysApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Simon Says — Тренажёр памяти")
        self.root.geometry("420x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1b26")

        # Конфигурация 4 цветов: базовый оттенок и вспышка (подсветка)
        self.colors = {
            "red":    {"base": "#991b1b", "flash": "#ef4444"},
            "blue":   {"base": "#1e40af", "flash": "#3b82f6"},
            "green":  {"base": "#166534", "flash": "#22c55e"},
            "yellow": {"base": "#854d0e", "flash": "#eab308"}
        }
        self.color_keys = list(self.colors.keys())

        # Игровые переменные
        self.sequence = []           # Последовательность компьютера
        self.player_step = 0         # Текущий шаг игрока в раунде
        self.is_displaying = False   # Флаг показа (блокирует клики)

        self.setup_ui()

    def setup_ui(self):
        # Верхний лейбл статуса и счёта
        self.lbl_status = tk.Label(
            self.root,
            text="Нажми «Старт», чтобы начать",
            font=("Arial", 14, "bold"),
            fg="#c0caf5",
            bg="#1a1b26",
            wraplength=380
        )
        self.lbl_status.pack(pady=(20, 10))

        # Сетка кнопок 2x2
        grid_frame = tk.Frame(self.root, bg="#1a1b26")
        grid_frame.pack(pady=10)

        self.buttons = {}

        # Координаты кнопок в сетке
        positions = {
            "green":  (0, 0),
            "red":    (0, 1),
            "yellow": (1, 0),
            "blue":   (1, 1)
        }

        for color, (r, c) in positions.items():
            btn = Button(
                grid_frame,
                bg=self.colors[color]["base"],
                activebackground=self.colors[color]["flash"],
                width=10,
                height=5,
                relief="raised",
                bd=4,
                cursor="hand2",
                command=lambda clr=color: self.on_button_click(clr)
            )
            btn.grid(row=r, column=c, padx=8, pady=8)
            self.buttons[color] = btn

        # Нижняя кнопка запуска
        self.btn_start = tk.Button(
            self.root,
            text="▶ Старт игры",
            font=("Arial", 12, "bold"),
            bg="#9ece6a",
            fg="#1a1b26",
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.start_new_game
        )
        self.btn_start.pack(pady=20)

    def start_new_game(self):
        self.sequence = []
        self.btn_start.config(state="disabled")
        self.next_round()

    def next_round(self):
        self.player_step = 0
        self.is_displaying = True

        # Компьютер добавляет случайный цвет
        new_color = random.choice(self.color_keys)
        self.sequence.append(new_color)

        round_num = len(self.sequence)
        self.lbl_status.config(
            text=f"Раунд {round_num}: Запоминай порядок!",
            fg="#e0af68"
        )

        # Небольшая пауза перед началом показа
        self.root.after(800, lambda: self.play_sequence(0))

    def play_sequence(self, index):
        if index < len(self.sequence):
            color = self.sequence[index]
            self.flash_button(color)

            # Следующий цвет подсвечивается через 600 мс
            self.root.after(600, lambda: self.play_sequence(index + 1))
        else:
            # Показ завершён — ход переходит игроку
            self.is_displaying = False
            self.lbl_status.config(
                text=f"Твой ход! Раунд {len(self.sequence)}",
                fg="#7dcfff"
            )

    def flash_button(self, color):
        """Кратковременная подсветка кнопки."""
        btn = self.buttons[color]
        btn.config(bg=self.colors[color]["flash"])
        # Возвращаем исходный тёмный оттенок через 300 мс
        self.root.after(300, lambda: btn.config(bg=self.colors[color]["base"]))

    def on_button_click(self, color):
        # Игнорируем нажатия, пока играет компьютер или игра не запущена
        if self.is_displaying or not self.sequence:
            return

        # Подсвечиваем нажатую кнопку
        self.flash_button(color)

        # Проверка нажатия
        if color == self.sequence[self.player_step]:
            self.player_step += 1

            # Если игрок безошибочно повторил всю цепочку
            if self.player_step == len(self.sequence):
                self.is_displaying = True
                self.lbl_status.config(text="Верно! Отлично!", fg="#9ece6a")
                self.root.after(1000, self.next_round)
        else:
            self.game_over()

    def game_over(self):
        score = len(self.sequence) - 1
        self.lbl_status.config(text=f"Игра окончена! Счёт: {score}", fg="#f7768e")
        self.btn_start.config(state="normal", text="🔄 Играть снова")
        
        messagebox.showinfo(
            "Game Over",
            f"Вы ошиблись!\nВаш итоговый счёт: {score} очк."
        )
        self.sequence = []


if __name__ == "__main__":
    app_root = tk.Tk()
    game = SimonSaysApp(app_root)
    app_root.mainloop()