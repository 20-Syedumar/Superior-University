# Cell 1: Personal Class
class Personal:
    def __init__(self, name, day, number):
        self._name = name
        self.day = day
        self.__number = number

    # Getter Part
    def get_name(self):
        return self._name

    def get_number(self):
        return self.__number

    # Setter Part
    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self.__number = number

    # Display Part
    def display_info(self):
        print("Name:", self._name)
        print("Day:", self.day)
        print("Number:", self.__number)

    # Convert to dictionary for CSV export
    def to_dict(self):
        return {
            "Name": self._name,
            "Day": self.day,
            "Number": self.__number
        }
