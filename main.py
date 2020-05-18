import tkinter as tk
from tkinter import font
import requests



# panjang dan tinggi canvas
tinggi = 500
panjang = 1000


def test_function(entry):
    print("this is the entry:", entry)

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem \nretrieving that information\nplease type the right city name'

	return final_str

def get_weather(city):
	weather_key = 'f84de89d348ab206134827047dffb193'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

#f84de89d348ab206134827047dffb193
#api.openweathermap.org/data/2.5/forecast/daily?q={city name}&cnt={cnt}&appid={your api key}

root = tk.Tk()
root.title("Aplikasi Perkiraan Cuaca")
root.iconbitmap('icon.ico')

canvas = tk.Canvas(root, height=tinggi, width=panjang)
canvas.pack()

background_image = tk.PhotoImage(file='bg3.png')
background_label = tk.Label(root, image=background_image)
background_label.place( relwidth=1, relheight=1)

frame = tk.Frame(root, bg='grey',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(frame,text="Enter City Name ", font=('arial',15,'bold'), bg='grey', fg='white')
label.place(relwidth=0.35,relheight=1)

entry = tk.Entry(frame, justify="center", bg='#d4d6d6',relief='flat', font=('arial',15,'bold'))
entry.place(relx=0.37,relwidth=0.4, relheight=1)

tombol_cari = tk.Button(frame, text="Get Weather", bg='#ffffff',font=('arial',15,'bold'),relief='flat', command=lambda: get_weather(entry.get()) )
tombol_cari.place(relx=0.8, relheight=1,relwidth=0.2)

lower_frame = tk.Frame(root, bg='grey', bd=5,relief='flat')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('arial', 22), justify="left",relief='flat')
label.place(relwidth=1, relheight=1)



root.mainloop()