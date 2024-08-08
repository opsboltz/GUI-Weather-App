from tkinter import *
import customtkinter
import requests

API_Key = "87cb20bee0648fcb5fa65fca154cebb2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Weather app')
root.geometry('900x500')


def Weather():
    city = Weather_entry.get()
    request_url = f"{BASE_URL}?q={city}&appid={API_Key}&units=imperial"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        # get the weather key
        weather = data['weather'][0]['description']
        # Access the main and temp key
        temperature = round(data["main"]["temp"])

        Weather_text.delete("1.0", END)  # Clear the textbox
        Weather_text.insert("1.0", f"Weather: {weather}\nTemperature: {temperature}°F")
    else:
        Weather_text.delete("1.0", END)  # Clear the textbox
        Weather_text.insert("1.0", "An error occurred. Please try again.")


# Create a CTkLabel
Weather_Label = customtkinter.CTkLabel(root, text="Welcome, Guessing you're here to get your Weather.",
                                       font=("Helvetica", 24))
Weather_Label.pack(pady=40)

# Create a CTkEntry
Weather_entry = customtkinter.CTkEntry(root, placeholder_text="EX: Chicago, IL, US", width=200)
Weather_entry.pack()

# Create a button to get weather
Weather_Button = customtkinter.CTkButton(root, text="Get Weather!", width=200, command=Weather)
Weather_Button.pack(pady=20)

# Create a CTkTextbox without the 'text' argument
Weather_text = customtkinter.CTkTextbox(root, height=500, width=900)
Weather_text.pack(pady=50)

root.mainloop()
