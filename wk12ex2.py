class HotelRoom:
    def __init__(self, RoomNumber, RoomType, IsBooked):
        self.RoomNumber = RoomNumber
        self.RoomType = RoomType
        self.IsBooked = IsBooked
        
    def BookRoom(self):
        self.IsBooked = True
    
    def CancelBooking(self):
        self.IsBooked = False
    
    def DisplayStatus(self):
        if (self.IsBooked == False): 
            return "AVAILABLE"
        else:
            return "BOOKED"
        
room1 = HotelRoom("100", "Junior Suite", False)
room2 = HotelRoom("200", "Presidential Suite", False)

print(f"{room1.RoomType} , number: {room1.RoomNumber} is: {room1.DisplayStatus()}")
print(f"{room2.RoomType} , number: {room2.RoomNumber} is: {room1.DisplayStatus()}")

room1.BookRoom()
room2.BookRoom()

print(f"{room1.RoomType} , number: {room1.RoomNumber} has been BOOKED and now is: {room1.DisplayStatus()}")
print(f"{room2.RoomType} , number: {room2.RoomNumber} has been BOOKED and now is: {room1.DisplayStatus()}")

room1.CancelBooking()
room2.CancelBooking()

print(f"{room1.RoomType} , number: {room1.RoomNumber} has been CANCELLED and now is: {room1.DisplayStatus()}")
print(f"{room2.RoomType} , number: {room2.RoomNumber} has been CANCELLED and now is: {room1.DisplayStatus()}")