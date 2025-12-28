SEATS = 50

def view(seats):
    print("\nSeat Status (0 = empty, 1 = booked)")
    for seat in seats:
        print(seat, end=" ")
    print()


def book(seats):
    num = int(input("Enter seat number to book (1-50): "))

    if num < 1 or num > SEATS:
        print("Invalid seat number.")
        return

    if seats[num - 1] == 1:
        print("Seat already booked.")
    else:
        seats[num - 1] = 1
        print(f"Seat {num} booked.")


def cancel(seats):
    num = int(input("Enter seat number to cancel (1-50): "))

    if num < 1 or num > SEATS:
        print("Invalid seat number.")
        return

    if seats[num - 1] == 0:
        print("Seat is not booked.")
    else:
        seats[num - 1] = 0
        print(f"Seat {num} cancelled.")


def main():
    seats = [0] * SEATS   # Initialize all seats as empty

    while True:
        print("\nRailway Reservation")
        print("1. Book Seat")
        print("2. Cancel Seat")
        print("3. View Seats")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            book(seats)
        elif choice == 2:
            cancel(seats)
        elif choice == 3:
            view(seats)
        elif choice == 4:
            print("Thank you.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
