import sqlite3
import tkinter as tk
from tkinter import messagebox

#database and table
def buat_database():
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()

    # Buat tabel
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        alamat TEXT NOT NULL,
        no_telp TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

#CRUD
def insert_contacts(nama, alamat, no_telp, email):
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO contacts (nama, alamat, no_telp, email)
    VALUES (?, ?, ?, ?)
    ''', (nama, alamat, no_telp, email))
    
    conn.commit()
    conn.close()

def retrieve_contacts():
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    
    conn.close()
    return rows

def update_contact(id, nama, alamat, no_telp, email):
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE contacts
    SET nama = ?, alamat = ?, no_telp = ?, email = ?
    WHERE id = ?
    ''', (nama, alamat, no_telp, email, id))
    
    conn.commit()
    conn.close()

def delete_contact(id):
    conn = sqlite3.connect('address_book.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()

#GUI
def insert_contacts_gui(nama, alamat, no_telp, email):
    insert_contacts(nama, alamat, no_telp, email)
    refresh_contacts_list()

def refresh_contacts_list():
    contacts_list.delete(0, tk.END)
    for row in retrieve_contacts():
        contacts_list.insert(tk.END, row)

def on_add():
    insert_contacts_gui(entry_nama.get(), entry_alamat.get(), entry_no_telp.get(), entry_email.get())
    entry_nama.delete(0, tk.END)
    entry_alamat.delete(0, tk.END)
    entry_no_telp.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def on_update():
    selected = contacts_list.curselection()
    if selected:
        contact_id = contacts_list.get(selected[0])[0]
        update_contact(contact_id, entry_nama.get(), entry_alamat.get(), entry_no_telp.get(), entry_email.get())
        refresh_contacts_list()

def on_delete():
    selected = contacts_list.curselection()
    if selected:
        contact_id = contacts_list.get(selected[0])[0]
        delete_contact(contact_id)
        refresh_contacts_list()

#application
buat_database()

root = tk.Tk()
root.title("Address Book")
root.configure(bg="lightpink")

#user input form
tk.Label(root, text="Nama", bg="lightpink", fg="black").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Alamat", bg="lightpink", fg="black").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="No Telp", bg="lightpink", fg="black").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Email", bg="lightpink", fg="black").grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_nama = tk.Entry(root)
entry_alamat = tk.Entry(root)
entry_no_telp = tk.Entry(root)
entry_email = tk.Entry(root)

entry_nama.grid(row=0, column=1, padx=10, pady=5)
entry_alamat.grid(row=1, column=1, padx=10, pady=5)
entry_no_telp.grid(row=2, column=1, padx=10, pady=5)
entry_email.grid(row=3, column=1, padx=10, pady=5)

#button
tk.Button(root, text="Add", command=on_add, bg="white", fg="green").grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Update", command=on_update, bg="white", fg="blue").grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Delete", command=on_delete, bg="white", fg="red").grid(row=4, column=2, padx=10, pady=5)

#contact list
contacts_list = tk.Listbox(root)
contacts_list.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
refresh_contacts_list()

root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()