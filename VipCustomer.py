from StandardCustomerBankAccount import StandardCustomerBankAccount


class VipCustomer(StandardCustomerBankAccount):
    def __init__(
        self,
        account_number,
        balance,
        name,
        email,
        phone,
    ):
        super().__init__(account_number, balance, name, email, phone)
        self.__gold_pts = 0

    def get_gold_pts(self):
        return self.__gold_pts

    def set_gold_pts(self, value):
        self.__gold_pts = value


# Tests
if __name__ == "__main__":
    cust1 = VipCustomer(123, 1000, "Steve", "steve@email.com", "123-4567")
    print("Account Info:")
    print("------------")
    print(cust1)
    print("------------")
    print(cust1.get_gold_pts())
    print(cust1.set_gold_pts(222))  # bug - setter is also returning None
    print(cust1.get_gold_pts())
