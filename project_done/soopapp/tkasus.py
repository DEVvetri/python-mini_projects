def fun1():
    count=0
    for i in range(1,6,1): 
            if i==1:
                for j in range(1,6):
                    print("#",end="")
                    
                count+=1
                print()
            elif i==2:
                for j in range(1,6-1):
                    print("#",end="")
                    
                count+=1
                print()
            elif i==3:
                for j in range(1,6-2):
                    print("#",end="")
                    
                count+=1
                print()
            elif i==4:
                for j in range(1,6-3):
                    print("#",end="")
                    
                count+=1
                print()
            elif i==5:
                for j in range(1,6-4):
                    print("#",end="")
                    
                count+=1
                print()
    if count==5:
        print("porgram ended")

def fun2():
    file_hand0=open("AR Gamer.jpeg","+br")
    file_hand1=open("Artworks in GTA IV.jpeg","+br")
    con_1=file_hand0.read()
    con_2=file_hand1.read()
    if con_1!=con_2:
        print("given images are not same")
    else:
        file=open("newimg.jpeg","+bw")

def fun3():
    file_hand0=open("AR Gamer.jpeg","+br")
    file_hand1=open("AR Gamer.jpeg","+br")
    file_hand2=open("Artworks in GTA IV.jpeg","+br")
    con_1=file_hand0.read()
    con_2=file_hand1.read()
    con_3=file_hand2.read()
    if con_1==con_2:
        file=open("newimg.jpeg","+bw")
        file.write(con_3)
        file.close()
    else:
        print("not same image")
    file_hand0.close()
    file_hand1.close()
    file_hand2.close()

# fun1()
print("next fun")
fun2()
print("next fun")

