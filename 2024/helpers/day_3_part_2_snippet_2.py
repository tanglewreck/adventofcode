# coding: utf-8
k = 0
data = "xyxmul(123,456)xyzmuöl(38),.mul(1,2)mul(3,3333)sjsjX"
valid = True
eof = False
while valid and not eof:
    try:
        l = 4
        if k + l > len(data):
            eof = True
            continue
        token = get_token(data, k, l)
        #print(k, l, token)
        if not token == "mul(":
            k += 1
            continue
        l += 1
        while get_token(data, k, l)[-1] in digits:
            token = get_token(data, k, l)
            l += 1
        if get_token(data, k, l)[-1] == ",":
            token = get_token(data, k, l)
            l += 1
            while get_token(data, k, l)[-1] in digits:
                token = get_token(data, k, l)
                l += 1
            if get_token(data, k, l)[-1] == ")":
                token = get_token(data, k, l)
                l += 1
                print(token)
        k += len(token)
    except IndexError:
        pass
