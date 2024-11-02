import random


def add(add_limt = 20):
    while True:
        d1 = random.randint(0, add_limt-1)
        d2 = random.randint(0, add_limt-1)

        stnmt = f"{str(d1)} + {str(d2)}"
        tot = eval(stnmt)

        if tot > add_limt:
            continue
        else:
            return [stnmt, tot]



def sub(sub_limt = 10):
    while True:
        d1 = random.randint(0, sub_limt-1)
        d2 = random.randint(0, sub_limt-1)

        stnmt = f"{str(d1)} - {str(d2)}"
        tot = eval(stnmt)

        if tot < 0:
            continue
        else:
            return [stnmt, tot]
        

def mult(mult_limt = 12, table_limt = 10):
    while True:
        d1 = random.randint(0, mult_limt)
        d2 = random.randint(0, mult_limt)

        stnmt = f"{str(d1)} x {str(d2)}"
        tot = eval(f"{str(d1)} * {str(d2)}")

        if tot > (mult_limt * table_limt):
            continue
        else:
            return [stnmt, tot]



def dvtn(dvtn_limt = 12):
    while True:
        d1 = random.randint(1, dvtn_limt)
        d2 = random.randint(1, dvtn_limt)

        if d1 < d2:
            continue
        else:
            stnmt = f"{str(d1)} \u00F7 {str(d2)}"
            caution, riminder = eval(f"{str(d1)} // {str(d2)}"), eval(f"{str(d1)} % {str(d2)}")

            return [stnmt, caution, riminder]


""" choice_fun = random.choice([add(), sub(), mult(), dvtn()])
print(choice_fun) 
 """