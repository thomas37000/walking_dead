from django.test import TestCase

from characters.models import Character, CharactersList

class CharacterTestCase(TestCase): # python3 manage.py test
    
    TEST_NAME_CHARACTER = 'Bartholome'
    TEST_LASTNAME_CHARACTER = 'Simpcon'
    
    def setUp(self): # initialisation de la CharactersList avant de lancer les tests
        self.charactersList = CharactersList()
        self.charactersList.name = 'characters List'
        self.charactersList.save()
        
        self.testNewCharacterList = Character()
        self.testNewCharacterList.name = self.TEST_NAME_CHARACTER
        self.testNewCharacterList.lastname = self.TEST_LASTNAME_CHARACTER
        self.testNewCharacterList.is_alive = False
        self.testNewCharacterList.charactersList = self.charactersList
        
        self.testNewCharacterList.save()
        
    def test_create_character(self): 
        
        # GET
        nbr_of_characters_before_add = Character.objects.count()
        
        # POST
        new_character = Character()
        new_character.name = 'Homer'
        new_character.lastname = 'Simpson'
        new_character.is_alive = True
        new_character.charactersList = self.charactersList
        
        new_character.save()
        
        nbr_of_characters_after_add = Character.objects.count()
        
        self.assertTrue(nbr_of_characters_after_add == nbr_of_characters_before_add + 1)

    def test_update_character(self):
        
        self.assertEqual(self.testNewCharacterList.name, self.TEST_NAME_CHARACTER)
        self.assertEqual(self.testNewCharacterList.lastname, self.TEST_LASTNAME_CHARACTER)
        self.testNewCharacterList.name = 'Bart'
        self.testNewCharacterList.name = 'Simpson'
        self.testNewCharacterList.is_alive = True
        
        self.testNewCharacterList.save()
        
    def test_delete_character(self):

        nbr_of_characters_before_delete = Character.objects.count()
        
        self.testNewCharacterList.delete()
        
        nbr_of_characters_after_delete = Character.objects.count()
        
        self.assertTrue(nbr_of_characters_after_delete == nbr_of_characters_before_delete - 1)