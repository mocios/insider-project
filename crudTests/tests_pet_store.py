import copy

import crudTests.utilities.API_helper as api_helper
from crudTests.utilities.test_pet import pet


class PetStoreTests:

    def test_add_new_pet(self):
        new_pet = copy.deepcopy(pet)
        response = api_helper.add_pet(new_pet)
        assert response.status_code == 201

    def test_add_new_pet_incorrect_data(self):
        new_pet = {}
        response = api_helper.add_pet(new_pet)
        assert response.status_code == 405

    def test_get_pet(self):
        new_pet = copy.deepcopy(pet)
        api_helper.add_pet(new_pet)
        response = api_helper.get_pet(new_pet["id"])
        assert response.status_code == 200

    def test_get_non_existing_pet(self):
        response = api_helper.get_pet(123)
        assert response.status_code == 404

    def test_get_pet_invalid_id(self):
        response = api_helper.get_pet("test_pet")
        assert response.status_code == 400

    def test_update_pet(self):
        new_pet = copy.deepcopy(pet)
        api_helper.add_pet(new_pet)
        new_pet["name"] = "GoodBoy"
        response = api_helper.update_pet(new_pet)
        assert response.status_code == 204

    def test_update_pet_invalid_id(self):
        new_pet = copy.deepcopy(pet)
        api_helper.add_pet(new_pet)
        new_pet["id"] = "GoodBoy"
        response = api_helper.update_pet(new_pet)
        assert response.status_code == 400

    def test_update_non_existing_pet(self):
        new_pet = copy.deepcopy(pet)
        response = api_helper.update_pet(new_pet)
        assert response.status_code == 404

    def test_delete_pet(self):
        new_pet = copy.deepcopy(pet)
        api_helper.add_pet(new_pet)
        response = api_helper.delete_pet(new_pet["id"])
        assert response.status_code == 204

    def test_delete_non_existing_pet(self):
        new_pet = copy.deepcopy(pet)
        response = api_helper.delete_pet(new_pet["id"])
        assert response.status_code == 404

    def test_delete_pet_invalid_id(self):
        new_pet = copy.deepcopy(pet)
        api_helper.add_pet(new_pet)
        new_pet["id"] = "GoodBoy"
        response = api_helper.delete_pet(new_pet["id"])
        assert response.status_code == 400
