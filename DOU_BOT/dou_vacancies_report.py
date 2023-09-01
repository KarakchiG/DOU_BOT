from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DouReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CLASS_NAME, "l-vacancy")

    def pull_vacancy_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            vacancy_titles = deal_box.find_element(
                By.CLASS_NAME, "title"
            ).text
            # print(vacancy_titles)

            vacancy_date = deal_box.find_element(
                By.CLASS_NAME, "date"
            ).get_attribute('innerHTML').strip()
            # print(vacancy_date)

            vacancy_info = deal_box.find_element(
                By.CLASS_NAME, "sh-info"
            ).text
            # print(vacancy_info)

            collection.append(
                [vacancy_titles, vacancy_date, vacancy_info]
            )
        return collection
