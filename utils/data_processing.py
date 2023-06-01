import csv
import statistics
from datetime import datetime

def process_csv_data(csv_content):
    transactions = []
    credit_total = 0
    debit_total = 0
    transaction_count = 0
    months = {}

    csv_reader = csv.DictReader(csv_content.splitlines())
    for row in csv_reader:
        transaction_id = int(row['Id'])
        transaction_date = datetime.strptime(row['Date'], '%m/%d')
        transaction_amount = float(row['Transaction'])

        transactions.append({
            'id': transaction_id,
            'date': transaction_date,
            'amount': transaction_amount
        })

        if transaction_amount > 0:
            credit_total += transaction_amount
        else:
            debit_total += transaction_amount

        month_key = transaction_date.strftime('%B')
        if month_key in months:
            months[month_key].append(transaction_amount)
        else:
            months[month_key] = [transaction_amount]

        transaction_count += 1

    average_credit_per_month = {}
    average_debit_per_month = {}
    for month, transactions in months.items():
        average_credit_per_month[month] = statistics.mean([t for t in transactions if t > 0])
        average_debit_per_month[month] = statistics.mean([t for t in transactions if t < 0])

    total_balance = credit_total + debit_total

    return transactions, total_balance, average_credit_per_month, average_debit_per_month, transaction_count, months
