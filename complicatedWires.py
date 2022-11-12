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

while True:

    hasSymbol = False
    isLedOn = False
    isRed = False
    isBlue = False
    text = input("Podaj r(czerwony) b(niebieski) s(symbol) l(LED) e(koniec): ").lower()
    if "r" in text:
        isRed = True
    if "b" in text:
        isBlue = True
    if "s" in text:
        hasSymbol = True
    if "l" in text:
        isLedOn = True
    if "e" in text:
        break

    if isRed and isBlue and hasSymbol and isLedOn:
        cut = False

    elif isRed and isBlue and hasSymbol and not isLedOn:
        cut = hasParallelPort

    elif isRed and isBlue and not hasSymbol and isLedOn:
        cut = isLastSerialNumberDigitEven

    elif isRed and isBlue and not hasSymbol and not isLedOn:
        cut = False

    elif isRed and not isBlue and hasSymbol and isLedOn:
        cut = moreThanTwoBatteries

    elif isRed and not isBlue and hasSymbol and not isLedOn:
        cut = True

    elif isRed and not isBlue and not hasSymbol and isLedOn:
        cut = moreThanTwoBatteries

    elif isRed and not isBlue and not hasSymbol and not isLedOn:
        cut = isLastSerialNumberDigitEven

    elif not isRed and isBlue and hasSymbol and isLedOn:
        cut = hasParallelPort

    elif not isRed and isBlue and hasSymbol and not isLedOn:
        cut = False

    elif not isRed and isBlue and not hasSymbol and isLedOn:
        cut = hasParallelPort

    elif not isRed and isBlue and not hasSymbol and not isLedOn:
        cut = isLastSerialNumberDigitEven

    elif not isRed and not isBlue and hasSymbol and isLedOn:
        cut = moreThanTwoBatteries

    elif not isRed and not isBlue and hasSymbol and not isLedOn:
        cut = True

    elif not isRed and not isBlue and not hasSymbol and isLedOn:
        cut = False

    elif not isRed and not isBlue and not hasSymbol and not isLedOn:
        cut = True

    if cut:
        print("Cut")
    else:
        print("Don't cut")
