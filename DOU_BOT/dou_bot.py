from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from DOU_BOT.constants import BASE_URL
from DOU_BOT.dou_vacancies_report import DouReport
from prettytable import PrettyTable


class DOU:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def land_first_page(self):
        self.driver.get(BASE_URL)

    def choose_category(self):
        select = Select(self.driver.find_element(By.NAME, "category"))
        select.select_by_value("QA")

    def choose_vacancy(self):
        input_vacancy = self.driver.find_element(By.CLASS_NAME, "job")
        input_vacancy.send_keys("python")

    def click_find_button(self):
        find_button = self.driver.find_element(By.CLASS_NAME, "btn-search")
        find_button.click()

    def vacancies_report(self):
        vacancies = self.driver.find_element(By.ID, "vacancyListId")
        vacancies_report = DouReport(vacancies)
        table = PrettyTable(
            field_names=["Vacancy", "Date", "Vacancy Info"]
        )
        table.add_rows(vacancies_report.pull_vacancy_attributes())
        print(table)

    def close_browser(self):
        self.driver.quit()
