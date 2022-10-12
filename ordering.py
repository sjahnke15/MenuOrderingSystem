import argparse

def main():
    interactive()
    #TODO - Use argparse to check if a --file option is present.
        # If it is, use the specified file and process orders line by line
        # Else, use the interactive ordering system in interactive()
    return None
    
def interactive():
    print("Welcome to the Evive Engineering Test interactive ordering system! Enter 'q' or ctrl+c to exit.")
    while(True):
        order = input("Order: ")
        if order == 'q':
            print("Pleasure doing business with you.")
            break
        #TODO - Process order using menu.json
        print("Order Received!")

if __name__ == '__main__':
    main()