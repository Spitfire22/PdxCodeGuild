#string = "abcdefghijklmnopqrstuvwxyz"

#start = string.find("a") + 1
#end = start + enco

#if end > 26:
#    end = end - 26

#string[end - 1]

### Below is what I made - Above is a start on the lab was supposed to be created.
### Loop back on the string so you're not going outside of it.

enco = int(input("How much rotation on your incoding do you want? "))

def rot13(rotate):
    result = ""

    for input in rotate:
        conv = ord(input)

        if conv >= ord('a') and conv <= ord('z'):
            if conv > ord('m'):
                conv -= enco
            else:
                conv += enco
            result += chr(conv)

## Tried to include caps - but it goes all funk(y)

        if conv >= ord('A') and conv <= ord('Z'):
            if conv > ord('M'):
                conv -= enco
            else:
                conv += enco
            result += chr(conv)

    return result

wordquery = input("What word do you want to encode? ")


print(rot13(wordquery))






