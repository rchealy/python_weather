import requests

apiikey = open("api_key.txt", "r").read()
apkey = "2f580c75df8f7443cc1eb3e6ce938c35"
apikey = apiikey.strip()

while True:
    location = input("Location: ")

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={apikey}')
    if result.json()['cod'] == '404':
        print("Invalid location!")
        continue
    break

description = result.json()['weather'][0]['description']
temperature = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
high = round(result.json()['main']['temp_max'])
low = round(result.json()['main']['temp_min'])

print(f"The weather in {location[0].upper()}{location[1:]} is {temperature}° C  with {description}.")
print(f"It feels like {feels_like}° C.")
print(f"Today's high id {high}° C and today's low is {low}° C.")


#res2 = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={apkey}')
#print(res2)
#res3 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={apkey}')
#print(res3.json())

print(apikey)
print(apkey)
#print(result.json())
