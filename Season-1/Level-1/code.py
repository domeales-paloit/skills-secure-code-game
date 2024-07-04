'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import *

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_AMOUNT = 200000
MAX_QUANTITY = 200
MAX_ITEMS = 100
MAX_COST = 1000000

def validorder(order: Order):
    cost = Decimal(0)
    payments = Decimal(0)

    for item_raw in order.items:
        item = Item(*item_raw)

        amount = Decimal(max(-1*MAX_AMOUNT,min(item.amount, MAX_AMOUNT)))
        quantity = Decimal(max(0,min(item.quantity, MAX_QUANTITY)))

        if item.type == 'payment':
            payments += amount
        elif item.type == 'product':
            cost += amount * quantity
        else:
            return "Invalid item type: %s" % item.type

    cost = round(cost,2)
    payments = round(payments,2)

    if cost > MAX_COST:
        return "Total amount payable for an order exceeded"

    if cost == payments:
        return "Order ID: %s - Full payment received!" % order.id
    else:
        net = payments - cost
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
