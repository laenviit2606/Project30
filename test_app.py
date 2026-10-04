import unittest
from app import app


class TestWebsite(unittest.TestCase):
    def setUp(self): #Runs before every test to prepare the test environment
        app.config["TESTING"] = True #Enable testing mode
        self.client = app.test_client() #Creates a simulated browser that sends requests directly to Flask

    def test_home_page(self):
        response = self.client.get("/") #Requests the Insights page 

        self.assertEqual(response.status_code, 200)
        self.assertIn("Language Explorer", response.get_data(as_text=True))

    def test_insights_page(self): 
        response = self.client.get("/insights")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Alternative-name coverage", response.get_data(as_text=True))

    def test_about_page(self):
        response = self.client.get("/about")

        self.assertEqual(response.status_code, 200)
        self.assertIn("AIATSIS", response.get_data(as_text=True))

    def test_search_result(self):
        response = self.client.get("/", query_string={"q": "Y75"}) #Simulates submitting the search from with Y75

        self.assertEqual(response.status_code, 200) #Reads the reponse statu; 200 means a successful response
        self.assertIn("Y75", response.get_data(as_text=True))
        self.assertIn("Language name:", response.get_data(as_text=True)) #Reads the returned HTML as text 

    def test_unknown_search(self):
        response = self.client.get("/", query_string={"q": "UNKNOWN999"})

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "No matching language found",
            response.get_data(as_text=True)
        )

    def test_blank_search(self):
        response = self.client.get("/", query_string={"q": "   "})

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Please enter a language code or name",
            response.get_data(as_text=True)
        )

#assertIn(...): Checks that expected text appears in that HTML
if __name__ == "__main__":
    unittest.main()