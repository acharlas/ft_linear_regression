theta0 = 0.0
theta1 = 0.0

with open("thetas", "r") as file:
    try:
        data = file.read().split(",")
        theta0 = float(data[0])
        theta1 = float(data[1])

    except:
        print("Error reading file")


def EstimatedPrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


mileage = float(input("Mileage: "))
print(EstimatedPrice(mileage, theta0, theta1))
