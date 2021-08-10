def evens_between_two(m:int,n:int):
    if m<n:
        ls = list(range(m,n+1))
        ls = list(filter(lambda x: x if x%2==0 else False,ls))
        print(ls)
    else:
        print("first entry must be smaller than the second number")
        response = input("Do you want to flip the inputs? Y/N: ").strip().lower()[0]
        if response == "y":
            evens_between_two(n,m)
        else:
            print("Please enter inputs again: ")
            while True:
                try:
                    m = int(input("Enter fist number: ").strip())
                    n = int(input("Enter Second number: ").strip())
                    evens_between_two(m,n)
                    break
                except Exception:
                    print("Value Error occurred please enter again")

def change_cases():
    st = input("Enter the string text with more than 4 characters: ")
    while len(st) < 4:
        st = input("Enter string more than 4 characters: ")
    st_toggle_case = st.swapcase()
    print(" Process 1 ".center(100,"*"))
    print(f"{st_toggle_case}")
    print(" Process 2 ".center(100,"*"))
    ls = list()
    for i in range(0,len(st)):
        if st[i].islower():
             ls.append(st[i].upper())
        elif st[i].isupper():
            ls.append(st[i].lower())
        else:
            ls.append(st[i])

    print("".join(ls))

def print_pattern(text:str):
    import random
    RED  = '\033[31m'
    GREEN  = '\033[32m'
    BLUE  = '\033[34m'
    ORANGE  = '\033[33m'
    PURPLE  = '\033[35m'
    my_color = [ORANGE, RED, GREEN, ORANGE, BLUE, PURPLE]
    if len(text)>2:
        text = text.upper().replace(" ","")
        for i in range(1,len(text)+1):
            a = " ".join(text[:i])
            new_text = ""
            for x in a:
                new_text += x + random.choice(my_color)
            print(new_text)

    else:
        text = input("enter text with more than two characters: ").strip()
        print_pattern(text)

def fibonacci(n:int):
    a = 0
    b = 1

    if n in (0,1):
        return 0
    else:
        ls = [a,b]
        for i in range(2,n+1):
            c = a+b
            a,b = b,c
            ls.append(c)
        return ls
def no_list():
    min_val=max_val=None
    summation = 0
    count = 1
    while True:
        while True:
            try:
                n = int(input("Enter number not 0 and -ve to exit ").strip())
                if n == 0:
                    raise Exception
                break
            except Exception:
                print("Value Error occurred")
        if n < 0 and count>1:
            return({"min":min_val,"max":max_val,"sum":summation,"avg":round(summation/(count-1),4) })
        if count == 1:
            min_val=max_val=n
        else:
            if n < min_val:
                min_val = n
            if n > max_val:
                max_val = n
        summation += n
        count += 1
print("Choose an option to execute \n 1. Program to print even numbers between m and n \n 2. Write a string and swap cases \n 3. Enter string to display pattern \n 4. Enter number of fibonacci numbers to be displayed \n 5. Calculate until negative number is entered\n")
resp = input("Enter program number to execute or type quit to exit :").strip()
if resp == '1':
    while True:
        try:
            m = int(input("Enter fist number: ").strip())
            n = int(input("Enter Second number: ").strip())
            evens_between_two(m,n)
            break
        except Exception:
            print("Value Error occurred please enter again")
elif resp == '2':
    change_cases()
elif resp == '3':
    text = input("enter text with more than two characters: ").strip()
    print_pattern(text)
elif resp == '4':
    while True:
        try:
            fibo_num = int(input("Enter number of fibonacci number: ").strip())
            if fibo_num <0:
                raise Exception
            print(fibonacci(fibo_num))
            break
        except Exception:
            print("Value must be valid")
elif resp=='5':
    dc = no_list()
    for k,v in dc.items():
        print(f"{k:{5}}: {v}")
else:
    print("Thank You")
