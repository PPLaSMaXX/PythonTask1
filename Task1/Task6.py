input1 = "01010101"
input2 = "00011100011"
input3 = "000111001011"
input4 = "000111010011"

def PoslidovnaPoslidovnist(input):

    print(input)

    series_zero = [0 for x in range(len(input))]
    series_one = [0 for x in range(len(input))]

    is_success = False
    series_state = 0
    series_one_break = 0
    series_zero_break = 0

    for n in input:

        if n == '0':
            if series_state == 1:
                series_one_break += 1
            series_state = 0
            series_zero[series_zero_break] += 1


        elif n == '1':
            if series_state == 0:
                series_zero_break += 1
            series_state = 1
            series_one[series_one_break] += 1

        if series_zero == series_one:
            is_success = True
        else:
            is_success = False

    #print(series_zero)
    #print(series_one)
    return is_success


print(PoslidovnaPoslidovnist(input1))
print(PoslidovnaPoslidovnist(input2))
print(PoslidovnaPoslidovnist(input3))
print(PoslidovnaPoslidovnist(input4))
