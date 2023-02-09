#Pierwsza klasa, która pobiera i sprawdza wprowadzone dane
class PobieranieDanych:

    def __init__(self):
        self.data = {}

    def get_data(self):
        print('Witam! Ten program pomoże obliczyć twoje wydatki, wystarczy tylko wprowadzić dane:)')
        while True:
            try:
                expenses = float(input("Wprowadź wydatki (przykład: 90.95): "))
                month = input("Wpisz miesiąc (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sept, Oct, Nov, Dec): ")
                if month not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]:
                    raise ValueError("Nieprawidłowy miesiąc. Proszę wpisać kwotę i miesiąc ponownie")
                self.data[month] = expenses
                ask = input("Wprowadzić więcej danych? (y/n)")
                if ask == "n" or ask == "N":
                    break
            except ValueError:
                print('Error')
#Sprawdzenie wprowadzonej kwoty - nie powinna być ujemna. Jeśli jest taka liczba - to para klucz-wartość będą usunięte

    def check_data(self):
        for key, value in self.data.copy().items():
            if value < 0:
                print("Wprowadzona liczba jest ujemna w miesiącu: ", key, "- liczba została usunięta z analizy.")
                del self.data[key]


#Druga klasa, która oblicza łączne wydatki oraz podsumowuje wydatki w każdym miesiącu
class PrzetwarzanieDanych:
    def __init__(self):
        self.data = {}
        self.total_expenses = 0

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def calculate_total(self):
        for value in self.data.values():
            self.total_expenses += value
        return self.total_expenses

    def display_data(self):
        for key, value in self.data.items():
            print("Miesiąc: ", key, "Wydatki: ", value)
        print("Łączne wydatki: ", self.total_expenses)

#Trzecia klasa, która wizualizuje wydatki za pomocą wykresu i biblioteki matplotlib
class WizualizacjaDanych:
    def __init__(self):
        pass

    def display_graph(self, data):
        import matplotlib.pyplot as plt
        months = list(data.keys())
        expenses = list(data.values())
        plt.plot(months, expenses)
        #plt.bar(months, expenses) - lepiej pokaże dane, jeśli użytkownik np. wprowadzi tylko jedną wartość
        plt.xlabel("Miesiąc")
        plt.ylabel("Wydatki")
        plt.show()


data_class1 = PobieranieDanych()
data_class1.get_data()
data_class1.check_data()
data_class2 = PrzetwarzanieDanych()
data_class2.set_data(data_class1.data)
data_class2.calculate_total()
data_class2.display_data()
data_class3 = WizualizacjaDanych()
data_class3.display_graph(data_class2.get_data())
