
class GenerateRandomNumber:
    accountNumber = 0

    @staticmethod
    def generateNumber():
        GenerateRandomNumber.accountNumber += 1
        return GenerateRandomNumber.accountNumber
