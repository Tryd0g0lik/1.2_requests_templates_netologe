import json

# from recipes.recipe_basis.module.basis_recipe import Basis
from recipe_basis.module.basis_recipe import Basis



class Menu:
    """
      def 'allResipes' - return a tuple type. The first element it's menu when type is str. Second element it's
      list type, a commands.

      def menu -  tuple, it gets of '__allResipes' function

      :param prop:
      :returns: string's menu when it has a symbol for action/command and title.
    """
    def __init__(self):
      self.commands_var = []
      self.all_recipes = []
      self.menu_var  = None

    def __allResipes(self, recipes) -> tuple:
        """
        Function gets file (it's json) contents.
        :param 'Basis': import  an iterator the iterator gets json file data and  returns a dictionary string
        :param recipes: The data of json file.
        :return: return a tuple type. The first element it's menu when type is str. Second element it's
      list type, a commands
        """
        self.all_recipes = list(dict(recipes).keys())
        menu_var = f"""
'a' - all recipes;
"""
        for recipe in self.all_recipes:
            rec = (str(recipe)[:3]).lower()
            menu_var += ("\n" 
                         f"'{rec}' - {recipe};" )
            self.commands_var.append(rec)

        self.menu_var = menu_var[ : -1] + "."
        return (self.menu_var, self.commands_var)


    def menu(self, fileName : str) -> str:
      """
			Returns command's  a symbol for run a menu and the list comand
      :param fileName: The file name there has recipes list
      :return: tuple, it gets of '__allResipes' function
      """

      with open(f"recipes/recipe_basis/files/data.json", encoding='utf-8', mode="r") as jsFile:

        self.json_data = Basis(json.load(jsFile))


      self.menu = Menu.__allResipes(self, self.json_data )
      return self.menu
