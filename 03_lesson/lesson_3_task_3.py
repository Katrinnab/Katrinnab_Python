from address import Address
from mailing import Mailing

addr1 = Address('234567', 'Москва', 'Красная', '23', '5')
addr2 = Address('198412', 'Санкт-Петербург', 'Отрадная', '15', '87')
mail = Mailing(addr1, addr2, '350', '974538396456')

print(mail)
