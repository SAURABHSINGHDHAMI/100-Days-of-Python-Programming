import requests

class IRCTC:
    def __init__(self):
        # User prompt for action selection
        user_input = input("""How would you like to proceed?
        1. Enter 1 to check live train station
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule""")
        
        if user_input == "1":
            print("live train status")
        elif user_input == "2":
            print("PNR")
        else:
            self.train_schedule()     
    
    def train_schedule(self):
        # User input for train number
        train_no = input("Enter the train no: ")
        self.fetch_data(train_no)
        
    def fetch_data(self, train_no):
        # API request to fetch train schedule data
        data = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/30c382602bfa67c8a7c580e6cfe2becb/TrainNumber/{}".format(train_no))
        
        data = data.json()
        
        # Displaying the train route details
        print(data['Route'])
        
        for i in data['Route']:
            # Printing station details
            print(i['StationName'], "|", i["ArrivalTime"], "|", i["DepartureTime"], "|", i["Distance"], "kms")
        
# Creating an instance of the IRCTC class to run the code
obj = IRCTC()
