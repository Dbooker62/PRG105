from office_furniture import OfficeFurniture
from desk import Desk
from filing_cabinet import FilingCabinet


def main():
    office_furniture = OfficeFurniture("Chair", "Wood", 40, 30, 35, 150)

    desk = Desk("Desk", "Metal", 60, 30, 30, 200, "Right", 3)

    filing_cabinet = FilingCabinet("Filing Cabinet", "Steel", 20, 18, 50, 100, 4, "Keyed")

    print(office_furniture)
    print(desk)
    print(filing_cabinet)


if __name__ == "__main__":
    main() 
    
    
    
    
    from office_furniture import OfficeFurniture

class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_of_drawers):
        super().__init__(category, material, length, width, height, price)
        self.location_of_drawers = location_of_drawers
        self.number_of_drawers = number_of_drawers

    def __str__(self):
        return super().__str__() + f", Location of Drawers: {self.location_of_drawers}, Number of Drawers: {self.number_of_drawers}"
      
      
      
      from office_furniture import OfficeFurniture

class FilingCabinet(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, number_of_drawers, lock_type):
        super().__init__(category, material, length, width, height, price)
        self.number_of_drawers = number_of_drawers
        self.lock_type = lock_type

    def __str__(self):
        return super().__str__() + f", Number of Drawers: {self.number_of_drawers}, Lock Type: {self.lock_type}"
      
      
      from office_furniture import OfficeFurniture
from desk import Desk
from filing_cabinet import FilingCabinet


def main():
    office_furniture = OfficeFurniture("Chair", "Wood", 40, 30, 35, 150)

    desk = Desk("Desk", "Metal", 60, 30, 30, 200, "Right", 3)

    filing_cabinet = FilingCabinet("Filing Cabinet", "Steel", 20, 18, 50, 100, 4, "Keyed")

    print(office_furniture)
    print(desk)
    print(filing_cabinet)


if __name__ == "__main__":
    main()
