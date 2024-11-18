import tkinter as tk

# Konfiguracja stałych (przelicznik mm na piksele)
MM_TO_PIXELS = 3.7795275591  # 1 mm to około 3.78 pikseli
LINE_HEIGHT = 20  # wysokość linii oznaczeń
NUMBER_OFFSET = 10  # odstęp dla cyfr poniżej podziałki

# Funkcja aktualizacji linijki
def update_ruler(event):
    canvas.delete("all")
    width_cm = int(root.winfo_width() / (10 * MM_TO_PIXELS))  # szerokość linijki w cm

    # Rysowanie podziałki co 1 mm i numeracja co 1 cm
    for mm in range((width_cm + 1) * 10):
        x_position = mm * MM_TO_PIXELS

        # Krótkie linie dla milimetrów
        if mm % 10 == 0:
            canvas.create_line(x_position, 0, x_position, LINE_HEIGHT, fill="black", width=1)
            # Oznaczenie cyfr dla każdego centymetra
            canvas.create_text(x_position, LINE_HEIGHT + NUMBER_OFFSET, text=str(mm // 10), anchor="n", font=("Arial", 10))
        else:
            canvas.create_line(x_position, 0, x_position, LINE_HEIGHT // 2, fill="black", width=1)

# Ustawienia głównego okna
root = tk.Tk()
root.title("Linijka w milimetrach")
root.geometry("1280x100")  # Szerokość okna, wysokość wystarczająca dla oznaczeń

# Ustawienie przezroczystości okna (dla systemu Linux)
root.attributes("-alpha", 0.5)  # 0.0 to całkowita przezroczystość, 1.0 to pełna widoczność

# Płótno do rysowania podziałki
canvas = tk.Canvas(root, height=LINE_HEIGHT + NUMBER_OFFSET * 2, bg="white")
canvas.pack(fill="both", expand=True)

# Aktualizacja linijki przy zmianie rozmiaru okna
root.bind("<Configure>", update_ruler)

root.mainloop()
