
import pathlib
import json
""" 
Cinema hall:

SCREEN


 123456789
1*........
2....*....
3*........
4*.....*..
5....*....
6*.......*
7*...****.
"""

class Cinema:
    MAIN_MENU=""" Select action:
    0-exit
    1-print hall
    2-sale ticket
    3-return ticket
    4-import hall
    """
    def __init__(self,rows,sits) -> None:
        self.sits=sits
        self.rows=rows
        self.hall=[1<<sits for n in range(rows)]
        # for n in range(rows):
        #     self.hall.append(1<<sits)
        print(self.hall)
        print(f'{1<<sits:b}')
        
        while True:
            match input(Cinema.MAIN_MENU):
                case '0':
                    self.save() 
                    break
                case '1':self.print_hall()
                case '2':self.sale_ticket()
                case '3':self.return_ticket()
                case '4':self.import_from_file()
                case _: print ('Incorrect selection')
        pass
    def import_from_file(self):
        with open(pathlib.Path(__file__).parent.joinpath('cinema_hall.json'),'w') as f:
            self.hall=json.load(f) 
            self.rows = len(self.hall)
            self.sits = len(f'{self.hall[0]:b}') - 1         
            pass
    def save(self):
        with open(pathlib.Path(__file__).parent.joinpath('cinema_hall.json'),'w') as f:
            json.dump(self.hall,f)
            pass
    def sale_ticket(self):
        self.print_hall()
        row,sit=self.menu()
        print(self.hall[row-1])
        print(sit)
        sit=self.sits-sit
        self.hall[row-1] = self.set_bit(self.hall[row-1],sit)        
        pass
    def return_ticket(self):
        self.print_hall()
        row,sit=self.menu()
        print(self.hall[row-1])
        print(sit)
        sit=self.sits-sit
        self.hall[row-1] = self.clear_bit(self.hall[row-1],sit)
        pass
    def print_hall(self):
        hall_to_print=''
        max_len_row=len(str(self.rows))+1
        hall_to_print+=max_len_row*' '
        for sit in range(1,self.sits+1):
            hall_to_print+= f'{sit}  '
            pass
        hall_to_print+='\n'
        
        for row, sit in enumerate(self.hall):
            row += 1
            hall_to_print+=f'{row}'
            len_row=len(str(row))
            hall_to_print+=(max_len_row-len_row)*' '
            sit=f'{sit:b}'[1:].replace('0','.').replace('1','*')
            
            for next_element in sit:
                hall_to_print += next_element + '  '
            #+ (len(str(sit))-1)*' '    
            pass
            hall_to_print+='\n'
        
        print(hall_to_print)
            
        pass
    def menu(self):
        while True:
            row=input('Enter row number: ')
            if not row.isdigit():
                print('Incorect enter! Try again!')
                continue
            row=int(row)
            if row not in range(1, self.sits+1):
                print('Value not in range! Try again!')
                continue
            break
        while True:
            sit=input('Enter sit number: ')
            if not sit.isdigit():
                print('Incorect enter! Try again!')
                continue
            sit=int(sit)
            if sit not in range(1, self.sits+1):
                print('Value not in range! Try again!')
                continue
            break
        return row, sit
        pass
    
    @staticmethod
    def set_bit(value,bit_number):return value|(1<<bit_number)
    @staticmethod
    def clear_bit(value,bit_number):return value&~(1<<bit_number)
    @staticmethod
    def get_bit(value,bit_number):return 1&(value>>bit_number)
    pass

