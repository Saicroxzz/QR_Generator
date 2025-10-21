# 🧾 Generador de Códigos QR (QR Generator)

Un proyecto en **Python** que permite generar **códigos QR** de manera rápida y sencilla a partir de una URL.
Incluye una **interfaz gráfica (GUI)** creada con **Tkinter** y utiliza las librerías **qrcode** y **Pillow (PIL)** para la generación y manipulación de las imágenes.

---

## 🧠 Descripción General

Este programa solicita al usuario una **URL**, genera automáticamente su **código QR** y lo **guarda en una carpeta "QR_Codes" ubicada en el Escritorio** del sistema.
Su diseño está orientado a la facilidad de uso y la portabilidad, ideal para usuarios que deseen generar QR sin necesidad de línea de comandos.

---

## ⚙️ Tecnologías y Librerías Utilizadas

| Librería       | Descripción                                                                               |
| -------------- | ----------------------------------------------------------------------------------------- |
| `qrcode`       | Genera el código QR a partir del texto o enlace proporcionado.                            |
| `Pillow (PIL)` | Permite trabajar con imágenes, manejar colores y guardar archivos en diferentes formatos. |
| `tkinter`      | Crea la interfaz gráfica de usuario (GUI).                                                |
| `os`           | Gestiona rutas y creación de directorios.                                                 |

---

## 🧩 Requisitos Previos

Asegúrate de tener instalado **Python 3.8 o superior**.
Luego instala las dependencias necesarias ejecutando en la terminal:

```bash
pip install qrcode[pil]
```

---

## 🚀 Ejecución del Proyecto

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Saicroxzz/QR_Generator.git
   ```
2. Ingresa a la carpeta del proyecto:

   ```bash
   cd QR_Generator
   ```
3. Ejecuta el archivo principal:

   ```bash
   python generador_qr_gui.py
   ```

---

## 💻 Interfaz Gráfica

La ventana principal contiene:

* Un **campo de texto** para ingresar la URL.
* Un **botón "Generar QR"** que crea el código QR automáticamente.

Una vez generado, el archivo se guarda en:

```
C:\Usuarios\<tu_usuario>\Escritorio\QR_Codes\qr.png
```

El programa notificará mediante una ventana emergente si la operación fue exitosa o si hubo algún error.

---

## 🧱 Estructura del Proyecto

```
QR_Generator/
│
├── generador_qr_gui.py     # Interfaz gráfica y lógica principal
├── qr.py                   # Módulo de generación de códigos QR
├── README.md               # Documentación del proyecto
└── requirements.txt        # Dependencias del proyecto
```

---

## 📸 Ejemplo de Uso

1. Ingresa una URL (por ejemplo: `https://www.google.com`).
2. Presiona **"Generar QR"**.
3. Se generará un archivo `qr.png` en la carpeta del escritorio:
   ![Ejemplo QR](https://upload.wikimedia.org/wikipedia/commons/6/6b/QRCode.png)

---

## 🔒 Manejo de Errores

El sistema valida:

* Que la URL no esté vacía.
* Que el directorio de salida exista (lo crea automáticamente si no existe).
* Excepciones en el proceso de guardado o creación del código QR.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente, siempre y cuando se mantenga el crédito al autor original.

---

## 👨‍💻 Autor

**Desarrollado por:** [Saicroxzz](https://github.com/Saicroxzz)
💡 *Proyecto educativo y de práctica con librerías gráficas y de manipulación de imágenes en Python.*
