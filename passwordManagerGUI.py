import sqlite3
import tkinter as tk
from passwordmanager import add_password, delete_password, change_password, get_password, create_table

db_name = "NewPasswort.db"


def show_frame1():
    # Blende das zweite Frame aus, falls es sichtbar ist
    passwoerter_Einsehen_Frame.pack_forget()
    # Zeige das erste Frame an
    passwort_Hinzufuegen_Frame.pack()


def show_frame2():
    # Blende das erste Frame aus, falls es sichtbar ist
    passwort_Hinzufuegen_Frame.pack_forget()
    # Zeige das zweite Frame an
    passwoerter_Einsehen_Frame.pack()


# Fenster erstellen
fenster = tk.Tk()
fenster.title("Passwort Manager")
fenster.geometry("500x500")

passwort_Hinzufuegen_Frame = tk.Frame()
passwoerter_Einsehen_Frame = tk.Frame()

passwort_Hinzufuegen_Frame.pack()

# Füge einen Button zu Frame 1 hinzu, der zum zweiten Frame wechselt
button1 = tk.Button(passwort_Hinzufuegen_Frame, text="Zur Übersicht", command=show_frame2)
button1.pack()
button2 = tk.Button(passwoerter_Einsehen_Frame, text="Passwörter Hinzufügen", command=show_frame1)
button2.pack()

username = tk.StringVar()
username.set("Bitte Username eingeben")

website = tk.StringVar()
website.set("Bitte Website eingeben")
# Alles Frame 1
ueberschrift1 = tk.Label(passwort_Hinzufuegen_Frame, text="Passwort Manager", font=("Arial", 20))
ueberschrift2 = tk.Label(passwort_Hinzufuegen_Frame, text="Passwort hinzufügen", font=("Arial", 16))

inputWebsite = tk.Entry(passwort_Hinzufuegen_Frame, width=50)
inputWebsite.insert(0, website.get())
inputWebsite.bind("<FocusIn>", lambda event: inputWebsite.delete('0', 'end'))

inputUsername = tk.Entry(passwort_Hinzufuegen_Frame, width=50)
inputUsername.insert(0, username.get())
inputUsername.bind("<FocusIn>", lambda event: inputUsername.delete('0', 'end'))

passwortHinzufuegenButton = tk.Button(passwort_Hinzufuegen_Frame, text="Passwort hinzufügen",
                                      command=lambda: add_password(db_name, inputWebsite.get(), inputUsername.get()))
ueberschrift1.pack()
ueberschrift2.pack()
inputWebsite.pack(padx=10, pady=10)
inputUsername.pack(padx=10, pady=10)
passwortHinzufuegenButton.pack(padx=10, pady=10)
button1.pack(padx=10, pady=10)

# Alles Frame 2
ueberschrift3 = tk.Label(passwoerter_Einsehen_Frame, text="Passwort Manager", font=("Arial", 20))
ueberschrift4 = tk.Label(passwoerter_Einsehen_Frame, text="Passwörter einsehen", font=("Arial", 16))
ueberschrift3.pack()
ueberschrift4.pack()

passwort_Hinzufuegen_Frame.tkraise()


def update_table():
    table.delete(0, tk.END)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT website, username, password FROM passwords")
    rows = c.fetchall()
    for row in rows:
        table.insert(tk.END, row)
    conn.close()


table = tk.Listbox(passwoerter_Einsehen_Frame, width=150)
table.pack()

update_table_button = tk.Button(passwoerter_Einsehen_Frame, text="Update Table", command=update_table)
update_table_button.pack()


table_test = tk.Listbox(passwoerter_Einsehen_Frame)


def main():
    update_table()
    fenster.mainloop()


if __name__ == "__main__":
    main()
