class User:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def skip_ads():
        return False


class PremiumUser(User):
    @staticmethod
    def skip_ads():
        return True


# Test №1
print(issubclass(PremiumUser, User))

# Test №2
user = User('Arthur')
premium_user = PremiumUser('Arthur')

print(user.skip_ads())
print(premium_user.skip_ads())
