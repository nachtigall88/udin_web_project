from string import digits

ip = '230.1.1.1'
flag = True

if not all(map(lambda x: 0 <= int(x) <= 225, ip.split('.'))):
    flag = False

if __name__ == '__main__':
    print(flag)
    print([int(x) for x in ip.split('.')])
