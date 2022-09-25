class Basis:
    def __init__(self, prop):
        """
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
                # Выпускаем через ретурн и там проверка ключа на совпадение запроса к реуцепту
                self.objects.pop(0)
                return obj
        if self.objects == []:
            raise StopIteration
