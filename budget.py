class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount, 
            'description': description
            })

    def withdraw(self, amount, description=''):
        
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description
        })
        return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']

        return balance

    def transfer(self, amount, category):

        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        balance = self.get_balance()

        if balance >= amount:
            return True
        else: 
            return False

    def __str__(self):
        result = self.name.center(30, '*') + "\n"

        for item in self.ledger:
            amount = item["amount"]
            description = item["description"]
            description = description[:23]
            result += f"{description:<23}{amount:>7.2f}\n"

        result += f"Total: {self.get_balance()}"
        return result

def create_spend_chart(categories):
    bar_chart = f"Percentage spent by category\n"
    spent_dict = {}
    for category in categories:
        spent_amount = 0

        for item in category.ledger:
            if item['amount'] < 0:
                spent_amount += abs(item['amount'])
        spent_dict[category.name]= spent_amount
    
    total_spent = sum(spent_dict.values())
    
    for key in spent_dict:
        percentage = (spent_dict[key]*100)/total_spent
        spent_dict[key] =  int(percentage // 10) * 10
    
    for percentage in range(100, -1, -10):
        result = f"{percentage:>3}| "
        for category in spent_dict:
            if spent_dict[category] >= percentage:
                result += "o  "
            else: 
                result += "   "

        bar_chart += result + "\n"

    bar_chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)

    for index in range(max_length):
        row = "     "

        for category in categories:
            if index < len(category.name):
                row += category.name[index] + "  "
            else:
                row += "   "

        bar_chart += row + "\n"
    print(bar_chart[:-1])
    return bar_chart[:-1]

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(100, 'groceries')
food.withdraw(100, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(200, clothing)
clothing.withdraw(100, 'groceries')
# print(food)
# print(clothing)

create_spend_chart([food,clothing])