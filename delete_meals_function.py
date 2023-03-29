"""Code borrowed from delete meals v1 to be used
for testing purposes in edit meals v2 (not a actual component)"""

def delete_menu(menu_, combo_input_):
    try:
        del menu_[combo_input_.title()]
        return True, menu_
    except KeyError:
        return False, menu_
