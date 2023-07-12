from selene import be, have
from selene.support.shared import browser


def test_empty_search(browser_size):
    browser.open('https://google.ru')
    browser.element('[name="q"]').should(be.blank).type('234234234лимиьмсдиьмдлиьма').press_enter()
    browser.element('[class="card-section"]').should(have.text('Не найдено ни одного документа по запросу.'))
    print('В выдаче браузера нет результатов поиска')

