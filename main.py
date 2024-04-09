import requests
import customtkinter
from PIL import Image
import os

'''
città = str(input("Inserire nome città:\n"))
linkMeteo = f"https://api.openweathermap.org/data/2.5/weather?q={città}&appid=ab6d1f611ca3cbdd08906449d48ea636&units=metric"
risposta = requests.get(linkMeteo).json()
temperatura = risposta['main']['temp']
umidità = risposta['main']['humidity']
print(linkMeteo)

print(f"La temperatura a {città} è di {temperatura}°C e l'umidità è del {umidità}%")
'''

def prendiMeteo():
    global img
    città = cittaBox.get("0.0", "end").lower()
    linkMeteo = f"https://api.openweathermap.org/data/2.5/weather?q={città}&appid=ab6d1f611ca3cbdd08906449d48ea636&units=metric"
    try:
        risposta = requests.get(linkMeteo).json()
        temperatura = risposta['main']['temp']
        umidita = risposta['main']['humidity']
        tempo = risposta["weather"][0]["description"]
        if "rain" in tempo:
            img = customtkinter.CTkImage(Image.open(os.getcwd() +"/imgs/pioggia.png"), size=(150, 150))
        elif "clouds" in tempo:
            img = customtkinter.CTkImage(Image.open(os.getcwd() +"/imgs/nuvoloso.png"), size=(150, 150))
        elif "clear" in tempo:
            img = customtkinter.CTkImage(Image.open(os.getcwd() +"/imgs/soleggiato.png"), size=(150, 150))
        imgL.configure(image=img)
        meteoL.configure(text=f"{temperatura}°C\n{umidita}%")
    except:
        meteoL.configure(text="Errore")

root = customtkinter.CTk()
root.geometry("400x600")
root.title("Meteo")

titolo = customtkinter.CTkLabel(text="Meteo di ", master=root, font=("verdana", 40))
titolo.pack(pady=10)

cittaBox = customtkinter.CTkTextbox(master=root, height=50)
cittaBox.pack(pady=10)

btn = customtkinter.CTkButton(master=root, text="Meteo", command=prendiMeteo)
btn.pack(pady=10)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10)

meteoL = customtkinter.CTkLabel(master=frame, text="")
meteoL.pack(pady=10)

imgL = customtkinter.CTkLabel(master=frame, text="")
imgL.pack(pady=10, padx=20)

root.mainloop()