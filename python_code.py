import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

class WordFinderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Finder Game")
        self.matrix_size = 10
        self.word_list = ["PYTHON", "JAVA", "CPLUSPLUS", "HTML", "CSS", "JAVASCRIPT", "RUBY", "PHP", "SWIFT", "GO"]
        self.matrix = [['' for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]
        self.populate_matrix()
        self.current_word = None
        self.cursor_pos = (0, 0)  # Initialize cursor position
        self.create_widgets()

    def populate_matrix(self):
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                self.matrix[i][j] = chr(random.randint(65, 90))  # Random uppercase letter

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.draw_matrix()
        self.search_button = tk.Button(self.master, text="Search", command=self.start_search)
        self.search_button.pack()

    def draw_matrix(self):
        self.canvas.delete("all")
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                self.canvas.create_rectangle(40 * j, 40 * i, 40 * (j + 1), 40 * (i + 1), outline="black")
                self.canvas.create_text(40 * j + 20, 40 * i + 20, text=self.matrix[i][j], font=("Arial", 16))

    def start_search(self):
        self.current_word = simpledialog.askstring("Input", "Enter the word to search:")
        if self.current_word:
            found = self.search_word(self.current_word)
            if found:
                messagebox.showinfo("Word Found", "Word found: " + self.current_word)
            else:
                messagebox.showinfo("Word Not Found", "Word not found: " + self.current_word)
        else:
            messagebox.showinfo("Error", "Please enter a word.")

    def search_word(self, word):
        self.clear_highlights()
        # Horizontal search
        for i in range(self.matrix_size):
            row = ''.join(self.matrix[i])
            index = self.kmp_search(row, word)
            if index != -1:
                self.highlight_found_cells(i, index, len(word), direction="HORIZONTAL")
                return True
        
        # Vertical search
        for j in range(self.matrix_size):
            col = ''.join(self.matrix[i][j] for i in range(self.matrix_size))
            index = self.kmp_search(col, word)
            if index != -1:
                self.highlight_found_cells(index, j, len(word), direction="VERTICAL")
                return True
        
        # Diagonal search
        for i in range(self.matrix_size - len(word) + 1):
            for j in range(self.matrix_size - len(word) + 1):
                diag = ''.join(self.matrix[i + k][j + k] for k in range(len(word)))
                if self.kmp_search(diag, word) != -1:
                    self.highlight_found_cells(i, j, len(word), direction="DIAGONAL")
                    return True
        
        return False

    def kmp_search(self, text, pattern):
        def compute_prefix_function(pattern):
            prefix_function = [0] * len(pattern)
            k = 0
            for q in range(1, len(pattern)):
                while k > 0 and pattern[k] != pattern[q]:
                    k = prefix_function[k - 1]
                if pattern[k] == pattern[q]:
                    k += 1
                prefix_function[q] = k
            return prefix_function

        prefix_function = compute_prefix_function(pattern)
        q = 0
        for i in range(len(text)):
            while q > 0 and pattern[q] != text[i]:
                q = prefix_function[q - 1]
            if pattern[q] == text[i]:
                q += 1
            if q == len(pattern):
                return i - len(pattern) + 1
        return -1

    def highlight_found_cells(self, start_row, start_col, length, direction):
        if direction == "HORIZONTAL":
            for i in range(length):
                self.canvas.create_rectangle(40 * (start_col + i), 40 * start_row, 40 * (start_col + i + 1), 40 * (start_row + 1), outline="red", width=2)
        elif direction == "VERTICAL":
            for i in range(length):
                self.canvas.create_rectangle(40 * start_col, 40 * (start_row + i), 40 * (start_col + 1), 40 * (start_row + i + 1), outline="red", width=2)
        elif direction == "DIAGONAL":
            for i in range(length):
                self.canvas.create_rectangle(40 * (start_col + i), 40 * (start_row + i), 40 * (start_col + i + 1), 40 * (start_row + i + 1), outline="red", width=2)
        self.canvas.update()
        time.sleep(0.2)

    def clear_highlights(self):
        self.draw_matrix()

def main():
    root = tk.Tk()
    game = WordFinderGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
