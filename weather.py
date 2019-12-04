import tkinter as tk

import requests

HEIGHT = 600
WIDTH = 800


    # 6ca265e51eb926695c879cfe8ceb4e6b
    # api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
    # 819ce39420ed3e
    # "https://us1.locationiq.com/v1/search.php"
    # /Users/sherif/Desktop/sky-background.png


def format_response(weather):
    name = (weather['name'])
    con = (weather['weather'][0]['description'])
    temp = (weather['main']['temp'])
    temp1 = (weather['main']['temp_min'])
    temp2 = (weather['main']['temp_max'])
    wind = (weather['wind']['speed'])
    hum = (weather['main']['humidity'])


    return 'City: %s \nCondition: %s \nTemperature (C): %s \nWind Speed: %s \nMinimum Temperature: %s ' \
           '\nMaximum Temperature: %s \nHumidity: %s' % (name, con, temp, wind, temp1, temp2, hum)


def find_weather(city):
    weather_key = '6ca265e51eb926695c879cfe8ceb4e6b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()


background_image=tk.PhotoImage('/Users/sherif/Desktop/sky-background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#00BFFF', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=50)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Find Weather", bg='black', font=50, command=lambda: find_weather(entry.get()))
button.place(relx=0.7, rely=0., relwidth=0.3, relheight=1)

bottom_frame = tk.Frame(root, bg='#00BFFF', bd=75)
bottom_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(bottom_frame, font=50)
label.place(relwidth=1, relheight=1)

root.mainloop()
