from bs4 import BeautifulSoup

class BeautifulSoupElement:
    def __init__(self):
        return
    
    def get_beautiful_html(self, driver):
        soup = BeautifulSoup(driver, "html.parser")
        return soup
    
    def get_elements_by_name_soup(self, html, target_name):
        soup = BeautifulSoup(html, "html.parser")
        return soup.find_all(name=target_name)

    def get_element_by_name_soup(self, html, target_name, index = 0):
        elements = self.get_elements_by_name_soup(html, target_name)
        if len(elements) > 0:
            return elements[index].prettify()
        else:
            return None
