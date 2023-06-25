import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
    trainer_info = requests.get(f"{host}/trainers")
    assert trainer_info.status_code == 200    
        
def test_my_id():
    answer_body = requests.get(f"{host}/trainers", params = {"trainer_id" : 4632})
    assert answer_body.json()['trainer_name'] == 'SergAS'