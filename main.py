"""
todo
improve user intraction
error handling
store index value for next player
"""
import pickle, os

def defaultvars():
    global A,B,C,P,Q,R,X,Y,Z
    A=[["a11","a12","a13"],["a21","a22","a23"],["a31","a32","a33"]]
    B=[["b11","b12","b13"],["b21","b22","b23"],["b31","b32","b33"]]
    C=[["c11","c12","c13"],["c21","c22","c23"],["c31","c32","c33"]]
    """test values
    A=[[1,"a12","a13"],[1,"a22","a23"],[1,"a32","a33"]]
    B=[[1,"b12","b13"],[1,"b22","b23"],[1,"b32","b33"]]
    C=[[1,"c12","c13"],["c21","c22","c23"],["c31","c32","c33"]]
    """
    P=[["p11","p12","p13"],["p21","p22","p23"],["p31","p32","p33"]]
    Q=[["q11","q12","q13"],["q21","q22","q23"],["q31","q32","q33"]]
    R=[["r11","r12","r13"],["r21","r22","r23"],["r31","r32","r33"]]

    X=[["x11","x12","x13"],["x21","x22","x23"],["x31","x32","x33"]]
    Y=[["y11","y12","y13"],["y21","y22","y23"],["y31","y32","y33"]]
    Z=[["z11","z12","z13"],["z21","z22","z23"],["z31","z32","z33"]]

if os.path.exists("data.pickle"):
    with open("data.pickle", "rb") as f:
        A = pickle.load(f)
        B = pickle.load(f)
        C = pickle.load(f)
        P = pickle.load(f)
        Q = pickle.load(f)
        R = pickle.load(f)
        X = pickle.load(f)
        Y = pickle.load(f)
        Z = pickle.load(f)
else:
    defaultvars()

on = True

def display():
    print(f"{A[0]}\t{B[0]}\t{C[0]}")
    print(f"{A[1]}\t{B[1]}\t{C[1]}")
    print(f"{A[2]}\t{B[2]}\t{C[2]}\n")

    print(f"{P[0]}\t{Q[0]}\t{R[0]}")
    print(f"{P[1]}\t{Q[1]}\t{R[1]}")
    print(f"{P[2]}\t{Q[2]}\t{R[2]}\n")

    print(f"{X[0]}\t{Y[0]}\t{Z[0]}")
    print(f"{X[1]}\t{Y[1]}\t{Z[1]}")
    print(f"{X[2]}\t{Y[2]}\t{Z[2]}")

def check(L):
    for i in range(3):
        if L[i][0] == L[i][1] == L[i][2]:
            return L[i][0]
        elif L[0][i] == L[1][i] == L[2][i]:
            return L[0][i]
    if L[0][0] == L[1][1] == L[2][2]:
        return L[0][0]
    elif L[0][2] == L[1][1] == L[2][0]:
        return L[0][2]
    
def myr():
    global on
    L=[[check(A),check(B),check(C)],[check(P),check(Q),check(R)],[check(X),check(Y),check(Z)]]
    x = check(L)
    if x == 1 or x == 0:
        on = False
        print("Winner",x)

def sendone(a):
    b=a[0].upper()
    x=int(a[2])
    y=int(a[1])
    match b:
        case "A":
            A[y-1][x-1] = 1
        case "B":
            B[y-1][x-1] = 1
        case "C":
            C[y-1][x-1] = 1
        case "P":
            P[y-1][x-1] = 1
        case "Q":
            Q[y-1][x-1] = 1
        case "R":
            R[y-1][x-1] = 1
        case "X":
            X[y-1][x-1] = 1
        case "Y":
            Y[y-1][x-1] = 1
        case "Z":
            Z[y-1][x-1] = 1
        

def sendzero(a):
    b=a[0].upper()
    x=int(a[2])
    y=int(a[1])
    match b:
        case "A":
            A[y-1][x-1] = 0
        case "B":
            B[y-1][x-1] = 0
        case "C":
            C[y-1][x-1] = 0
        case "P":
            P[y-1][x-1] = 0
        case "Q":
            Q[y-1][x-1] = 0
        case "R":
            R[y-1][x-1] = 0
        case "X":
            X[y-1][x-1] = 0
        case "Y":
            Y[y-1][x-1] = 0
        case "Z":
            Z[y-1][x-1] = 0
        
