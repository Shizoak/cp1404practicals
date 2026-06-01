"""Inputs should be:

    price per kWh in cents,
    daily use in kWh, and
    number of days in the billing period.
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
chosen_tariff = int(input("Which tariff? 11 or 31: "))
daily_kWh_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if chosen_tariff == 11:
    tariff_rate = TARIFF_11
else:
    tariff_rate = TARIFF_31
daily_bill = tariff_rate * daily_kWh_use
total_bill = daily_bill * billing_days
print(f"Estimated bill: ${total_bill:.2f}")
