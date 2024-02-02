# https://openweathermap.org/
 # https://api.openweathermap.org/data/2.5/weather?q=Воронеж&appid=3fe790c4c3f692ca9f0151dfa8b0f4df&units=metric
import requests
from translatepy.translators.google import GoogleTranslate  


google_transate = GoogleTranslate()





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
  
  print(f'Температура: {temp}℃🎈')
  print(f'влажость: {humidity}%😱😨')
  
  weather = data['weather'][0]['main']
  translate_weather = google_transate.translate(weather,'ru')
  print(f'погода: {translate_weather}🍔')
  country = data['sys']['country']
  print(f'страна: {country}🍉')




def main():
  print("Здравствуйте в приложение погода!")
  city = input("Введите название города: ")
  api_key = "3fe790c4c3f692ca9f0151dfa8b0f4df"
  
  get_weather(city, api_key)

main()









