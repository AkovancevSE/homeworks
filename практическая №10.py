with open('C:\Users\Станислав\Desktop\Акованцев станислав_у-233-vvod.txt', 'r') as first_file:
    data = first_file.read()
with open('C:\Users\Станислав\Desktop\Акованцев станислав_у-233-vivod.txt', 'w') as second_file:
    second_file.write(data)