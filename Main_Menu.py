import csv 
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def insert():
    # file name and headers
    filename='Novels.csv'  
    headers=['Novel_name  ','Author  ','Genre','Rating','Note']

    #open the file and write the headers
    write_header = not os.path.exists(filename) or os.path.getsize(filename) == 0 #so that it won't type headers again
    with open('Novels.csv',mode='a', newline='') as file:
        writer= csv.writer(file)
        if write_header:
            writer.writerow(headers)
        print("Welcome to the library!")

        while True:
            #getting user input
            name=input("Enter the Novel's name: ")
            author=input("Enter the Author's name: ")
            genre=input("Entre genre (mystery/romance/fantasy/horror/self_help): ")
            rate=int(input("Enter your rating score(1-10): "))
            note=input("Have you read the book? (y/n): ")

            # write the row to csv
            writer.writerow([name,author,genre,rate,note])
            print("Row Added!")

            #ask if user wants to add more
            cont=input("Do you wanna add more(y/n): ").lower()
            if (cont=='n'):
                break

    print(f"\nData saved to file name {filename}")

def see():
    with open('Novels.csv',mode='r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)

def update():
    headers=['Novel_name','Author','Genre','Rating','Note']
    updated_row=[]
    with open('Novels.csv',mode='r') as file:
        reader=csv.reader(file)
        header=next(reader) #save headers separately
        for row in reader:
            updated_row.append(row)

    #ask user which record to update
    target=input("Enter the name of the Novel you want to update: ")
    for row in updated_row:
        if row[0].lower() == target.lower():
            print(f"The data for this novel is \nAuthor={row[1]},\nGenre={row[2]},\nRating={row[3]},\nNote={row[4]}")       
            print("1.Update Author")
            print("2.Update Genre")
            print("3.Update Rating")
            print("4.Update Note")
            choice=int(input("Enter what you want to change: "))
            if choice==1:
                a=input("Enter new Author: ")
                row[1]=a #works the same as the code below
                print("Record Updated!")
                break
            elif choice==2:
                row[2]=input("Enter new genre: ")
                print("Record updated!")
                break
            elif choice==3:
                row[3]=int(input("Enter new rating: "))
                print("Record updated!")        
                break
            elif choice==4:
                row[4]=input("Enter new note: ")
                print("Record updated!")
                break
            else:
                print("Something's wrong")
    
    with open('Novels.csv',mode='w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(headers) #
        writer.writerows(updated_row)
        print('Data as been uploaded!!!')

def all():
    df=pd.read_csv("Novels.csv")
    top_clean=df[df['Rating']>0] #so it will remove novels with 0 rating
    top=top_clean.sort_values(by='Rating',ascending=False)
    plt.figure(figsize=(10,6))
    # top.plot(x='Novel_name',y='Rating',kind='bar',color="#42f5ef",legend=False) for plotting via matplotlib
    sns.barplot(data=top,x='Novel_name',y='Rating',hue='Genre',palette='pastel') #to show diff genres
    plt.title("Novel Ratings")
    plt.xlabel("Novels")
    plt.ylabel("Rating")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("Novel_ratings.png",dpi=300,bbox_inches='tight') #to save the figure
    plt.show()

def top():
    df=pd.read_csv("Novels.csv")
    top_nov=df.sort_values(by='Rating',ascending=False).head(5)
    plt.figure(figsize=(10,6))
    sns.barplot(data=top_nov,x='Novel_name',y='Rating',hue='Genre',palette='pastel')
    plt.title("Top 5 Novels")
    plt.xlabel("Novels")
    plt.ylabel("Ratings")
    plt.xticks(rotation=45)
    plt.tight_layout() #to cut out extra blank spaces
    plt.savefig('Top 5 novels.png',dpi=300,bbox_inches='tight')
    plt.show()


def menu():
    while True:
        print("\n1. Enter book details")
        print("2. See all the books")
        print("3. Update a record")
        print("4. See Novel ratings")
        print("5. Top 5 Novels to read")
        print("6. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            insert()
        elif choice==2:
            see()
        elif choice==3:
            update()
        elif choice==4:
            all()           
        elif choice==5:
            top()
        elif choice==6:
            print("You have exited!!")
            break  
        else:
            print("Choose again")  

          

menu()
         
