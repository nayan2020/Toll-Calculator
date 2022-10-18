# Context
 A new road has been built and is now open for general traffic. The road construction company needs your help in calculating the money collection via toll from travellers. 
 
# FASTAG
  The construction company prefers money to be collected via FASTAG. FASTAG is an electronic payment utility that can be used to pay tolls.  All vehicles have a vehicle number. The FASTAG is associated with a vehicle number.
  If there is no sufficient balance in the FASTAG, then the remaining cost of the toll needs to be paid by cash. If travellers do not have a FASTAG they can make the payment by Cash. There is a flat fee of 40 for such cash transactions.
  
# Toll charges
 Amount of toll collected varies based on the weight of the vehicle.
 
![toll_geek](https://user-images.githubusercontent.com/59414392/196355017-ab75cb75-f4e4-4610-ab2e-c8179241d194.png)

# Journey Type
 Toll charges are different for a single trip and for a return journey. When a vehicle does a return journey, there is a discount of 50% for the return journey.
For eg: If a Van passes through the toll first time, the toll collected is 100. If the same Van passes again through the toll, the amount collected for the return journey is 50. If the Van passes a third time, it will be treated as a new single journey and the toll collected is 100. 

# Goal
 Your task is to build a solution that calculates various tolls collected and print the payment summary and vehicle type summary.
 
 * The payment summary should give a breakup of the total amount collected and the total discount given. 
 * The vehicle type summary should display the total number of vehicles passed per type in descending order of the collection amount.
 
# Assumptions
 * All vehicles passing through has a vehicle number. 
 * Some vehicles may not have FASTAG, in that case the toll amount is paid by cash. 
 * Some vehicles that have FASTAG may not have sufficient money to pay the toll, then the remaining amount is paid by cash. 
 * Tolls are always collected from FASTAG first, then only cash is taken if needed. 
 * Every cash transaction has a flat fee of 40. 
 * Cash amount collected includes the toll charges paid and the flat fee of 40. 
 * The vehicle count is calculated based on journeys. eg: if the same car passes twice, the count is 2.

# Pre-requisites
* Python 3.8/3.9

# How to run the code

We have provided scripts to execute the code. The filename which has the main method should be named as `geektrust.py` and should not be renamed to anything else.

Use `run.sh` if you are Linux/Unix/macOS Operating systems and `run.bat` if you are on Windows. Both the files run the commands silently and prints only output from the input files in the directory `smaple_input`

Internally both the scripts run the following commands 

* `python -m geektrust sample_input/input1.txt` - This will run the solution passing in the sample input file `input1.txt` as the command line argument.
* `python -m geektrust sample_input/input2.txt` - This will run the solution passing in the sample input file `input2.txt` as the command line argument.
* `python -m geektrust sample_input/input3.txt` - This will run the solution passing in the sample input file `input3.txt` as the command line argument.
* `python -m geektrust sample_input/input4.txt` - This will run the solution passing in the sample input file `input4.txt` as the command line argument.
* `python -m geektrust sample_input/input5.txt` - This will run the solution passing in the sample input file `input5.txt` as the command line argument.

 We expect your program to take the location to the text file as parameter. Input needs to be read from a text file, and output should be printed to the console. The text file will contain only commands in the format prescribed by the respective problem. We have added the code snippet to help you read from the file passed as command line argument. 

 # Running the code for multiple test cases

Run `run.sh` or `run.bat` in your local machine to ensure your solution is working correctly. Once confirmed please uplaod it in Geektrust and check for the test cases.

