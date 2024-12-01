from File_1 import Personal
# Cell 3: Normal Class (inherits from Personal)
class Normal(Personal):
    def __init__(self, name, day, number, room_num, service):
        super().__init__(name, day, number)
        self.room_num = room_num
        self.service = service

    def display_info(self):
        super().display_info()
        print("Room Number:", self.room_num)
        print("Service:", self.service)

    def to_dict(self):
        data = super().to_dict()
        data["Room Number"] = self.room_num
        data["Service"] = self.service
        return data