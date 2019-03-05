# Week 2 quiz Written by Kevin z5168851 and Eric Martin for COMP9021
#See comments and test cases in stub.
#0.5 mark for passing all tests for describe_rule()
#1 mark for passing all tests for draw_line()
#1 mark for passing all tests for uniquely_produced_by_rule()

def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}

def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for number in rule:
        print(f'After {number[0]} followed by {number[1]}, we draw {rule[number]}')
             
def draw_line(rule_nb, first, second, length):
     
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    
    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    rule = rule_encoded_by(rule_nb)
    result =[first,second]
    if length == 0:
        print ()
    elif length <=2:
        result = result[:length]
    else:
        for num in range(length-2):
            tem = (result[-2],result[-1])
            result.append(rule[tem])
    result2 =[]
    print("".join([str(i) for i in result]))
    
    

def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    rule = {(0,0):-1,(0,1):-1,(1,0):-1,(1,1):-1}
    for i in range(len(line)-2):
        tem = (int(line[i]),int(line[i+1]))
        rule[tem] = int(line[i+2])
    result_s = ""
    for value in rule.values():
        if value>=0:
            result_s = result_s + str(value)
        else:
            return(-1)
    result_10 = int(result_s,2)
    
    if result_10>15 or result_10<0:
        return(-1)
    else:
        return(result_10)
