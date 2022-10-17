import argparse
from order_processor import OrderProcessor

# Global OrderProcessor object used by interactive and processFile methods
proc = OrderProcessor()

# Main
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False)
    args = parser.parse_args()
    if not args.file:
        interactive()
    else:
        processFile(args.file)

    return None
    
# Function that implements the "interactive" feature of this ordering system which takes orders from 
#   standard input and outputs the result to standard output until the input is 'q' or the program is 
#   forcefully stopped
def interactive():
    print("Welcome to the Evive Engineering Test interactive ordering system! Enter 'q' or ctrl+c to exit.")
    while(True):
        order = input("Order: ")
        if order == 'q':
            print("Pleasure doing business with you.")
            break
        print(proc.process(order))

# Function that goes through orders in the specified .txt file and outputs the result to standard output
def processFile(filepath):
    try:
        with open(filepath, 'r') as f:
            for line in f.read().splitlines():
                print(proc.process(line))
    except Exception as e:
        print(e)

# Sentinel
if __name__ == '__main__':
    main()