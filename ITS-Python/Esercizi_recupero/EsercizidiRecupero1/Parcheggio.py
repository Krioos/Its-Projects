def calculateCharges(clients: dict[int, float]) -> None:
    sum_charge = 0
    total_hours = 0
    print(f"{'Car':<10}{'Hours':<15}{'Charge'}")
    for car, hours in clients.items():
        if hours <= 3:
            charge = 2.00
        else:
            charge = min(2.00 + (hours - 3) * 0.50, 10.00)
        sum_charge += charge
        total_hours += hours
        print(f"{car:<10}{hours:<15.1f}{charge:>6.2f} $")
    print(f"{'TOTAL':<10}{total_hours:<15.1f}{sum_charge:>6.2f} $")

dict = {
    "1": 1.5,
    "2": 4, 
    "3": 24
}
calculateCharges(dict)