import json
class Basis:
    def __init__(self, prop):
        """
        Class is iterator/
        To works with large data file json
        :type prop: file json data
        """
        self.lists = []
        self.dics = prop
        self.objects = None

    def __iter__(self) -> list:
        if self.lists != []:
            self.objects = self.lists
        elif self.dics != {}:

            # for key in :
            list_key = list(dict(self.dics).keys())
            list_value = list(dict(self.dics).values())
            self.objects = list(zip(list_key, list_value))
        return self
    def __next__(self) -> tuple:
        for obj in self.objects:


            if type(obj) != tuple:
                list(self.objects).pop(0)
                continue
            elif type(obj) == tuple:

                self.objects.pop(0)
                return obj
        if self.objects == []:
            raise StopIteration


def recipes() -> list:
    """
    It's generates
    :return: dictionary
    """
    fileName = "D:\\django-sites\\NetologeDjango\\first_project\\dj-homeworks\\1.2-requests-templates\\recipes\\recipe_basis\\files\\data.json"
    l = []

    with open(file=fileName, encoding="utf-8", mode='r') as file:
        for rec in Basis(json.load(file)):
            rec = list(dict(rec).keys())[0][0: 3]
            l.append(rec)
    return l