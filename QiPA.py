import os
import shutil
import tkinter as tk
from tkinter import filedialog
import tempfile

def selectApp():
    root = tk.Tk()
    root.withdraw()  
    app = filedialog.askdirectory(title="Select the .app directory")

    if not app:
        print("You haven't selected the app, please select the .app folder location.")
        quit()

    print(f"Selected .app directory: {app}")
    return app

def makeIPA(app):
    app_parent_dir = os.path.dirname(app)  # Ottiene la directory in cui si trova la .app
    temp_dir = tempfile.mkdtemp()  # Crea una directory temporanea
    payload_path = os.path.join(temp_dir, "Payload")
    os.mkdir(payload_path)  # Crea la cartella Payload

    # Sposta l'app in Payload
    app_name = os.path.basename(app)  # Ottiene solo il nome della cartella .app
    shutil.copytree(app, os.path.join(payload_path, app_name))

    # Chiede il nome dell'IPA
    ipa_name = input("Type your IPA name (leave empty to use the same app name): ").strip()
    if not ipa_name:
        ipa_name = app_name.replace(".app", "")  # Usa il nome dell'app senza .app

    # Percorso dell'IPA nella stessa cartella della .app
    final_ipa_path = os.path.join(app_parent_dir, ipa_name + ".ipa")

    # Crea il file ZIP e lo rinomina in .ipa
    shutil.make_archive(os.path.join(temp_dir, ipa_name), 'zip', temp_dir, "Payload")
    os.rename(os.path.join(temp_dir, ipa_name + ".zip"), final_ipa_path)

    # Elimina la directory temporanea
    shutil.rmtree(temp_dir)

    print(f"File IPA saved at: {final_ipa_path}")

print("This is a tool to create an IPA directly from a .app")
choice = input("Press ENTER to continue or type Q to quit: ")

if choice.lower() == "q":
    quit()

app_path = selectApp()
makeIPA(app_path)
