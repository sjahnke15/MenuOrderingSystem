
# MenuOrderingSystem
For Evive's engineering test. This application provides two ways to input orders:
- Interactive:
	- The interactive mode is the default way to use this application. While running, you can type the order, and it will output the result then ask for more orders. To stop this, you can either input 'q', or use 'ctrl-c' to exit.
- File
	- You can also input a .txt file with orders separated by lines. An example text file is included in this repository to reference the formatting.

### Repo Structure
**menu.json**: This json file is the 'menu' for this restaurant. Using json, it would be very easy to add/delete items or meals and it is very easy to import into a python script.

**test_orders.txt**: The example text input file that can be used to input orders rather than manually typing them into standard input.

**order_processor.py**: This file contains the class OrderProcessor used to process orders as they come in by outputting error strings or meal strings using the process() method. I developed this class assuming the specified menu would not be static.

**ordering.py**: This file implements the main function, and parses the command line input to determine whether the user wants interactive mode or file mode.

**tests.py**: This file uses the unittest framework to do some unit testing on methods within the OrderProcessor class. I made sure that the application stuck to the specified requirements, and could adapt to changes in the menu
## Requirements
This application requires Python 3. All libraries used are included in the Python standard library, which doesn't require any additional package installs.

 *OPTIONAL:* I would recommend to use a virtual environment. I use Python3's venv, but any other virtual environment tool would suffice. To create a virtual environment with venv, make sure you are in this repo's root directory then use the command:
 
 `python -m venv venv`
 
 You should see a folder named "venv" in this directory now. To activate the virtual environment:
 
 For Windows: `.\venv\Scripts\activate`
 For Linux: `source venv/bin/activate`
## Usage
To run interactive mode, simply run the application with no command line input

`python ordering.py`

To run using a text file, add the `--file {filepath}` option, where filepath is the path to the .txt file containing the order(s).

`python ordering.py --file {filepath}`

To run the tests located in test.py:

`python tests.py`
