import json


class Basis:
    def __init__(self, prop):
        """
        Class is iterator/
        To works with large data file json
        :tuple prop: file json data
        """
        self.lists = []
        self.dics = prop
        self.objects = None

    def __iter__(self) -> list:
        if self.lists != []:
            self.objects = self.lists
        elif self.dics != {}:

            list_key = list(dict(self.dics).keys())
            list_value = list(dict(self.dics).values())
            self.objects = list(zip(list_key, list_value))
        return self

    def __next__(self) -> tuple:
        for obj in self.objects:
            print(f"dfsis {obj}")

            if type(obj) != tuple:
                list(self.objects).pop(0)
                continue
            elif type(obj) == tuple:

                self.objects.pop(0)
                return obj
        if self.objects == []:
            raise StopIteration


class Calc:

    def __init__(self, pathFile: str, recipe: str, number: int):
        self.pathFile = pathFile
        self.recipe = recipe
        self.number = number

    def filtCalc(self) -> list:

        with open(self.pathFile, encoding="utf-8", mode="r") as file:
            f = json.load(file)

            print(f"""fff \n {[ response for response in Basis(f) if tuple(response)[0] == self.recipe]}""")
            recepe_response = [ response for response in Basis(f) if tuple(response)[0] == self.recipe]
            return recepe_response

    def calc(self) -> list:
        recepe_response = Calc.filtCalc(self)
        print(f"Response: {recepe_response}")

        product = list(dict(list(recepe_response)[0][1]).keys())
        numbers = list(dict(list(recepe_response)[0][1]).values())
        for i, elem in enumerate(numbers):
            print(f"""product: {product},
numbers: {numbers},
i: {i}, elem: {elem}""")

            numbers[i] *= self.number
        print(f"Numbers[i]: {numbers}")
        response = list(zip(product, numbers))
        print(f"Response: {response}")
        return response
