# Functions

# variables
# For every 40 hours, the employee gets 4 hours of paid vacation
vacation_factor = 4


# Calculate amount based on hourly rate
def calculate_amount_by_hourly_rate(hours, base_rate, over_time_rate):
    if hours <= 80:
        base_hours = hours
        over_time_hours = 0

    if hours > 80:
        base_hours = 80
        over_time_hours = hours - 80

    return base_hours * base_rate + over_time_hours * over_time_rate


def calculate_paid_vacation_hours(hours_worked):
    return round(hours_worked/40, 2) * vacation_factor


def main():
    input_hours = float(input('Enter Hours : '))
    input_base_rate = float(input('Base Rate : '))
    input_over_time_rate = float(input('Overtime Rate : '))
    amount = calculate_amount_by_hourly_rate(input_hours, input_base_rate, input_over_time_rate)
    user_vacation_hours = calculate_paid_vacation_hours(input_hours)
    print("------------------------------------")
    print("Amount ", amount)
    print("Vacation Hours ", user_vacation_hours)


if __name__ == '__main__':
    main()



