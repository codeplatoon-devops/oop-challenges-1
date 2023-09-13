from CustomerBankAccount import CustomerBankAccount


class StandardCustomerBankAccount(CustomerBankAccount):
    def __init__(self, account_number, balance, name, email, phone):
        super().__init__(account_number, balance, name, email, phone)
        self.__silver_pts = 0
        self.__reward_trans = []

    def get_silver_pts(self):
        return self.__silver_pts

    def get_reward_trans(self):
        return self.__reward_trans

    def set_silver_pts(self, value):
        self.__silver_pts = value

    def set_reward_trans(self, value):
        self.__reward_trans = value


# Tests
if __name__ == "__main__":
    acct1 = StandardCustomerBankAccount(111, 50, "Steve", "steve@email.com", "123-4567")
    print(acct1.get_silver_pts())  # 0
    acct1.set_silver_pts(200)
    print(acct1.get_silver_pts())  # 200
