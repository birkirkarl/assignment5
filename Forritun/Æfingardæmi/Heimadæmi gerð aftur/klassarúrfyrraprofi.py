class OrderLine(object):
    def __init__(self, name, price, number, discount):
        self.name=name
        self.price = price
        self.number = number
        self.discount = discount
    
    def __str__(self):
        return "{0:<10}{1:<9}{2:<11}{3:<12}{4:<5}".format(self.name, self.price, self.number, self.discount, self.price * self.number)




class Order(object):
    def __init__(self):
        self.lines = []

    def __str__(self):
        result = 'Product   Price   Quantity   Discount    Total \n'
        result += '==============================================\n'
        for line in self.lines:
            result += '{0}\n'.format(str(line))
        result += '==============================================\n'
        total, totalExcludingDiscount, discount = self.getTotals()
        result += 'Total excluding discount : {0:>21.0f}\n'.format(totalExcludingDiscount)
        result += 'Total discount: {0:>31.0f}\n'.format(discount)
        result += 'Total: {0:>40.0f}\n'.format(total)
        return result


    def addLine(self, name, price, number, discount):
        self.lines.append(OrderLine(name, price, number,discount))

    def getTotals(self):
        total_ex = 0
        total_disc = 0
        for line in self.lines:
            total_ex += line.price * line.number
            total_disc += line.price * line.number * (line.discount / 100)
        return total_ex - total_disc, total_ex, total_disc


def main():
    order = Order() 
    order.addLine("eggs", 60, 12, 0)
    order.addLine("bread", 200, 1, 10)
    order.addLine("milk", 120, 2, 5)
    total, _, _ = order.getTotals()
    print("The total price is: {0:0f}".format(total))
    print(order)

main()