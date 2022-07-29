class MyCustomList(list):

    def __getitem__(self, item):
        print("getting item")
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if value < 1:
            print("Not adding it")
            return
        super().__setitem__(key, value)

    def append(self, item) -> None:
        if item < 1:
            return
        super().append(item)


c = MyCustomList()
print(c)
c.append(9)
c.append(-1)
print(c[0])
c[1] = -6
print(c)


class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.save_dict()

    def save_dict(self):
        with open("config.txt", "a") as f:
            for key, value in self.items():
                f.write("{} = {}\n".format(key, value))


my_dict = MyDict()
my_dict["name"] = "David"
my_dict["age"] = 21
print(my_dict)
