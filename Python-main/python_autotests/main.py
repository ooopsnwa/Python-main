import requests

token = '2434a1a20f1789cbdd19058cc0381d80' 
host = 'https://pokemonbattle.me:9104'

# answer_reg = requests.post('https://pokemonbattle.me:9104/trainers/reg', json =  # Регистрация тренера
#                        {
#     "trainer_token": token,
#     "email": "pismoss@yandex.ru",
#     "password": "123456S"
# }, headers = {"Content-Type": "application/json"})

# answer_confirm = requests.post(f"{host}/trainers/confirm_email", json = # Подтверждение почты
#                                {
#     "trainer_token": token,
#     }, headers = {"Content-Type": "application/json"})

# ans_change_avatar = requests.post(f"{host}/trainers/change_avatar", json = # Смена аватара
#                                {
#     "card_number": "4276550045710954",
#     "card_csv": "125",
#     "card_actual": "10/24",
# 	"num": "56456", # это пароль от смс,
# 	"avatar_id": "8"
# }, headers = {"Content-Type" : "application/json", "trainer_token" : token})
# print (ans_change_avatar.text)



ans_poke_create = requests.post(f"{host}/pokemons", json = # Создание покемона
                            {
    "name": "Firstpoo",
    "photo": "https://dolnikov.ru/pokemons/albums/075.png"
}, headers =  {"Content-Type": "application/json", "trainer_token" : token})

print (ans_poke_create.text)

ans_poke_rename = requests.put(f"{host}/pokemons", json = # Переименование покемона
                            {
    "pokemon_id": "13150",
    "name": "Secondpoo",
    "photo": "https://dolnikov.ru/pokemons/albums/075.png"
}, headers =  {"Content-Type": "application/json", "trainer_token" : token})

print (ans_poke_rename.text)

ans_poke_inball = requests.post(f"{host}/trainers/add_pokeball", json = # Покемон в покебол
                            {
    "pokemon_id": "13150"
}, headers =  {"Content-Type": "application/json", "trainer_token" : token})

print (ans_poke_inball.text)



# ans_poke_kill = requests.post(f"{host}/pokemons/kill", json = # Убийство покемона
#                             {
#     "pokemon_id": "13151"
# }, headers =  {"Content-Type": "application/json", "trainer_token" : token})

# print (ans_poke_kill.text)
