class Ticket:
    def __init__(self, ticket_id, passenger_name, departure, destination):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.departure = departure
        self.destination = destination

    def display(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")
        print("------------------")


class TicketManagementSystem:
    def __init__(self):
        self.tickets = []  # List to store tickets

    def add_ticket(self, ticket):
        # Check if the ticket ID already exists
        if any(t.ticket_id == ticket.ticket_id for t in self.tickets):
            print("\nA ticket with this ID already exists. Please try again.\n")
        else:
            self.tickets.append(ticket)
            print("\nThis Ticket confirmed successfully!\n")

    def remove_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                self.tickets.remove(ticket)
                print("\nThis Ticket removed successfully!\n")
                return
        print("\nTicket not found.\n")

    def display_tickets(self):
        print("\n")
        if not self.tickets:
            print("No tickets found.\n")
        else:
            print("Confirmed Ticket Lists are Here:\n")
            for ticket in self.tickets:
                ticket.display()


# Specialized ticket types inheriting from the Ticket class
class EconomyTicket(Ticket):
    def __init__(self, ticket_id, passenger_name, departure, destination, baggage_allowance):
        super().__init__(ticket_id, passenger_name, departure, destination)
        self.baggage_allowance = baggage_allowance

    def display(self):
        super().display()
        print(f"Baggage Allowance: {self.baggage_allowance} kg")
        print("------------------")


class BusinessTicket(Ticket):
    def __init__(self, ticket_id, passenger_name, departure, destination, lounge_access):
        super().__init__(ticket_id, passenger_name, departure, destination)
        self.lounge_access = lounge_access

    def display(self):
        super().display()
        print(f"Lounge Access: {'Yes' if self.lounge_access else 'No'}")
        print("------------------")


# Menu-driven logic
def main():
    system = TicketManagementSystem()
    while True:
        print("1. Add an Economy Ticket")
        print("2. Add a Business Ticket")
        print("3. Remove a Ticket")
        print("4. Display Tickets")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ticket_id = int(input("Enter ticket ID: "))
            passenger_name = input("Enter passenger name: ")
            departure = input("Enter departure: ")
            destination = input("Enter destination: ")
            baggage_allowance = float(input("Enter baggage allowance (kg): "))
            ticket = EconomyTicket(ticket_id, passenger_name, departure, destination, baggage_allowance)
            system.add_ticket(ticket)

        elif choice == 2:
            ticket_id = int(input("Enter ticket ID: "))
            passenger_name = input("Enter passenger name: ")
            departure = input("Enter departure: ")
            destination = input("Enter destination: ")
            lounge_access = input("Lounge access (yes/no): ").strip().lower() == "yes"
            ticket = BusinessTicket(ticket_id, passenger_name, departure, destination, lounge_access)
            system.add_ticket(ticket)

        elif choice == 3:
            ticket_id = int(input("Enter ticket ID to remove: "))
            system.remove_ticket(ticket_id)

        elif choice == 4:
            system.display_tickets()

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


# Call the main function
main()
