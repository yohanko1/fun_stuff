import re
input_str = '1*2+3+4*5' 
num = re.compile(r'^[0-9]+$')
op = re.compile(r'^[*/+-]$')

# restart for-loop version
def process(tokens, op1, op2):
    restart = True
    while restart:
        restart = False
        for i, t in enumerate(tokens):
            if re.search(op, t) is not None:
                if t is op1 or t is op2:
                    tokens.insert(i, "("+t +" "+ tokens[i-1] +" "+ tokens[i+1]+")")
                    tokens.pop(i-1)
                    tokens.pop(i)
                    tokens.pop(i)
                    restart = True
                    break;
    return tokens

# while version
def process1(tokens, op1, op2):
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if re.search(op, t) is not None and t is op1 or t is op2:
            exp = "("+ t +" "+ tokens[i-1] +" "+ tokens[i+1]+")"
            tokens.insert(i, exp)
            tokens.pop(i-1)
            tokens.pop(i)
            tokens.pop(i)
            continue
        i += 1

    return tokens

def list2str(l):
    return str(l).strip('[]')

def main():
    tokens = re.split(r'(\D)', input_str)
    print tokens
    #process(process(tokens,'*', '/'), '+', '-')
    process1(process1(tokens,'*', '/'), '+', '-')
    print list2str(tokens)

if __name__ == "__main__":
    main()
