# https://openweathermap.org/
 # https://api.openweathermap.org/data/2.5/weather?q=Воронеж&appid=3fe790c4c3f692ca9f0151dfa8b0f4df&units=metric
import requests
from translatepy.translators.google import GoogleTranslate  

import tkinter

google_transate = GoogleTranslate()

root = tkinter.Tk()
root.geometry('500x500')

tempVar = tkinter.StringVar()
humidityVar = tkinter.StringVar()
weatherVar = tkinter.StringVar()
countryVar = tkinter.StringVar()




def get_weather(city , api_key):
 #print(f"Ващ город: {city} и ключ API: {api_key}")
  url = 'https://api.openweathermap.org/data/2.5/weather?'
  complete_url = f"{url}q={city}&appid={api_key}&units=metric"
  print(complete_url)

  r = requests.get(complete_url)
  print(r)

  data = r.json()
 # print(data)

  temp = data['main']['temp']
  humidity = data['main']['humidity']
  
  tempVar.set(f'Температура: {temp}℃😀')
  humidityVar.set(f'влажость: {humidity}%😱😨')

  weather = data['weather'][0]['main']
  translate_weather = google_transate.translate(weather,'ru')
  weatherVar.set(f'погода: {translate_weather}🍔')
  
  country = data['sys']['country']
  countryVar.set(f'страна: {country}🍉')

  return tempVar, humidityVar, weatherVar, countryVar

 

def main():
  print("Здравствуйте в приложение погода!")
  city = city_entry.get()
  api_key = "3fe790c4c3f692ca9f0151dfa8b0f4df"
  
  get_weather(city, api_key)

# main()

label = tkinter.Label(root,cursor='dot',text='Введите город о котором хотите узнать информацию.',fg='white',bg='green',padx='500')
label.pack()

city_entry = tkinter.Entry(root,fg='green',cursor='boat')
city_entry.pack()

button = tkinter.Button(root,fg='black',cursor='boat',text='Искать',command=main)
button.pack()

temp_label = tkinter.Label(root,cursor='boat',textvariable=tempVar, fg='white',bg='black',padx='500')
temp_label.pack()



humidity_label = tkinter.Label(root,cursor='boat',textvariable=humidityVar, fg='white',bg='black',padx='500')
humidity_label.pack()

weather_label = tkinter.Label(root,cursor='boat',textvariable=weatherVar, fg='white',bg='black',padx='500')
weather_label.pack()


country_label = tkinter.Label(root,cursor='boat',textvariable=countryVar, fg='white',bg='black',padx='500')
country_label.pack()



root.mainloop()