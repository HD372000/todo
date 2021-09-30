import argparse
import sys
from datetime import date
import linecache

def todo(args):

    if args.x == 'add':
        f=open("todo.txt","a")
        if args.s == []:
            print("Error: Missing todo string. Nothing added!")
        
        for i in args.s:
            f.write(i)
            f.write("\n")
            print("Added todo: \"{}\"".format(i))
        f.close()

    elif args.x == 'ls':
        f=open("todo.txt","r")
        k=f.readlines()
        t=reversed(k)
        n=list(reversed(k))
        if n==[]:
            print("There are no pending todos!")
        for i,j in zip(t,range(len(n))):
            print("[{0}] {1}".format(len(n)-j,i.rstrip()))
        f.close()

    elif args.x == 'del':
        f= open("todo.txt", "r")
        lines = f.readlines()
        f.close()
        if args.s == []:
            print("Error: Missing NUMBER for deleting todo.")
        elif int(args.s[0])>len(lines):
            print("Error: todo #{0} does not exist. Nothing deleted.".format(args.s[0]))
        else:
            for i in args.s:
                del lines[int(i)-1]
                print("Deleted todo #{}".format(i))
            new_file = open("todo.txt", "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()
                
    elif args.x == 'done':
        f= open("todo.txt", "r")
        f1=open("done.txt","a")
        lines = f.readlines()
        if args.s==[] :
            print("Error: Missing NUMBER for marking todo as done.")
        elif int(args.s[0])>len(lines) :
            print("Error: todo #{0} does not exist.".format(args.s[0]))
        else:
            for i in args.s:
                l = linecache.getline("todo.txt", int(i))
                f1.write(l)
                print("Marked todo #{} as done.".format(i))
                del lines[int(i)-1]   
            new_file = open("todo.txt", "w+")
            for line in lines:
                new_file.write(line)
            new_file.close() 
            f1.close()
            f.close()
        
    elif args.x == 'report':
        f= open("todo.txt", "r")
        f1=open("done.txt","r")
        lines1 = f.readlines()
        lines2=f1.readlines()
        today = date.today()
        print("{0} Pending : {1} Completed : {2}".format(today.strftime("%d/%m/%Y"),len(lines1),len(lines2)))
        f1.close()
        f.close()

    elif args.x == 'help':
        use="Usage :-\n" \
            "$ ./todo add \"todo item\"   # Add a new todo \n" \
            "$ ./todo ls                # Show remaining todos\n" \
            "$ ./todo del NUMBER        # Delete a todo\n" \
            "$ ./todo done NUMBER       # Complete a todo\n" \
            "$ ./todo help              # Show usage\n" \
            "$ ./todo report            # Statistics\n"
        print(use)

    elif args.x == None:
        use="Usage :-\n" \
            "$ ./todo add \"todo item\"   # Add a new todo \n" \
            "$ ./todo ls                # Show remaining todos\n" \
            "$ ./todo del NUMBER        # Delete a todo\n" \
            "$ ./todo done NUMBER       # Complete a todo\n" \
            "$ ./todo help              # Show usage\n" \
            "$ ./todo report            # Statistics\n"
        print(use)


if __name__ == "__main__":
    
    parser=argparse.ArgumentParser()
    
    parser.add_argument('x', type=str, nargs="?")
    parser.add_argument('s', type=str, nargs='*')

    args=parser.parse_args()

    todo(args)

    
   
      
            



           

