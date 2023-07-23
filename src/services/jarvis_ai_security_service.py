from models.avenger import Avenger

class JarvisAiSecurityService:
    def __init__(self) -> None:
        pass


    def security_pass_phrase_auth(self, avenger: Avenger, password_phrase: str):
        pass_phrases = self.get_pass_phrases()

        if avenger.super_hero_name in pass_phrases:
            phrase = pass_phrases[avenger.super_hero_name]
            if phrase == password_phrase:
                return True
            
        return False


    def get_pass_phrases(self):
        phrases = {
            "Iron Man": "I am Iron Man",
            "Hulk": "Strongest Avenger",
            "Thor": "Point Break"
            
        }

        return phrases

