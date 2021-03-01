def val():
    s = float(input("Shares in Millions: "))
    e = float(input("Net Income: "))
    c = float(input("Cash: "))
    d = float(input("Debt: "))
    g = float(input("10 Year Expected Growth Rate: "))
    p = float(input("Perpetual Growth Rate: "))
    d = float(input("Discount Rate: "))
    e = e/s
    cd = (c - d) / s
    counter = 0
    npv = 0
    while counter < 100:
        npv += e
        if counter < 10:
            e = e * (1 + (g / 100) - (d / 100))
        else:
            e = e * (1 - (d / 100) + (p / 100))
        counter += 1
    return str((npv + cd)) + "\n"


def main():
    run = True
    while run:
        print(val())        

if __name__ == "__main__":
    main()