import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

ARCHIVO = "ventas.txt"


def guardar_venta(tipo, precio, fecha, cliente, entrega):
    """Agrega una venta al archivo. Devuelve True si se guardó correctamente."""
    try:
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{tipo} \t {precio} \t {fecha}  \t {cliente} \t {entrega} \n")
        return True
    except PermissionError:
        messagebox.showerror("Error", "Error en los permisos del archivo.")
    except OSError as error:
        messagebox.showerror("Error", f"Problemas con el archivo usando el SO:\n{error}")
    return False


def leer_ventas():
    """Devuelve la lista de ventas guardadas (cada una como lista de campos)."""
    ventas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = [c.strip() for c in linea.rstrip("\n").split("\t")]
                if any(campos):
                    ventas.append(campos)
    except FileNotFoundError:
        pass
    except OSError as error:
        messagebox.showerror("Error", f"No se pudo leer el archivo:\n{error}")
    return ventas


class AppVentas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de ventas de madera")
        self.geometry("720x480")
        self.minsize(640, 420)

        self._crear_formulario()
        self._crear_tabla()
        self.cargar_tabla()

    # ---------- Interfaz ----------
    def _crear_formulario(self):
        marco = ttk.LabelFrame(self, text="Nueva venta", padding=10)
        marco.pack(fill="x", padx=10, pady=10)
        marco.columnconfigure(1, weight=1)

        self.var_tipo = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_fecha = tk.StringVar(value=date.today().strftime("%d/%m/%Y"))
        self.var_cliente = tk.StringVar()
        self.var_entrega = tk.StringVar()

        campos = [
            ("Tipo de madera:", self.var_tipo),
            ("Valor de la venta:", self.var_precio),
            ("Fecha de la venta:", self.var_fecha),
            ("Cliente:", self.var_cliente),
            ("Condición de entrega:", self.var_entrega),
        ]
        self.entradas = []
        for fila, (texto, variable) in enumerate(campos):
            ttk.Label(marco, text=texto).grid(row=fila, column=0, sticky="w", pady=3, padx=(0, 10))
            entrada = ttk.Entry(marco, textvariable=variable)
            entrada.grid(row=fila, column=1, sticky="ew", pady=3)
            self.entradas.append(entrada)

        botones = ttk.Frame(marco)
        botones.grid(row=len(campos), column=0, columnspan=2, pady=(10, 0), sticky="e")
        ttk.Button(botones, text="Registrar venta", command=self.registrar).pack(side="left", padx=5)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)

        self.entradas[0].focus()
        self.bind("<Return>", lambda e: self.registrar())

    def _crear_tabla(self):
        marco = ttk.LabelFrame(self, text="Ventas registradas", padding=10)
        marco.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        columnas = ("tipo", "precio", "fecha", "cliente", "entrega")
        encabezados = ("Tipo de madera", "Valor", "Fecha", "Cliente", "Entrega")
        self.tabla = ttk.Treeview(marco, columns=columnas, show="headings")
        for col, enc in zip(columnas, encabezados):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=120, anchor="w")

        scroll = ttk.Scrollbar(marco, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    # ---------- Lógica ----------
    def registrar(self):
        tipo = self.var_tipo.get().strip()
        precio = self.var_precio.get().strip()
        fecha = self.var_fecha.get().strip()
        cliente = self.var_cliente.get().strip()
        entrega = self.var_entrega.get().strip()

        if not all((tipo, precio, fecha, cliente, entrega)):
            messagebox.showwarning("Datos incompletos", "Completá todos los campos.")
            return

        try:
            float(precio.replace(",", "."))
        except ValueError:
            messagebox.showwarning("Valor inválido", "El valor de la venta debe ser un número.")
            return

        if guardar_venta(tipo, precio, fecha, cliente, entrega):
            self.cargar_tabla()
            self.limpiar()
            messagebox.showinfo("Listo", "Venta registrada correctamente.")

    def limpiar(self):
        self.var_tipo.set("")
        self.var_precio.set("")
        self.var_fecha.set(date.today().strftime("%d/%m/%Y"))
        self.var_cliente.set("")
        self.var_entrega.set("")
        self.entradas[0].focus()

    def cargar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        for venta in leer_ventas():
            # Completa con vacíos si alguna línea vieja tiene menos campos
            venta = (venta + [""] * 5)[:5]
            self.tabla.insert("", "end", values=venta)


def main():
    app = AppVentas()
    app.mainloop()


if __name__ == "__main__":
    main()
