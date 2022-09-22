import InsectClass as I

def main():

    housefly = I.Insect(2,4) 
        #assigning the value of the attribute

    mosquito = I.Insect(6,8)
   
    housefly.flight_length()

    mosquito.flight_length()

    print('the house fly can fly up to', housefly.get_flight(), 'miles')
    print('the mosquito can fly up to', mosquito.get_flight(), 'miles')

main()