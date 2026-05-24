from datetime import datetime

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []
        self.last_interaction = None

    def add_interaction(self, interaction): #Metoden lägger till en ny interaktion i kundens lista och uppdaterar datumet för senaste interaktionen
        self.interactions.append(interaction)
        self.last_interaction = datetime.now()

    def calculate_days_since_last_interaction(self): 
        if self.last_interaction is None:
            return None
        return (datetime.now() - self.last_interaction).days

    def is_inactive(self):
        days = self.calculate_days_since_last_interaction()
        return days is not None and days > 30

class CustomerDataSystem:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        for customer in self.customers:
            if customer.email == email:
                raise ValueError(
                    "En kund med denna e-postadress finns redan i systemet."
                )
        self.customers.append(Customer(name, email, phone))
        print(f"Ny kund med namn {name} har lagts till.")

    def remove_customer(self, email):
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print(f"Kund med e-post {email} har tagits bort.")
                return
        raise KeyError("Kunden finns inte i systemet.")

    def update_customer_contact(self, email, new_email=None, new_phone=None):
        for customer in self.customers:
            if customer.email == email:
                if new_email:
                    customer.email = new_email
                if new_phone:
                    customer.phone = new_phone
                print(f"Kontaktinformation för {customer.name} har uppdaterats.")
                return
        raise KeyError("Kunden finns inte i systemet.")

    def add_interaction_to_customer(self, email, interaction):
        for customer in self.customers:
            if customer.email == email:
                customer.add_interaction(interaction)
                print(f"Interaktion har lagts till för {customer.name}.")
                return
        raise KeyError("Kunden finns inte i systemet.")

    def get_customer_interactions(self, email):
        for customer in self.customers:
            if customer.email == email:
                print(f"Interaktioner för {customer.name}:")
                return customer.interactions
        raise KeyError("Kunden finns inte i systemet.")

    def print_all_customers(self):
        print("Alla kunder i systemet:")
        for customer in self.customers:
            print(f"- {customer.name}, {customer.email}, {customer.phone}")

    def print_inactive_customers(self): #VG
        print("Inaktiva kunder (över 30 dagar):")
        found = False
        for customer in self.customers:
            if customer.is_inactive():
                days = customer.calculate_days_since_last_interaction()
                print(
                    f"- {customer.name}, {days} dagar sedan senaste interaktion"
                )
                found = True
        if not found:
            print("Inga inaktiva kunder hittades.")


# DEMONSTRATION
if __name__ == "__main__":
    system = CustomerDataSystem("Dagnord")

    system.add_customer("Anna", "anna@mail.com", "0701234567")
    system.add_customer("Ivan", "ivan@mail.com", "0707654321")

    system.add_interaction_to_customer("anna@mail.com", "Telefon")

    system.print_all_customers()
    system.print_inactive_customers()

    try:
        system.add_customer("Anika", "anna@mail.com", "000")
    except ValueError as e:
        print("Fel:", e)

    try:
        system.remove_customer("patrik@mail.com")
    except KeyError as e:
        print("Fel:", e)
