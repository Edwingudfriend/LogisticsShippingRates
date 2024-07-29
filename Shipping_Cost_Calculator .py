# SHiping Cost Calculator

##Input package weight and shiping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

##Calculate Shipping cost
shipping_cost = weight * rate

## Dispaly the result
print(f"Shipping Cost: {shipping_cost} USD")
