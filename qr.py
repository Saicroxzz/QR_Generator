# generador_qr_gui.py
import qrcode
from PIL import Image
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def generar_qr(url: str, archivo_salida: str, tamaño_box: int = 10, borde: int = 4):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=tamaño_box,
        border=borde,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    carpeta = os.path.dirname(archivo_salida)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta, exist_ok=True)

    img.save(archivo_salida)
    return archivo_salida

def generar_desde_gui():
    url = entry_url.get().strip()
    if not url:
        messagebox.showwarning("Error", "Por favor ingresa una URL válida.")
        return

    # Carpeta de salida en el escritorio
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop", "QR_Codes")
    archivo_salida = os.path.join(escritorio, "qr.png")

    try:
        ruta = generar_qr(url, archivo_salida)
        messagebox.showinfo("Éxito", f"Código QR guardado en:\n{ruta}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el QR:\n{e}")

# Configuración de la ventana
root = tk.Tk()
root.title("Generador de QR")
root.geometry("400x150")
root.resizable(False, False)

# Etiqueta y entrada de URL
tk.Label(root, text="Ingresa la URL:").pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Botón para generar QR
tk.Button(root, text="Generar QR", command=generar_desde_gui).pack(pady=20)

root.mainloop()
