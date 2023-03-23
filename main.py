def encode(userInput):
    encString = ''
    for i in userInput:
        num = int(i)+3
        if num >= 10:
            num -= 10
        encString += str(num)
    print('Your password has been encoded and stored!\n')
    return encString


def main():
    go = True
    encString = ''
    while go:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        option = input('Please enter an option: ')
        if option == '3':
            go = False
            break
        elif option == '1':
            userInput = input('Please enter your password to encode: ')
            encString = encode(userInput)
        # elif option == '2':
        #     if encString != '':
        #         decode(encString)
        else:
            print('Invalid input')


if __name__ == "__main__":
    main()