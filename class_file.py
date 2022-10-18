class RegisteredVehicle:
    def __init__(self, vehicle_type: str, vehicle_category: str, toll_tax: int) -> None:
        self._vehicle_type: str = vehicle_type
        self._vehicle_category: str = vehicle_category
        self._toll_tax: int = toll_tax

    def get_toll_tax(self):
        return self._toll_tax


class RegisteredVehicles:
    def __init__(self) -> None:
        self._container = dict()

    def add_vehicle(self, vehicle_type: str, vehicle_category: str, toll_tax: int) -> None:
        self._container[vehicle_type] = RegisteredVehicle(vehicle_type, vehicle_category, toll_tax)

    def get_vehicle_toll_tax(self, vehicle_type: str):
        return self._container[vehicle_type].get_toll_tax()


# tax part

class CrossVehicle:
    def __init__(self, vehicle_id: str, fastag_amount: int = 0) -> None:
        self._vehicle_id: str = vehicle_id
        self._fastag_amount: int = fastag_amount
        self._one_time_pass: bool = False

    def add_one_time_pass(self, pass_time: bool) -> None:
        self._one_time_pass = pass_time

    def add_remain_fastag_ammount(self, fastag_amount: int) -> None:
        self._fastag_amount = fastag_amount

    def get_fastag_amount(self) -> int:
        return self._fastag_amount

    def get_one_time_pass(self) -> bool:
        return self._one_time_pass


class CrossVehicles:
    def __init__(self) -> None:
        self._fastag_container = dict()
        self._non_fastag_container = dict()

    def add_fastag_tax(self, vehicle_id: str, fastag_amount: int) -> None:
        self._fastag_container[vehicle_id] = CrossVehicle(vehicle_id, fastag_amount)

    def add_non_fastag_tax(self, vehicle_id: str) -> None:
        self._non_fastag_container[vehicle_id] = CrossVehicle(vehicle_id)

    def add_pass_time(self, vehicle_id: str, pass_time: bool) -> None:
        if vehicle_id in list(self._fastag_container.keys()):
            self._fastag_container[vehicle_id].add_one_time_pass(pass_time)
        elif vehicle_id in list(self._non_fastag_container.keys()):
            self._non_fastag_container[vehicle_id].add_one_time_pass(pass_time)

    def add_remain_fastag_amount(self, vehicle_id: str, fastag_amount: int) -> None:
        if vehicle_id in list(self._fastag_container.keys()):
            self._fastag_container[vehicle_id].add_remain_fastag_ammount(fastag_amount)
        elif vehicle_id in list(self._non_fastag_container.keys()):
            self._non_fastag_container[vehicle_id].add_remain_fastag_ammount(fastag_amount)

    def get_amount(self, vehicle_id: str) -> int:
        if vehicle_id in list(self._fastag_container.keys()):
            return self._fastag_container[vehicle_id].get_fastag_amount()
        elif vehicle_id in list(self._non_fastag_container.keys()):
            return self._non_fastag_container[vehicle_id].get_fastag_amount()

    def get_pass_time(self, vehicle_id: str) -> bool:
        if vehicle_id in list(self._fastag_container.keys()):
            return self._fastag_container[vehicle_id].get_one_time_pass()
        elif vehicle_id in list(self._non_fastag_container.keys()):
            return self._non_fastag_container[vehicle_id].get_one_time_pass()

    def get_vehicles_name(self, vehicle_id: str) -> bool:
        if vehicle_id in list(self._fastag_container.keys()):
            return True
        elif vehicle_id in list(self._non_fastag_container.keys()):
            return True
        else:
            return False
