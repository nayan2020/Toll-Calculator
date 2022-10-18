from collections import OrderedDict

from class
_file import RegisteredVehicles, CrossVehicles
from sys import argv


def main():
    registered_vehicles = [
        ["TRUCK", "Heavy vehicle", 200],
        ["BUS", "Heavy vehicle", 200],
        ["VAN", "Light vehicle", 100],
        ["CAR", "Light vehicle", 100],
        ["RICKSHAW", "Light vehicle", 100],
        ["SCOOTER", "Two wheeler", 50],
        ["MOTORBIKE", "Two wheeler", 50],
    ]
    vehicles = RegisteredVehicles()
    for vehicle in registered_vehicles:
        vehicles.add_vehicle(vehicle[0], vehicle[1], vehicle[2])

    tax_collector = CrossVehicles()
    # main part
    total_discount = 0
    pay_using_fastag = 0
    pay_using_cash = 0
    amount_limit_0 = 0
    cash_tax = 40  # given

    crossed_vehicle = dict()  # store summary

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    for line in lines:
        line = line.split(" ")
        if line[0] == "FASTAG":
            tax_collector.add_fastag_tax(line[1], int(line[2]))

        elif line[0] == "COLLECT_TOLL":
            vehicle_type = line[1]
            vehicle_id = line[2][:-1]

            if tax_collector.get_vehicles_name(vehicle_id):
                vehicle_tax = vehicles.get_vehicle_toll_tax(vehicle_type)
                # 2nd time tax will be 50%
                if tax_collector.get_pass_time(vehicle_id):
                    vehicle_tax = vehicle_tax * 0.5
                    total_discount += vehicle_tax

                fastag_amount = tax_collector.get_amount(vehicle_id)
                cash_amount = vehicle_tax - fastag_amount

                if cash_amount > amount_limit_0:
                    pay_using_cash += cash_amount + cash_tax

                    used_fastag = vehicle_tax - cash_amount
                    # update the fastag ammount
                    tax_collector.add_remain_fastag_amount(vehicle_id, fastag_amount - used_fastag)
                    pay_using_fastag += used_fastag
                else:
                    used_fastag = vehicle_tax
                    # update the fastag ammount
                    tax_collector.add_remain_fastag_amount(vehicle_id, fastag_amount - used_fastag)
                    pay_using_fastag += used_fastag
            else:
                if not tax_collector.get_vehicles_name(vehicle_id):
                    tax_collector.add_non_fastag_tax(vehicle_id)

                cash_amount = vehicles.get_vehicle_toll_tax(vehicle_type)
                pay_using_cash += cash_amount + cash_tax

            # change the passing parameter
            pass_time: bool = tax_collector.get_pass_time(vehicle_id)
            if not pass_time:
                tax_collector.add_pass_time(vehicle_id, True)
            else:
                tax_collector.add_pass_time(vehicle_id, False)

            # vehicle type details store in as dict
            # vehicle type details
            if vehicle_type in crossed_vehicle:
                crossed_vehicle[line[1]] = crossed_vehicle[vehicle_type] + 1
            else:
                crossed_vehicle[vehicle_type] = 1

        elif line[0] == "PRINT_COLLECTION":
            print_final_summery(pay_using_fastag, pay_using_cash, total_discount, crossed_vehicle)


def print_final_summery(pay_using_fastag: int, pay_using_cash: int, total_discount: int, crossed_vehicle: dict) -> None:
    # print of the getting
    total_amount = pay_using_cash + pay_using_fastag

    print(f"TOTAL_COLLECTION {int(total_amount)} {int(total_discount)}")
    print(f"PAYMENT_SUMMARY {int(pay_using_fastag)} {int(pay_using_cash)}")
    print("VEHICLE_TYPE_SUMMARY")

    vehicle = OrderedDict(sorted(crossed_vehicle.items(), key=lambda kv: kv[0]))
    sorted_list = sorted(vehicle.items(), key=lambda kv: kv[1], reverse=True)
    for item in sorted_list:
        print(f'{item[0]} {item[1]}')


if __name__ == "__main__":
    main()
