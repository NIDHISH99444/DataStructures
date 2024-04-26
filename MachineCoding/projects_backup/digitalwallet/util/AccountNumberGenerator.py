class AccountNumberGenerator:
    account_number = 0

    @staticmethod
    def get_next_account_number():
        AccountNumberGenerator.account_number += 1
        return AccountNumberGenerator.account_number
