def prob_a_and_b(a,b, total):
    prob_a=orange/total

    prob_bga=blue/(total-1)

    prob_aandb=prob_a*prob_bga
    return round(prob_aandb,3)

orange=int(input("Enter number of orage balls:"))
blue=int(input("enter number of blue balls:"))
total=orange+blue

print(prob_a_and_b(orange,blue, total))