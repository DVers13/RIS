from LL1 import dictionary
def ll1(word):
    n = 1
    word = word.split()
    word.append("end")
    stack = []

    for i in range(len(word)):
        
        symbol = word[i]
        print("symbol =", symbol)

        accept = 0
        error = 0
        end = 0

        while (not (accept) or not (error) or not (end)):
            print(n, " -> ")

            if (symbol == "end" and (symbol in dictionary[n][0]) and len(stack) == 0):
                end = 1

            if (symbol.isdigit()):
                symbol = "count"

            m = ", ) ( true false * / + - or and not end const def = < >".split()
            if i != len(word)-1 and (symbol not in m):
                symbol = ("def" if ((word[i+1] == '(')) else symbol)
            
            if (symbol not in m):
                symbol = ("perem")
            
            if ((symbol in dictionary[n][0]) and not (end)):

                # Return
                new_n = n
                if dictionary[n][2] == 1:
                    new_n = stack.pop()
                    print(n, "Берем из stack", new_n)
                    print("stack:", stack)
                else:
                    new_n = dictionary[n][1]

                # Statck
                if dictionary[n][3] ==    1:
                    print(n, "Записываем в stack", n+1)
                    stack.append(n+1)
                    print("stack:", stack)

                # Accept
                if dictionary[n][4] == 1:
                    accept = 1
                    print(n, "ACCEPT")
                    print("----------------------------\n")
                    n = new_n
                    break

                n = new_n

            elif end:
                break
            # Error
            elif dictionary[n][5] == 0:
                n += 1
            else: 
                error = 1
                break
        
        if error:
            print("!!!ERROR!!!")
            break

        if end:
            print("--------------------------------------------") 
            print("Слово принадлежит данному формальному языку.")
            break


if __name__=='__main__':
    ll1('d = def ( a )')
