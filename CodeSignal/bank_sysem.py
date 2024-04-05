"""
Copyright Elijah Lopez
"""
import heapq

accounts = dict()
PAYMENTS_LEN = 0
#  use heapq.heappush
#  (timestamp + delay, timestamp, payment_id)
payments_heap = []
# instead of messing with the heap, lazy cancel
payments_metadata = {} # payment_id: ScheduledPayment


class ScheduledPayment:
    def __init__(self, _id, account_id, amount):
        self._id = _id
        self.canceled = False
        self.processed = False
        self.account_id = account_id
        self.amount = amount


class Account:
    # TODO: __slots__
    def __init__(self, account_id, timestamp):
        self.account_id = account_id
        self.amount = 0
        self.total_spend = 0
        # payment ids or references to the object
        self.payments = []
        self.created = timestamp
        self.transactions = []

    def __hash__(self):
        return hash(self.account_id)

    def deposit(self, amount, timestamp):
        self.amount += amount
        self.transactions.append((amount, timestamp))
        return self.amount

    def withdraw(self, amount, timestamp):
        if self.amount < amount:
            raise ValueError('insufficient funds')
        self.amount -= amount
        self.total_spend += amount
        self.transactions.append((-amount, timestamp))
        return self.amount

    def __eq__(self, other):
        if self.account_id == other:
            return True
        return self.account_id == other.account_id

    def get_balance(self, time_at):
        balance = 0
        if time_at < self.created:
            raise ValueError()
        for amount, t in self.transactions:
            if t <= time_at:
                balance += amount
        return balance


def solution(queries):
    output = []
    for query in queries:
        # query = query.split()
        timestamp = int(query[1])
        while payments_heap and payments_heap[0][0] <= timestamp:
            payment_process_time, payment_id = heapq.heappop(payments_heap)
            payment = payments_metadata[payment_id]
            if not payment.canceled:
                try:
                    # todo: use suppress
                    accounts[payment.account_id].withdraw(payment.amount, payment_process_time)
                    payment.processed = True
                except ValueError:
                    pass
        match query[0]:
            case 'CREATE_ACCOUNT':
                if query[2] in accounts:
                    output.append("false")
                else:
                    output.append("true")
                    accounts[query[2]] = Account(query[2], timestamp)
            case 'DEPOSIT':
                try:
                    output.append(str(accounts[query[2]].deposit(int(query[3]), timestamp)))
                except KeyError:
                    output.append('')
            case 'TRANSFER':
                if query[2] not in accounts or query[3] not in accounts:
                    output.append('')
                elif query[2] == query[3]:
                    output.append('')
                else:
                    amount = int(query[4])
                    try:
                        output.append(str(accounts[query[2]].withdraw(amount, timestamp)))
                        accounts[query[3]].deposit(amount, timestamp)
                    except ValueError:
                        output.append('')
            case 'TOP_SPENDERS':
                lst = sorted(accounts.values(), key=lambda acc: (-acc.total_spend, acc.account_id))
                lst_format = ', '.join(f'{acc.account_id}({acc.total_spend})' for acc in lst[:int(query[2])])
                output.append(lst_format)
            case 'SCHEDULE_PAYMENT':
                if query[2] not in accounts:
                    output.append('')
                else:
                    payment_id = f'payment{len(payments_metadata) + 1}'
                    output.append(payment_id)

                    scheduled_payment = ScheduledPayment(payment_id, query[2], int(query[3]))
                    accounts[query[2]].payments.append(payment_id)
                    payments_metadata[payment_id] = scheduled_payment

                    when = timestamp + int(query[4])
                    heapq.heappush(payments_heap, (when, payment_id))

            case 'CANCEL_PAYMENT':
                if query[3] not in payments_metadata:
                    output.append('false')
                else:
                    payment = payments_metadata[query[3]]
                    if payment.canceled or payment.processed or payment.account_id != query[2]:
                        output.append('false')
                    else:
                        payments_metadata[query[3]].canceled = True
                        output.append('true')
            case 'MERGE_ACCOUNTS':
                if query[2] == query[3] or query[2] not in accounts or query[3] not in accounts:
                    output.append('false')
                else:
                    account_to_rm = accounts.pop(query[3])
                    account1 = accounts[query[2]]
                    account1.total_spend += account_to_rm.total_spend
                    account1.amount += account_to_rm.amount
                    for payment_id in account_to_rm.payments:
                        payment = payments_metadata[payment_id]
                        payment.account_id = query[2]
                        account1.payments.append(payment_id)
                    account1.transactions.extend(account_to_rm.transactions)
                    account1.created = min(account1.created, account_to_rm.created)
                    output.append('true')
            case 'GET_BALANCE':
                account = accounts[query[2]]
                time_at = int(query[3])
                try:
                    output.append(str(account.get_balance(time_at)))
                except ValueError:
                    output.append('')
    return output
