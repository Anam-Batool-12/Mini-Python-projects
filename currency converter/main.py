with open('currency.txt') as f:
    data = f.readlines()
    print(data)
    for line in data:
      parsed = 