import matplotlib.pyplot as plt
import numpy as np


class linear_regression:
    def __init__(self):
        # init values
        self.get_data()
        self.theta0 = 0
        self.theta1 = 0
        self.tmptheta0 = 0
        self.tmptheta1 = 0

    def get_data(self):
        # get data from data.csv
        with open("data.csv", "r", encoding="utf-8") as file:
            data = file.read().split()
            data.pop(0)
            km = []
            price = []
            for element in data:
                tmp = element.split(",")
                km.append(float(tmp[0]))
                price.append(float(tmp[1]))
        self.kmList = km
        self.priceList = price

    def save(self):
        # save thetas
        with open("thetas", "w") as file:
            file.write(f"{self.theta0},{self.theta1}")

    def plot(self, flag=0):
        # plot the data
        plt.plot(self.kmList, self.priceList, "ro")
        plt.xlabel("Kilometers")
        plt.ylabel("Price")
        plt.show()

    def estimatePrice(self, mileage):
        return self.theta0 + mileage * self.theta1

    def train(self, learning_rate):
        for i in range(len(self.kmList)):
            self.theta0 += self.estimatePrice(self.kmList[i]) - self.priceList[i]
            self.theta1 += (
                self.estimatePrice(self.kmList[i]) - self.priceList[i] * self.kmList[i]
            )
        self.tmptheta0 *= learning_rate / len(self.kmList)
        self.tmptheta1 *= learning_rate / len(self.kmList)

        return self.theta0, self.theta1


li = linear_regression()
li.train(0.5)
print(li.theta0, li.theta1)
# li.plot()
# print(li.kmList)
