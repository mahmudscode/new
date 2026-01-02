# TravelWiz – Python + Tkinter Version (Simplified GUI Rewrite)
# Converted from the given C++ console project

import tkinter as tk
from tkinter import messagebox

# ---------------- Data Models -----------------
class User:
    def __init__(self, email, password, fname, lname, phone, address, uid):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.address = address
        self.uid = uid
        self.bookings = []

class Booking:
    def __init__(self, place, hotel, transport, date, members, cost):
        self.place = place
        self.hotel = hotel
        self.transport = transport
        self.date = date
        self.members = members
        self.cost = cost

# ---------------- App -----------------
class TravelWizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TravelWiz")
        self.root.geometry("600x500")

        self.users = []
        self.current_user = None
        self.uid_counter = 1

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.login_screen()

    # ---------- Utilities ----------
    def clear(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ---------- Login / Register ----------
    def login_screen(self):
        self.clear()

        tk.Label(self.main_frame, text="TravelWiz", font=("Arial", 22, "bold")).pack(pady=20)

        tk.Label(self.main_frame, text="Email").pack()
        email_entry = tk.Entry(self.main_frame)
        email_entry.pack()

        tk.Label(self.main_frame, text="Password").pack()
        pass_entry = tk.Entry(self.main_frame, show="*")
        pass_entry.pack()

        def login():
            for u in self.users:
                if u.email == email_entry.get() and u.password == pass_entry.get():
                    self.current_user = u
                    self.home_screen()
                    return
            messagebox.showerror("Error", "Invalid login")

        tk.Button(self.main_frame, text="Login", command=login).pack(pady=10)
        tk.Button(self.main_frame, text="Register", command=self.register_screen).pack()

    def register_screen(self):
        self.clear()

        tk.Label(self.main_frame, text="Register", font=("Arial", 20)).pack(pady=10)

        entries = {}
        for field in ["First Name", "Last Name", "Phone", "Address", "Email", "Password"]:
            tk.Label(self.main_frame, text=field).pack()
            e = tk.Entry(self.main_frame)
            e.pack()
            entries[field] = e

        def register():
            user = User(
                entries["Email"].get(),
                entries["Password"].get(),
                entries["First Name"].get(),
                entries["Last Name"].get(),
                entries["Phone"].get(),
                entries["Address"].get(),
                self.uid_counter
            )
            self.uid_counter += 1
            self.users.append(user)
            messagebox.showinfo("Success", "Account created")
            self.login_screen()

        tk.Button(self.main_frame, text="Create Account", command=register).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.login_screen).pack()

    # ---------- Home ----------
    def home_screen(self):
        self.clear()

        tk.Label(self.main_frame, text=f"Welcome {self.current_user.fname}", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.main_frame, text="Search Tour", width=20, command=self.search_screen).pack(pady=5)
        tk.Button(self.main_frame, text="Profile", width=20, command=self.profile_screen).pack(pady=5)
        tk.Button(self.main_frame, text="My Bookings", width=20, command=self.booking_screen).pack(pady=5)
        tk.Button(self.main_frame, text="Logout", width=20, command=self.logout).pack(pady=5)

    # ---------- Search ----------
    def search_screen(self):
        self.clear()

        tk.Label(self.main_frame, text="Search Destination", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Place").pack()
        place_entry = tk.Entry(self.main_frame)
        place_entry.pack()

        tk.Label(self.main_frame, text="Hotel").pack()
        hotel_entry = tk.Entry(self.main_frame)
        hotel_entry.pack()

        tk.Label(self.main_frame, text="Transport").pack()
        transport_entry = tk.Entry(self.main_frame)
        transport_entry.pack()

        tk.Label(self.main_frame, text="Date").pack()
        date_entry = tk.Entry(self.main_frame)
        date_entry.pack()

        tk.Label(self.main_frame, text="Members").pack()
        members_entry = tk.Entry(self.main_frame)
        members_entry.pack()

        def book():
            members = int(members_entry.get())
            cost = (len(hotel_entry.get()) + len(transport_entry.get())) * 500 * members
            booking = Booking(
                place_entry.get(),
                hotel_entry.get(),
                transport_entry.get(),
                date_entry.get(),
                members,
                cost
            )
            self.current_user.bookings.append(booking)
            messagebox.showinfo("Booked", f"Tour booked! Cost: {cost} Tk")
            self.home_screen()

        tk.Button(self.main_frame, text="Confirm Booking", command=book).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.home_screen).pack()

    # ---------- Profile ----------
    def profile_screen(self):
        self.clear()
        u = self.current_user

        tk.Label(self.main_frame, text="Profile", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text=f"Name: {u.fname} {u.lname}").pack()
        tk.Label(self.main_frame, text=f"Email: {u.email}").pack()
        tk.Label(self.main_frame, text=f"Phone: {u.phone}").pack()
        tk.Label(self.main_frame, text=f"Address: {u.address}").pack()

        tk.Button(self.main_frame, text="Back", command=self.home_screen).pack(pady=10)

    # ---------- Bookings ----------
    def booking_screen(self):
        self.clear()

        tk.Label(self.main_frame, text="My Bookings", font=("Arial", 16)).pack(pady=10)

        if not self.current_user.bookings:
            tk.Label(self.main_frame, text="No bookings yet").pack()
        else:
            for b in self.current_user.bookings:
                tk.Label(
                    self.main_frame,
                    text=f"{b.place} | {b.hotel} | {b.transport} | {b.cost} Tk"
                ).pack(anchor="w")

        tk.Button(self.main_frame, text="Back", command=self.home_screen).pack(pady=10)

    def logout(self):
        self.current_user = None
        self.login_screen()


# ---------------- Run -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TravelWizApp(root)
    root.mainloop()
