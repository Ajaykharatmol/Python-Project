class library:
   def __init__(self,bookname,booknumber,name,id,isd,rt):
        self.bookname=bookname
        self.booknumber=booknumber
        self.name=name
        self.id=id
        self.isd=isd
        self.rt=rt
   
   def addBookDatails():
      bookname=input("Enter the bookname ")
      booknumber =input("Enter the booknumber ")

      f=open("books.text","a")
      f.write(bookname+"\n")
      f.write(str(booknumber)+"\n")
      f.close()
        
   def showBookDatails():
       with open("books.text","r") as f:
            for line in f:
                print(line)

   def issueBook():
      bookname=input("Enter the bookname you want to issue")
      booknumber =input("Enter the booknumber you want to issue ")

     
      
      with open("books.text","r") as f:
                  for line in f:
                            n = line.strip()
                            no = f.readline().strip()
                            
                            if(bookname==n or booknumber==no):
                                      s=input("Enter student name:")
                                      id=input("Enter student id:")
                                      isd=input("Enter date you want issue:")
                                      red=input("Enter date you want return:")
                   
      f=open("issuebooks.txt","a")
      f.write(bookname+"\n")
      f.write(str(booknumber)+"\n")
      f.write(s+"\n")
      f.write(id+"\n")
      f.write(isd+"\n")
      f.write(red+"\n")
      f.close()
      

   def returnBook():
      bookname=input("Enter bookname you want to return")
      my_d={}
      with open("issuebooks.txt","r") as f:
                  for line in f:
                            n = line.strip()
                            no = f.readline().strip()
                            s=f.readline().strip()
                            id=f.readline().strip()
                            isd=f.readline().strip()
                            red=f.readline().strip()
                            if(bookname!=n):
                                  my_d[no]=library(n,no,s,id,isd,red)
                                      
                   
      f=open("issuebooks.txt","w")
      for i in my_d:
         f.write(my_d[i].bookname+"\n")
         f.write(my_d[i].booknumber+"\n")
         f.write(my_d[i].s+"\n")
         f.write(my_d[i].id+"\n")
         f.write(my_d[i].isd+"\n")
         f.write(my_d[i].red+"\n")
      f.close()

def main():
    choice = 1
    while(choice!=5):
        print("\t\t1.acceptBookDatails")
        print("\t\t2.showBookDatails")
        print("\t\t3.issueBook")
        print("\t\t4.returnBook")
        print("\t\t5.Exit")

        choice= input("Enter your choice:")
        if(choice=="1"):
            print("---addBookDatails-----")
            library.addBookDatails()
        elif(choice=="2"):
            print("----showBookDatails----")
            library.showBookDatails()
        elif(choice=="3"):
            print("----issueBook----")
            library.issueBook()
        elif(choice=="4"):
           print("----returnBook----")
           library.returnBook()
        elif(choice=="5"):
            break
        else:
            print("Invalid choice")

        
if __name__=="__main__":
   main()
















        
    
    
