from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox


class Producto:
    
    db_name = 'BaseDeDatos.db'
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Registro de productos')
    
        # Creando un contenedor
        frame = LabelFrame(self.wind, text='Registro de productos')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Ingreso nombre
        Label(frame, text='Nombre').grid(row=2, column=0)
        self.Nombre = Entry(frame)
        self.Nombre.focus()
        self.Nombre.grid(row=2, column=1)
        
        # Ingreso Precio
        Label(frame, text='Precio').grid(row=3, column=0)
        self.Precio = Entry(frame)
        self.Precio.grid(row=3, column=1)
        
        # Creando botones
        ttk.Button(frame, text='Guardar producto', command=self.agregar_producto).grid(row=4, columnspan=2, sticky=W+E)
        
        
        self.message = Label(text='', fg='red')
        self.message.grid(row=5, column=0, columnspan=2, sticky=W+E)
        
        # Crear una tabla
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=6, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)
        
        self.get_Productos()
        
        # Crear botones de eliminar y modificar debajo de la tabla
        ttk.Button(frame, text='Eliminar producto', command=self.confirmar_eliminar_producto).grid(row=7, column=0, sticky=W+E)
        ttk.Button(frame, text='Modificar producto', command=self.modificar_producto).grid(row=7, column=1, sticky=W+E)
        
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parameters)
            conn.commit()
            return resultado
     
    def get_Productos(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        query = 'SELECT * FROM Productos ORDER BY Nombre ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 'end', text=row[1], values=(row[2]))
        
    def agregar_producto(self):
        if self.validacion():
            query = 'INSERT INTO Productos VALUES (NULL, ?, ?)'
            parameters = (self.Nombre.get(), self.Precio.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Producto {} agregado satisfactoriamente'.format(self.Nombre.get())
            self.Nombre.delete(0, END)
            self.Precio.delete(0, END)
            self.get_Productos()
        else:
            self.message['text'] = 'Nombre y Precio son requeridos'
    
    def confirmar_eliminar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo('Eliminar producto', 'Selecciona un producto para eliminar')
            return
        
        confirmation = messagebox.askyesno('Eliminar producto', '¿Estás seguro que deseas eliminar este producto?')
        if confirmation:
            self.eliminar_producto()
    
    def eliminar_producto(self):
        selected_item = self.tree.selection()
        Nombre = self.tree.item(selected_item)['text']
        query = 'DELETE FROM Productos WHERE Nombre = ?'
        self.run_query(query, (Nombre,))
        self.get_Productos()
        
    def modificar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo('Modificar producto', 'Selecciona un producto para modificar')
            return
        
        Nombre = self.tree.item(selected_item)['text']
        Precio = self.tree.item(selected_item)['values'][0]
        
        self.edit_wind = Toplevel()
        self.edit_wind.title('Editar producto')
        
        # Nombre antiguo
        Label(self.edit_wind, text='Nombre antiguo:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=Nombre), state='readonly').grid(row=0, column=2)
        
        # Nuevo nombre
        Label(self.edit_wind, text='Nuevo nombre:').grid(row=1, column=1)
        new_nombre = Entry(self.edit_wind)
        new_nombre.grid(row=1, column=2)
        
        # Precio antiguo
        Label(self.edit_wind, text='Precio antiguo:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=Precio), state='readonly').grid(row=2, column=2)
        
        # Nuevo precio
        Label(self.edit_wind, text='Nuevo precio:').grid(row=3, column=1)
        new_precio = Entry(self.edit_wind)
        new_precio.grid(row=3, column=2)
        
        ttk.Button(self.edit_wind, text='Actualizar', command=lambda: self.actualizar_producto(new_nombre.get(), new_precio.get(), Nombre)).grid(row=4, columnspan=3, sticky=W+E)
        
    def actualizar_producto(self, new_nombre, new_precio, Nombre):
        query = 'UPDATE Productos SET Nombre = ?, Precio = ? WHERE Nombre = ?'
        parameters = (new_nombre, new_precio, Nombre)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.get_Productos()
        
    def validacion(self):
        return len(self.Nombre.get()) != 0 and len(self.Precio.get()) != 0
    

if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    window.mainloop()
