import unittest
from models.avenger import Avenger
from services.jarvis_ai_security_service import JarvisAiSecurityService

class JarvisAiServiceTests(unittest.TestCase):
    def test_security_pass_phrase_auth(self):
        avenger: Avenger = Avenger()    
        avenger.super_hero_name = "Iron Man"
        
        service: JarvisAiSecurityService = JarvisAiSecurityService()
        result = service.security_pass_phrase_auth(avenger, "I am Iron Man")

        self.assertTrue(result)

    def test_security_pass_phrase_auth_thor_strongest_avenger(self):
        avenger: Avenger = Avenger()    
        avenger.super_hero_name = "Thor"
        
        service: JarvisAiSecurityService = JarvisAiSecurityService()
        result = service.security_pass_phrase_auth(avenger, "Strongest Avenger")

        self.assertFalse(result)

    
    def test_security_pass_phrase_auth_thor_point_break(self):
        avenger: Avenger = Avenger()    
        avenger.super_hero_name = "Thor"
        
        service: JarvisAiSecurityService = JarvisAiSecurityService()
        result = service.security_pass_phrase_auth(avenger, "Point Break")

        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()