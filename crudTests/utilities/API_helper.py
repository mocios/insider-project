import requests


def get_pet(pet_id):
    endpoint = f"/pet/{pet_id}"
    response = requests.get(url=endpoint)
    return response.json()


def add_pet(body):
    endpoint = "/pet"
    response = requests.post(url=endpoint, data=body)
    return response.json()


def update_pet(body):
    endpoint = "/pet"
    response = requests.put(url=endpoint, data=body)
    return response.json()


def delete_pet(pet_id):
    endpoint = f"/pet/{pet_id}"
    response = requests.delete(url=endpoint)
    return response.json()

