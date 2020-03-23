def make_change(amount):
    change = {}
    a = amount
    change.update({"H" : (a//50)})
    a= a%50
    change.update({"Q" : (a//25)})
    a = a%25
    change.update({"D" : (a//10)})
    a = a%10
    change.update({"N" : (a//5)})
    a = a%5
    change.update({"P" : (a//1)})

    change = {k : v for k,v in change.items() if v>=1}

    return(change)
    


make_change(37)
 

make_change(430)
