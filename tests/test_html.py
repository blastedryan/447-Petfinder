from tests.webtests import WebTests

class WebBones(WebTests):
    def test_web_bones(self):
        self.driver.get(self.htmlPath)
        self.driver.find_element_by_tag_name("input")
        self.driver.find_element_by_tag_name("label")
        self.driver.find_element_by_tag_name("button")

    