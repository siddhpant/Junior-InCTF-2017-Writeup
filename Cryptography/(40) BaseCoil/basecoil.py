with open('cipher.txt') as f:
    data = f.read()

while True:
    try:
        data = data.decode('base64')
        print data
    except:
        break
