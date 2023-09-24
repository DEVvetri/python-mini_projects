file_name="helo.txt"
content="hi bro ena panura"
count=0
for i in file_name:
        while i==".":
            if file_name!="" and content!="":
                  file=open(f'{file_name}',"w")

                  file.write(content)
                  file.close()
                  break
            else:
                  print("poochu da samy")
                #   messagebox.showerror("error","conditions not accepted")
            count+=1