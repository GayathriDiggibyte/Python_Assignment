from src.Assignment3.util import mutation
def main():
    s=input("Enter a string : ")
    pos=int(input("Enter the position to change the string at : "))
    var_to_add=input("Enter a string to add : ")
    mutedstring=mutation(s,pos,var_to_add)
    print("The mutated string : ",mutedstring)

main()
