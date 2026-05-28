import math

p1=[0,0]
p2=[0,0]

def calcular_distancia(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    res=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    print(f"La distancia es {res}")
    return(res)

if __name__ == "__main__":
    p1=[float(i) for i in input("X1 X2: ").split()]
    p2=[float(i) for i in input("Y1 Y2: ").split()]
+   calcular_distancia(p1,p2)