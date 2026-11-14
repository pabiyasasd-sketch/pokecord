import aiohttp  # A library for asynchronous HTTP requests
import random

class Pokemon:
    pokemons = {}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.img = None
        self.hp = random.randint(100, 200)
        self.power = random.randint(100, 200)
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['forms'][0]['name']  # Returning a Pokémon's name
                else:
                    return "Pikachu"  # Return the default name if the request fails

    async def info(self):
        # A method that returns information about the pokémon
        if not self.name:
            self.name = await self.get_name()  # Retrieving a name if it has not yet been uploaded
        return f"Your Pokémon: {self.name}, HP: {self.hp}, Power: {self.power}"  # Returning the string with the Pokémon's name and stats

    async def show_img(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    print(data)
                    return data["sprites"]["front_default"]  # Returning a Pokémon's image URL
                else:
                    return "none"  # Return none if the request fails
                
    async def show_ability(self):
        # An asynchronous method to retrieve the ability of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data["abilities"][0]["ability"]["name"]  # Returning a Pokémon's ability
                else:
                    return "none"  # Return none if the request fails
                
    async def attack(self, enemy):
        if isinstance(enemy, Wizard):  # Periksa apakah musuh adalah tipe data Penyihir (instance dari kelas Penyihir)
            kesempatan = random.randint(1,5)
            if kesempatan == 1:
                return "Pokemon Wizard used shield in the fight."
    
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"@{enemy.pokemon_trainer} have a fight with @{self.pokemon_trainer}!"
        else:
            enemy.hp = 0
            return f"@{self.pokemon_trainer} Won against @{enemy.pokemon_trainer}!"

class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    async def attack(self, enemy):
        superpower = random.randint(5, 15)
        self.kekuatan += superpower
        result = await super().attack(enemy)
        self.kekuatan -= superpower
        return result + f"\nFighter used a super attack with power: {superpower}"