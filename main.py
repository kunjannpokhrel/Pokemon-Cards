from PIL import Image , ImageDraw ,ImageFont
import requests
import random

def get_pokemon(name):
    main_url = "https://pokeapi.co/api/v2"
    url = f"{main_url}/pokemon/{name}"
    request = requests.get(url)
    if request.status_code == 200:
     print("DATA RETRIVED FROM API")
     data = request.json()
     return data
    else:
     print("POKEMON NOT FOUND")
     return None

def get_artwork(data):
    artwork_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    response = requests.get(artwork_url)
    with open("pokemon.png", "wb") as file:
     file.write(response.content)
    image=Image.open("pokemon.png")
    return image

def create_card(data,image):
    hp = data["stats"][0]["base_stat"]
    attack = data["stats"][1]["base_stat"]
    defense = data["stats"][2]["base_stat"]
    special_attack = data["stats"][3]["base_stat"]
    special_defense = data["stats"][4]["base_stat"]
    speed = data["stats"][5]["base_stat"]
    pokemon_type = data["types"][0]["type"]["name"]

    # RETRIVED from POKEAPI
    type_colors = {
        "electric": "yellow",    "fire": "red",           "water": "skyblue",
        "grass": "lightgreen",   "psychic": "pink",        "ghost": "purple",
        "ice": "lightcyan",      "dark": "gray",           "dragon": "orange",
        "normal": "lightgray",   "fighting": "orange",     "poison": "violet",
        "ground": "tan",         "rock": "saddlebrown",    "bug": "lightgreen",
        "flying": "lightblue",   "steel": "lightsteelblue","fairy": "lightpink"}

    background_color = type_colors[pokemon_type]
    card = Image.new("RGB", (600, 800), background_color)
    draw=ImageDraw.Draw(card)
    draw.rectangle((10,10,590,790), outline="black", width=5)
    draw.rectangle((50,100,550,393.75), outline="black", width=3)
    resized_image=image.resize((300,300))
    card.paste(resized_image,(150,100),resized_image)
    font= ImageFont.truetype("arial.ttf",32)
    draw.text((60,50),data["name"].capitalize(),font=font ,fill="black")
    draw.text((70, 500), f"HP: {hp}", font=font, fill="black")
    draw.text((70, 540), f"Attack: {attack}", font=font, fill="black")
    draw.text((70, 580), f"Defense: {defense}", font=font, fill="black")
    draw.text((330, 500), f"Sp. Attack: {special_attack}", font=font, fill="black")
    draw.text((330, 540), f"Sp. Defense: {special_defense}", font=font, fill="black")
    draw.text((330, 580), f"Speed: {speed}", font=font, fill="black")
    return card

def pokemon():
    while True:
     name = input("The Pokemon You Want To Find About [TRY: random]: ").lower()
     if name == "random":
      name = str(random.randint(1, 1025))
     data = get_pokemon(name)
     if data is not None:
      break
    image = get_artwork(data)
    card = create_card(data,image)
    card.show()

pokemon()