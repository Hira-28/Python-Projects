import numpy as np

# Base Transport class
class Transport:
    def __init__(self, transport_id, departure, destination, date):
        self.transport_id = transport_id
        self.departure = departure
        self.destination = destination
        self.date = date

    def display(self):
        print(f"Transport ID: {self.transport_id}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")
        print(f"Date: {self.date}")
        print("------------------")


# Bus, Train, Launch, Plane classes using inheritance and polymorphism
class Bus(Transport):
    def __init__(self, transport_id, departure, destination, date, bus_type, available_seats):
        super().__init__(transport_id, departure, destination, date)
        self.bus_type = bus_type
        self.available_seats = available_seats

    def display(self):
        super().display()
        print(f"Bus Type: {self.bus_type}")
        print(f"Available Seats: {self.available_seats}")
        print("------------------")


class Train(Transport):
    def __init__(self, transport_id, departure, destination, date, train_name, available_seats):
        super().__init__(transport_id, departure, destination, date)
        self.train_name = train_name
        self.available_seats = available_seats

    def display(self):
        super().display()
        print(f"Train Name: {self.train_name}")
        print(f"Available Seats: {self.available_seats}")
        print("------------------")


class Launch(Transport):
    def __init__(self, transport_id, departure, destination, date, launch_name, cabin_class):
        super().__init__(transport_id, departure, destination, date)
        self.launch_name = launch_name
        self.cabin_class = cabin_class

    def display(self):
        super().display()
        print(f"Launch Name: {self.launch_name}")
        print(f"Cabin Class: {self.cabin_class}")
        print("------------------")


class Plane(Transport):
    def __init__(self, transport_id, departure, destination, date, flight_number, available_seats):
        super().__init__(transport_id, departure, destination, date)
        self.flight_number = flight_number
        self.available_seats = available_seats

    def display(self):
        super().display()
        print(f"Flight Number: {self.flight_number}")
        print(f"Available Seats: {self.available_seats}")
        print("------------------")


# Ticket class
class Ticket:
    def __init__(self, ticket_id, passenger_name, departure, destination, transport_type, transport_id):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.departure = departure
        self.destination = destination
        self.transport_type = transport_type
        self.transport_id = transport_id

    def display(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")
        print(f"Transport Type: {self.transport_type}")
        print(f"Transport ID: {self.transport_id}")
        print("------------------")


# Transport Management System
class TransportSchedule:
    def __init__(self):
        self.transports = []  # List to store transport objects

    def add_transport(self, transport):
        if any(t.transport_id == transport.transport_id for t in self.transports):
            print(f"Transport with ID {transport.transport_id} already exists.")
        else:
            self.transports.append(transport)
            print("\nTransport added successfully!\n")

    def display_transports(self):
        print("\nTransport Schedule:")
        print("------------------")

        if not self.transports:
            print("No transports scheduled yet.\n")
        else:
            for transport in self.transports:
                transport.display()


# Ticket Management System
class TicketManagementSystem:
    def __init__(self):
        self.tickets = []  # List to store tickets
        self.ticket_stats = {}  # Dictionary to count tickets by transport type

    def add_ticket(self, ticket):
        try:
            ticket_ids = {t.ticket_id for t in self.tickets}
            if ticket.ticket_id in ticket_ids:
                raise ValueError("A ticket with this ID already exists.")
            self.tickets.append(ticket)
            self.ticket_stats[ticket.transport_type] = self.ticket_stats.get(ticket.transport_type, 0) + 1
            print("\nTicket confirmed successfully!\n")
        except ValueError as e:
            print(f"\nError: {e}\n")

    def remove_ticket(self, ticket_id):
        try:
            ticket = next(t for t in self.tickets if t.ticket_id == ticket_id)
            self.tickets.remove(ticket)
            self.ticket_stats[ticket.transport_type] -= 1
            if self.ticket_stats[ticket.transport_type] == 0:
                del self.ticket_stats[ticket.transport_type]
            print("\nTicket removed successfully!\n")
        except StopIteration:
            print("\nTicket not found.\n")

    def display_tickets(self):
        print("\n")
        if not self.tickets:
            print("No tickets found.\n")
        else:
            print("Confirmed Ticket List:")
            for ticket in self.tickets:
                ticket.display()

    def display_statistics(self):
        print("\nTicket Statistics:")
        for transport_type, count in self.ticket_stats.items():
            print(f"{transport_type} Tickets: {count}")
        print("------------------")


# Fare Calculation with NumPy and Lambda
def calculate_fare(distances, base_fare):
    """
    Calculate fare using NumPy and lambda functions.
    :param distances: List or array of distances
    :param base_fare: Base fare for tickets
    :return: List of fares
    """
    distances = np.array(distances)
    fares = list(map(lambda d: base_fare + d * 0.1, distances))
    return fares


# Main Function
def main():
    transport_schedule = TransportSchedule()
    ticket_system = TicketManagementSystem()
    base_fare = 100

    while True:
        print("1. Add a Transport")
        print("2. View Transports")
        print("3. Add a Ticket")
        print("4. Remove a Ticket")
        print("5. Display Tickets")
        print("6. Display Ticket Statistics")
        print("7. Calculate Fare")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        try:
            if choice == 1:
                print("Select Transport Type: 1. Bus 2. Train 3. Launch 4. Plane")
                transport_type = int(input("Enter your choice: "))
                transport_id = input("Enter Transport ID: ")
                departure = input("Enter departure: ")
                destination = input("Enter destination: ")
                date = input("Enter date (YYYY-MM-DD): ")

                if transport_type == 1:
                    bus_type = input("Enter Bus Type (AC/Non-AC): ")
                    available_seats = int(input("Enter available seats: "))
                    transport = Bus(transport_id, departure, destination, date, bus_type, available_seats)

                elif transport_type == 2:
                    train_name = input("Enter Train Name: ")
                    available_seats = int(input("Enter available seats: "))
                    transport = Train(transport_id, departure, destination, date, train_name, available_seats)

                elif transport_type == 3:
                    launch_name = input("Enter Launch Name: ")
                    cabin_class = input("Enter Cabin Class (Economy/Business): ")
                    transport = Launch(transport_id, departure, destination, date, launch_name, cabin_class)

                elif transport_type == 4:
                    flight_number = input("Enter Flight Number: ")
                    available_seats = int(input("Enter available seats: "))
                    transport = Plane(transport_id, departure, destination, date, flight_number, available_seats)

                else:
                    print("Invalid transport type.")
                    continue

                transport_schedule.add_transport(transport)

            elif choice == 2:
                transport_schedule.display_transports()

            elif choice == 3:
                ticket_id = int(input("Enter ticket ID: "))
                passenger_name = input("Enter passenger name: ")
                departure = input("Enter departure: ")
                destination = input("Enter destination: ")
                transport_type = input("Enter transport type (Bus/Train/Launch/Plane): ")
                transport_id = input("Enter transport ID: ")
                ticket = Ticket(ticket_id, passenger_name, departure, destination, transport_type, transport_id)
                ticket_system.add_ticket(ticket)

            elif choice == 4:
                ticket_id = int(input("Enter ticket ID to remove: "))
                ticket_system.remove_ticket(ticket_id)

            elif choice == 5:
                ticket_system.display_tickets()

            elif choice == 6:
                ticket_system.display_statistics()

            elif choice == 7:
                distances = tuple(map(float, input("Enter distances (comma-separated): ").split(",")))
                fares = calculate_fare(distances, base_fare)
                print(f"Fares for distances {distances}: {fares}")

            elif choice == 8:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

        print()


# Run the main function
main()
