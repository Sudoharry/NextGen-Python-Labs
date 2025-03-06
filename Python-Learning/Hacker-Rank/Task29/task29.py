def wrapper(f):
    def fun(l):
        # Format and sort the numbers
        formatted_numbers = sorted(format_number(num) for num in l)
        print(*formatted_numbers, sep='\n')
    return fun
    
def format_number(number):
    # Extract the last 10 digits of the number
    number = number[-10:]
    # Format the number as +91 xxxxx xxxxx
    return f'+91 {number[:5]} {number[5:]}'

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


