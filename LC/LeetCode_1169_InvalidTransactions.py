from collections import defaultdict

"""
https://www.notion.so/paulonteri/Hashtables-Hashsets-220d9f0e409044c58ec6c2b0e7fe0ab5#cf22995975274881a28b544b0fce4716
"""

def invalidTransactions(transactions):
    invalid = []

    # Record all transactions done at a particular time
    #   including the person and the location.
    transaction_time = defaultdict(dict)
    for transaction in transactions:
        name, str_time, amount, city = transaction.split(",")
        time = int(str_time)

        if name not in transaction_time[time]:
            transaction_time[time][name] = set()
            transaction_time[time][name].add(city)
        else:
            transaction_time[time][name].add(city)

    for transaction in transactions:
        name, str_time, amount, city = transaction.split(",")
        time = int(str_time)

        # # check amount
        if int(amount) > 1000:
            invalid.append(transaction)
            continue

        # # check if person did transaction within 60 minutes in a different city
        for inv_time in range(time-60, time+61):
            if inv_time not in transaction_time:
                continue
            if name not in transaction_time[inv_time]:
                continue

            trans_by_name_at_time = transaction_time[inv_time][name]

            # check if transactions were done in a different city
            if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                invalid.append(transaction)
                break

    return invalid

# print(invalidTransactions(["alice,20,800,mtv",
#                            "alice,50,100,mtv",
#                            "alice,50,100,mts",
#                            "alice,51,100,frankfurt"]))

print(invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))