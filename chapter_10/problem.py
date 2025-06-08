import random

class BookTicket:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        print(f"🚆 Train number: {self.trainNo}")

    def book(self):
        print(f"✅ Booked ticket for train no: {self.trainNo}")

    def destination(self, fo, to):
        # origin (fo) এবং destination (to) কে object এর মধ্যে save করছি
        self.fo = fo
        self.to = to
        print(f"📍 Train is going from {self.fo} to {self.to}")

    def bookTicket(self):
        ticket_number = random.randint(1111, 10000)
        print(f"🎟️ Ticket booked for train {self.trainNo} from {self.fo} to {self.to}. Ticket No: {ticket_number}")

# Object তৈরি
s1 = BookTicket(2345)
s1.book()
s1.destination("Dhaka", "Rajshahi")
s1.bookTicket()
