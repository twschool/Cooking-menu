"""Last version of delete meal changed so it returns a tuple instead
of returning a list also there is no main routine in the script because
I wanted to use it for testing in edit_meals_v2"""

def delete_menu(menu_, combo_input_):
    try:
        del menu_[combo_input_.title()]
        return True, menu_
    except KeyError:
        return False, menu_
