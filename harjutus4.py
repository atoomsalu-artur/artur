import turtle

try:
    r= float(input("ringi raadius r="))
    s= 3.14 * r
    p = 2 * 3.14 * r
    print(f"Ringi pindala on {s:0.2f} ja ümbermõõt on {p:.2}")
    turtle.circle(r)
except:
    print("Kontrolli sisestust!")
    

turtle.done()












