import customtkinter as ctk
from tkinter import ttk  # Importing ttk for Treeview

# Example data
database = [
    {"Nom": "Ali", "Prénom": "Ahmed", "Date de naissance": "1990-01-01", "Email": "ali@gmail.com", "Téléphone": "0555123456",
     "NIN": "12345678901234", "Ville": "Alger", "Commune": "Bab El Oued", "Type": "F3"},
    {"Nom": "Sara", "Prénom": "Mohamed", "Date de naissance": "1995-05-20", "Email": "sara@gmail.com", "Téléphone": "0666987654",
     "NIN": "98765432109876", "Ville": "Oran", "Commune": "Es Senia", "Type": "F2"},
    {"Nom": "Khaled", "Prénom": "Hassan", "Date de naissance": "1988-10-15", "Email": "khaled@gmail.com", "Téléphone": "0777234567",
     "NIN": "11112222333344", "Ville": "Alger", "Commune": "El Harrach", "Type": "F4"},
    {"Nom": "Yasmine", "Prénom": "Samir", "Date de naissance": "1992-07-30", "Email": "yasmine@gmail.com", "Téléphone": "0777123456",
     "NIN": "44445555666677", "Ville": "Alger", "Commune": "Bab El Oued", "Type": "F3"}
]

# Function to fetch data from "database" based on city and municipality
def fetch_data(ville, commune):
    results = [row for row in database if row["Ville"] == ville and row["Commune"] == commune]
    return results

# Function to display data in a new window
def show_data():
    ville = entry_ville.get().strip()
    commune = entry_commune.get().strip()

    # Validate input
    if not ville or not commune:
        ctk.CTkMessagebox(title="Erreur", message="Veuillez entrer la ville et la commune.", icon="warning")
        return

    # Fetch data
    data = fetch_data(ville, commune)

    # If no data found
    if not data:
        ctk.CTkMessagebox(title="Aucune donnée", message="Aucune donnée trouvée pour cette ville et commune.", icon="info")
        return

    # Create a new window to display the data
    result_window = ctk.CTkToplevel(root)
    result_window.title("Résultats de la recherche")
    result_window.geometry("1000x400")

    # Create a Treeview table
    columns = ("Nom", "Prénom", "Date de naissance", "Email", "Téléphone", "NIN", "Ville", "Commune", "Type")
    tree = ttk.Treeview(result_window, columns=columns, show="headings", height=10)

    # Add column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    tree.pack(fill="both", expand=True)

    # Insert data into the Treeview
    for row in data:
        tree.insert("", "end", values=(row["Nom"], row["Prénom"], row["Date de naissance"], row["Email"],
                                       row["Téléphone"], row["NIN"], row["Ville"], row["Commune"], row["Type"]))
#dark or light mood
ctk.set_appearance_mode("system")


# Create the main application window
root = ctk.CTk()
root.title("Recherche de location")
root.geometry("700x700")


# Input interface
bold_font = ctk.CTkFont(family="Courier New", size=18, weight="bold")
label_ville = ctk.CTkLabel(root, text="Ville :", text_color="#808080", anchor='w', font=bold_font).pack(pady=10)
entry_ville = ctk.CTkEntry(root, height=40,width=260, bg_color="white"  , border_width=0 , font=("Courier New" , 16))
entry_ville.pack(pady=5)

label_commune=ctk.CTkLabel(root, text="Commune :", text_color="#808080", anchor='w', font=bold_font).pack(pady=10)
entry_commune = ctk.CTkEntry(root,  height=40, width=260,  bg_color="white", border_width=0 , font=("Courier New" , 16))
entry_commune.pack(pady=5)

# Search button
search_btn = ctk.CTkButton(root, text="Afficher les données", command=show_data , bg_color="#5D3FD3"  , height=40,width=200)
search_btn.pack(pady=20)

# Run the application
root.mainloop()
