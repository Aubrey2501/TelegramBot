input_file = open('numbers.txt', 'r')
data = input_file.read().split()
sum_num = sum(int(i) for i in data)
outp_file = open('answer.txt', 'w')
outp_file.write(str(sum_num))
input_file.close()
outp_file.close()

# �����!
