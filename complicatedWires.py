isLastSerialNumberDigitEven = False
moreThanTwoBatteries = False
hasParallelPort = False

cut = True

# last digit is even
while True:
    answer = input("Czy ostatnia cyfra numeru seryjnego jest parzysta? ").lower()
    if answer == "t":
        isLastSerialNumberDigitEven = True
        break
    elif answer == "f" or answer == "n":
        isLastSerialNumberDigitEven = False
        break

# more than two batteries?
while True:
    answer = input("Czy ma więcej niż 2 baterie? ").lower()
    if answer == "t":
        moreThanTwoBatteries = True
        break
    elif answer == "f" or answer == "n":
        moreThanTwoBatteries = False
        break

# parallel port
while True:
    answer = input("Czy ma port równoległy? ").lower()
    if answer == "t":
        hasParallelPort = True
        break
    elif answer == "f" or answer == "n":
        hasParallelPort = False
        break

cutArray = [
    True, False, True, moreThanTwoBatteries, isLastSerialNumberDigitEven, hasParallelPort, False, hasParallelPort,
    isLastSerialNumberDigitEven, moreThanTwoBatteries, True, moreThanTwoBatteries, False, isLastSerialNumberDigitEven,
    hasParallelPort, False
]

while True:

    hasSymbol = 0
    isLedOn = 0
    isRed = 0
    isBlue = 0
    text = input("Podaj r(czerwony) b(niebieski) s(symbol) l(LED) e(koniec): ").lower()
    if "r" in text:
        isRed = 1
    if "b" in text:
        isBlue = 1
    if "s" in text:
        hasSymbol = 1
    if "l" in text:
        isLedOn = 1
    if "e" in text:
        break

    idx = isRed*2**3 + isBlue*2**2 + hasSymbol*2 + isLedOn
    cut = cutArray[idx]

    if cut:
        print("Cut")
    else:
        print("Don't cut")
