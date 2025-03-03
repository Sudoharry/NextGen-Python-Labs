#.. WAF to convert USD into INR

## Take user input of how much $$ needs to convert into INR


usd_value = int(input("Enter the dollar for conversion:"))

# convert = usd_value * 87

# print(usd_value, "dollars in INR is", convert)


def conv_money(usd_value):
    inr_value = usd_value * 87
    print(usd_value, "USD = ", inr_value, "INR")

conv_money(usd_value)