def dump_data():
    with open("data.pickle", "wb") as f:
        pickle.dump(A, f)
        pickle.dump(B, f)
        pickle.dump(C, f)
        pickle.dump(P, f)
        pickle.dump(Q, f)
        pickle.dump(R, f)
        pickle.dump(X, f)
        pickle.dump(Y, f)
        pickle.dump(Z, f)
def findnextbox(x):
    if x=="11":
        return "A"
    elif x=="12":
        return "B"
    elif x=="13":
        return "C"
    elif x=="21":
        return "P"
    elif x=="22":
        return "Q"
    elif x=="23":
        return "R"
    elif x=="31":
        return "X"
    elif x=="32":
        return "Y"
    elif x=="33":
        return "Z"
    
def invalidbox(a):
    if a == 'A':
        if check(A) == 1 or check(A) == 0:
            return 1
    elif a == 'B':
        if check(B) == 1 or check(B) == 0:
            return 1
    elif a == 'C':
        if check(C) == 1 or check(C) == 0:
            return 1
    elif a == 'P':
        if check(P) == 1 or check(P) == 0:
            return 1
    elif a == 'Q':
        if check(Q) == 1 or check(Q) == 0:
            return 1
    elif a == 'R':
        if check(R) == 1 or check(R) == 0:
            return 1
    elif a == 'X':
        if check(X) == 1 or check(X) == 0:
            return 1
    elif a == 'Y':
        if check(Y) == 1 or check(Y) == 0:
            return 1
    elif a == 'Z':
        if check(Z) == 1 or check(Z) == 0:
            return 1
    else:
        return 0
    
    
def main():
    player_counter=2
    global next_box
    while on==True:
        if player_counter%2==0:
            #print("\033[2J\033[H", end="", flush=True)
            display()
            if player_counter==2:
                print("Start the game (1)")
                a=input("pick (1) :")
                if a == "newgame":
                    if os.path.exists("data.pickle"):
                        os.remove("data.pickle")
                    defaultvars()
                    main()
                player_counter+=1
                sendone(a)
                dump_data()
            else:    
                if invalidbox(next_box):
                    print("u can play wherever u want")
                    a=input("pick (1) :")
                    if a == "newgame":
                        if os.path.exists("data.pickle"):
                            os.remove("data.pickle")
                        defaultvars()
                        main()
                    if invalidbox(a[0].upper()):
                        print("u cannot play there")
                        player_counter+=2
                        continue
                    else:
                        player_counter+=1
                        sendone(a)
                        dump_data()
                else:
                    a=input("pick (1) :")
                    if a == "newgame":
                        os.remove("data.pickle")
                        #print("db cleared. restart the program to start new game")
                        #sys.exit(0)
                        main()
                    if a[0].upper() == next_box:
                        player_counter+=1
                        sendone(a)
                        dump_data()
                    else:
                        print(f"Invalid Box U have to play in {next_box} box")
                        player_counter+=2
                        continue
            myr()
            next_box=findnextbox(a[-2:])
        else:
            #print("\033[2J\033[H", end="", flush=True)
            display()
            if invalidbox(next_box):
                print("u can play wherever u want")
                a=input("pick (1) :")
                if a == "newgame":
                    if os.path.exists("data.pickle"):
                        os.remove("data.pickle")
                    defaultvars()
                    main()
                if invalidbox(a[0].upper()):
                    print("u cannot play there")
                    player_counter+=2
                    continue
                else:
                    player_counter+=1
                    sendzero(a)
                    dump_data()
            else:
                a=input("pick (0) :")
                if a == "newgame":
                    if os.path.exists("data.pickle"):
                        os.remove("data.pickle")
                    defaultvars()
                    main()
                if a[0].upper() == next_box:
                    player_counter+=1
                    sendzero(a)
                    dump_data()
                else:
                    print(f"Invalid Box U have to play in {next_box} box")
                    player_counter+=2
                    continue
            myr()
            next_box=findnextbox(a[-2:])
            print("next box",next_box)

main()