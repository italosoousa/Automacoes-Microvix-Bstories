import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Interface Automação")
root.geometry("800x500")

# Barra superior
top_bar = tk.Frame(root, height=40, highlightbackground="white", highlightthickness=1)
top_bar.pack(side="top", fill="x")

logo_label = tk.Label(top_bar, text="Logo", font=("Arial", 14))
logo_label.pack(side="left", padx=10, pady=5)

# Barra lateral esquerda
side_bar = tk.Frame(root, width=120, highlightbackground="white", highlightthickness=1)
side_bar.pack(side="left", fill="y")

for i in range(3):
    btn = tk.Button(side_bar, text=f"Botão {i+1}", width=12)
    btn.pack(pady=15, padx=10)

# Área principal
main_area = tk.Frame(root, highlightbackground="white", highlightthickness=1)
main_area.pack(side="left", fill="both", expand=True)

root.mainloop()