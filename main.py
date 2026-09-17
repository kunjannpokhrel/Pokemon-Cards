from PIL import Image
import requests
def pokemon():
    name=input("The Pokemon You Want To Find About: ").lower()
    main_url= "https://pokeapi.co/api/v2"
    url= f"{main_url}/pokemon/{name}"
    request=requests.get(url)
    if request.status_code==200:
        print("DATA RETRIVED FROM API")
    else:
        print("COULD NOT RETRIVE DATA")
    data=request.json()
    print(f"Name = {data["name"].capitalize()}")
    print(f"Id = {data["id"]}")
    print(f"Height = {data["height"]}")
    print(f"Weight = {data["weight"]}")
    print(f"Type = {data['types'][0]['type']['name'].capitalize()}")
    print(f"Ability = {data['abilities'][0]['ability']['name'].capitalize()}")
    print(f"HP = {data['stats'][0]['base_stat']}")
    print(f"Attack = {data['stats'][1]['base_stat']}")
    print(f"Defense = {data['stats'][2]['base_stat']}")
    print(f"Special Attack = {data['stats'][3]['base_stat']}")
    print(f"Special Defense = {data['stats'][4]['base_stat']}")
    print(f"Speed = {data['stats'][5]['base_stat']}")
    artwork_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    response = requests.get(artwork_url)
    with open("pokemon.png", "wb") as file:
     file.write(response.content)
    image=Image.open("pokemon.png")
    print(image.size)
    print(image.mode)
    resized_image=image.resize((300,300))
pokemon()
