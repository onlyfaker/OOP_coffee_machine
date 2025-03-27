from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

CoffeeMaker().report()
coffes = Menu().get_items()

is_on = True
while is_on:
    coffees = menu.get_items()
    user_choice = input(f"chose your coffe {coffees} or 'report': ")

    if user_choice=='off':
        is_on = False
    elif user_choice=='report':
        coffee_maker.report()
        money_machine.report()
    # else:
    #     order = Menu().find_drink(user_choice)
    #     if order!=None:
    #         if ==True:
    #
