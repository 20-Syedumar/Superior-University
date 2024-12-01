from File_1 import Personal
# Cell 2: Premium Class (inherits from Personal)
class Premium(Personal):
    def __init__(self, name, day, number, room_num, service, extra):
        super().__init__(name, day, number)
        self.room_num = room_num
        self.service = service
        self.extra = extra

    def display_info(self):
        super().display_info()
        print("Breakfast:", self.extra)
        print("Room Number:", self.room_num)
        print("Service:", self.service)

    def to_dict(self):
        data = super().to_dict()
        data["Room Number"] = self.room_num
        data["Service"] = self.service
        data["Breakfast"] = self.extra
        return data