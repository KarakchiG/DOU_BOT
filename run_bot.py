from DOU_BOT.dou_bot import DOU

bot = DOU()
bot.land_first_page()
bot.choose_category()
bot.choose_vacancy()
bot.click_find_button()
bot.vacancies_report()

input("Press enter to close the browser")
bot.close_browser()
