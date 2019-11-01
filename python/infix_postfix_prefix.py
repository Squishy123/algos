def op(sym):
    if(sym == '^'):
        return 3
    elif(sym == '*' or sym == '/'):
        return 2
    elif(sym == '+' or sym == '-'):
        return 1
    return 0

def in_to_post(self, equation):
    operators=[]
    nums=[]
    post=[]
    equation=list(equation.split(' '))

    for e in equation:
        if e in ['^', '*', '/', '+', '-']:
            while(len(operators) > 0):
                popped=operators.pop()
                if(op(e) < op(popped)):
                    break
                else:
                    post.append(popped)        

            #if current op is lower in priority - take the higher operator
            if(len(operators) > 0 and op(e) < op(operators[:-1])):
                post.append(operators.pop())   
        else:
            post.append(e)
        
    while(len(operators) > 0):
        popped=operators.pop()
        post.append(popped)
