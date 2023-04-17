class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number=number
        
        from employee import Employee

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_pay_rate):
        super().__init__(name, number)
        self._shift = shift
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift(self):
        return self._shift

    def set_shift(self, shift):
        self._shift = shift

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate =hourly_pay_rate
        
        from production_worker import ProductionWorker


name = input("Enter employee name: ")
number = input("Enter employee number: ")
shift = int(input("Enter shift (1 for day, 2 for night): "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))

employee = ProductionWorker(name, number, shift, hourly_pay_rate)


print("Employee Name:", employee.get_name())
print("Employee Number:", employee.get_number())
print("Shift:", employee.get_shift())
print("Hourly Pay Rate:", employee.get_hourly_pay_rate())
