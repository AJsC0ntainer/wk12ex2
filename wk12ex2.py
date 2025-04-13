#Class of type HotelRoom
class HotelRoom:
    #Constructor to create rooms
    def __init__(self, RoomNumber, RoomType, IsBooked):
        #Constructor properties
        self.RoomNumber = RoomNumber
        self.RoomType = RoomType
        self.IsBooked = IsBooked
    #Method to book a room
    def BookRoom(self):
        self.IsBooked = True
    #Method to cancel a room
    def CancelBooking(self):
        self.IsBooked = False
    #Method to display the status of a room
    def DisplayStatus(self):
        if (self.IsBooked == False): 
            return "AVAILABLE"
        else:
            return "BOOKED"
#Create object 1
room1 = HotelRoom("100", "Junior Suite", False)
#Create object 2
room2 = HotelRoom("200", "Presidential Suite", False)
#Display room objects information before booking
print(f"{room1.RoomType} , number: {room1.RoomNumber} is: {room1.DisplayStatus()}")
print(f"{room2.RoomType} , number: {room2.RoomNumber} is: {room1.DisplayStatus()}")
#Calls the booking method
room1.BookRoom()
room2.BookRoom()
#Display room objects information after booking
print(f"{room1.RoomType} , number: {room1.RoomNumber} has been BOOKED and now is: {room1.DisplayStatus()}")
print(f"{room2.RoomType} , number: {room2.RoomNumber} has been BOOKED and now is: {room1.DisplayStatus()}")
#Calls the method to cancel a room
room1.CancelBooking()
room2.CancelBooking()
#Displays room objects after cancelling a room
print(f"{room1.RoomType} , number: {room1.RoomNumber} has been CANCELLED and now is: {room1.DisplayStatus()}")
print(f"{room2.RoomType} , number: {room2.RoomNumber} has been CANCELLED and now is: {room1.DisplayStatus()}")

#Pushed to GitHub wk12ex2 Repo.