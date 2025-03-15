import calendar
import datetime
class SmartMeetingScheduler:
    def __init__(self, working_hours=(9, 17), holidays=None):
        self.working_hours = working_hours
        self.holidays = holidays if holidays else []
        self.schedule = {} 

    def is_working_day(self, date):
        if date.weekday() >= 5 or date in self.holidays:
            return False
        return True

    def initialize_user(self, user):
        if user not in self.schedule:
            self.schedule[user] = []

    def schedule_meeting(self, user, date, start_time, end_time):
        self.initialize_user(user)
        if not self.is_working_day(date):
            print("Error: Cannot schedule meetings on weekends or holidays.")
            return

        new_meeting = (start_time, end_time)
        for meeting in self.schedule[user]:
            if max(meeting[0], new_meeting[0]) < min(meeting[1], new_meeting[1]):
                print("Error: Overlapping meeting detected.")
                return

        self.schedule[user].append(new_meeting)
        print("Meeting scheduled successfully.")

    def check_available_slots(self, user, date):
        self.initialize_user(user)
        if not self.is_working_day(date):
            print("No available slots. It's a weekend or holiday.")
            return

        booked_slots = sorted(self.schedule[user])
        available_slots = []

        current_time = self.working_hours[0]
        for meeting in booked_slots:
            if current_time < meeting[0]:
                available_slots.append((current_time, meeting[0]))
            current_time = max(current_time, meeting[1])

        if current_time < self.working_hours[1]:
            available_slots.append((current_time, self.working_hours[1]))

        if available_slots:
            print("Available slots:")
            for slot in available_slots:
                print(f"{slot[0]}:00 - {slot[1]}:00")
        else:
            print("No available slots.")

    def view_meetings(self, user):
        self.initialize_user(user)
        if self.schedule[user]:
            print(f"Upcoming meetings for {user}:")
            for meeting in sorted(self.schedule[user]):
                print(f"{meeting[0]}:00 - {meeting[1]}:00")
        else:
            print("No upcoming meetings.")

scheduler = SmartMeetingScheduler(holidays=[datetime.date(2025, 3, 21)])
user = "Amruta"
date = datetime.date(2025, 3, 18)
scheduler.schedule_meeting(user, date, 10, 11)
scheduler.check_available_slots(user, date)
scheduler.view_meetings(user)
