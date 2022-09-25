class Menu:
    def __init__(self, prop : dict):
        """
        :param prop:
        :returns: Return : string's menu when it has a symbol for action/command and title.
        """
        self.recipes = prop

    def allResipes(self):
        self.all_recipes = list(dict(self.recipes).keys())
        # self.count = list(self.all_recipes).count()
        el = None
        str_var = '{}'
        menu_var = f"""
'a' - all recipes;
"""
        for recipe in self.all_recipes:
            rec = (str(recipe)[:3]).lower()
            menu_var += ("\n" + f"'{rec}' - {recipe};" )
        menu_var = menu_var[ : -1] + "."
        return menu_var