import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# User Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Event Class
class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.attendees = []  # List to store registered users

    def register_user(self, user):
        self.attendees.append(user)
        return f"{user.username} registered for {self.name}."

# Notification Class
class Notification:
    def send_reminder(self, user, event):
        return f"Reminder sent to {user.username} for event: {event.name}."

class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XYZ Non-Profit Event Manager")
        
        # Creating events dictionary
        self.events = {
            "Fundraiser Gala": Event("Fundraiser Gala", "2025-05-10", "Community Center"),
            "Volunteer Meetup": Event("Volunteer Meetup", "2025-06-15", "Local Park"),
            "Awareness Drive": Event("Awareness Drive", "2025-07-20", "City Hall")
        }
        
        # Creating UI Components
        tk.Label(root, text="Enter Your Name:").grid(row=0, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Enter Your Email:").grid(row=1, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1)

        tk.Label(root, text="Select Event:").grid(row=2, column=0)
        self.event_var = tk.StringVar(root)
        self.event_var.set("Fundraiser Gala")
        tk.OptionMenu(root, self.event_var, *self.events.keys()).grid(row=2, column=1)
        
        tk.Button(root, text="Register", command=self.register_event).grid(row=3, column=0, columnspan=2)

    def register_event(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        event_name = self.event_var.get()
        
        if username and email:
            user = User(username, email)
            event = self.events[event_name]
            messagebox.showinfo("Registration", event.register_user(user))
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")

# Run the GUI
root = tk.Tk()
app = EventApp(root)
root.mainloop()
