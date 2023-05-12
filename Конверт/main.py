import requests
from bs4 import BeautifulSoup
import time


DOLLAR_RUB = 'https://www.google.ru/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=APwXEdfdP23ZCKtwZbK6sTAhtiVNJBwjYg%3A1683731102325&source=hp&ei=nrJbZKvWEOKExc8PnPyJmAU&iflsig=AOEireoAAAAAZFvAruAsZnK7AVoUiX6TmkR3FzyoPVVm&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAguEIAEELEDMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCKBRCxAxCDATIICAAQgAQQsQM6DQguEIoFEMcBEK8BECc6BwgjEIoFECc6EAguEIAEEBQQhwIQxwEQrwE6CwguEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoECCMQJzoLCC4QgAQQxwEQrwE6BQgAEIAEOhYILhCABBAUEIcCELEDEIMBEMcBENEDOgsILhCABBCxAxDUAlAAWNsGYIwVaABwAHgAgAFYiAHwApIBATWYAQCgAQE&sclient=gws-wiz'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

def check_currency():
    full_page = requests.get(DOLLAR_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlide","class": "SwHCTb","data-precision":2})
    print("Сейчас курс: 1 доллар = " + convert[0].text)
    time.sleep(3)
    check_currency()

check_currency()