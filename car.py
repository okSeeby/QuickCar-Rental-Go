import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

#connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PASSWORD",
    database="QuickCarRentalGo"
)
#create cursor
mycursor = mydb.cursor()

"""
class that includes GUI creation and methods that the buttons will call
"""
class CarRentalService:
    """
    Class constructor. Creates main window for most GUI frames to be placed on.
    """
    def __init__(self, root):
        # Main window
        self.root = root
        self.root.title("Quick Car Go")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f2f2f2")  # Light gray background

        # Frame of main window
        self.main_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Display login page
        self.show_login_page()

    """
    Creates user login frame. Clears frame and then places login frame on window.
    """
    def show_login_page(self):
        # Clear main frame
        self.clear_frame()

        # Login title
        tk.Label(self.main_frame, text="Login", font=("Helvetica", 28, "bold"), bg="#f2f2f2", fg="#333333").pack(pady=20)

        # Email entry box
        tk.Label(self.main_frame, text="Email", font=("Helvetica", 12), bg="#f2f2f2", fg="#555555").pack(pady=5)
        self.email_entry = tk.Entry(self.main_frame, font=("Helvetica", 12), width=30)
        self.email_entry.pack(pady=5)

        # Password entry box
        tk.Label(self.main_frame, text="Password", font=("Helvetica", 12), bg="#f2f2f2", fg="#555555").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, font=("Helvetica", 12), show="*", width=30)
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(self.main_frame, text="Login", font=("Helvetica", 12), bg="#4CAF50", fg="white", width=15,
                  command=self.login).pack(pady=20)

        # Sign up button
        tk.Button(self.main_frame, text="Sign Up", font=("Helvetica", 12), bg="#2196F3", fg="white", width=15,
                  command=self.show_signup_page).pack(pady=5)

        # Admin login button
        tk.Button(self.main_frame, text="Admin Login", font=("Helvetica", 12), bg="#FFC107", fg="black", width=15,
                  command=self.show_admin_login_page).pack(pady=5)

    """
    After signup button is pressed on user login page, creates signup frame, clears window, and places frame on window.
    """
    def show_signup_page(self):
        # Clear main frame
        self.clear_frame()

        # Signup title
        tk.Label(self.main_frame, text="Sign Up", font=("Helvetica", 28, "bold"), bg="#f2f2f2", fg="#333333").pack(pady=20)

        # Name entry box
        tk.Label(self.main_frame, text="Name", font=("Helvetica", 12), bg="#f2f2f2", fg="#555555").pack(pady=5)
        self.signup_name_entry = tk.Entry(self.main_frame, font=("Helvetica", 12), width=30)
        self.signup_name_entry.pack(pady=5)

        # Email entry box
        tk.Label(self.main_frame, text="Email", font=("Helvetica", 12), bg="#f2f2f2", fg="#555555").pack(pady=5)
        self.signup_email_entry = tk.Entry(self.main_frame, font=("Helvetica", 12), width=30)
        self.signup_email_entry.pack(pady=5)

        # Password entry box
        tk.Label(self.main_frame, text="Password", font=("Helvetica", 12), bg="#f2f2f2", fg="#555555").pack(pady=5)
        self.signup_password_entry = tk.Entry(self.main_frame, font=("Helvetica", 12), show="*", width=30)
        self.signup_password_entry.pack(pady=5)

        # Phone number entry box
        tk.Label(self.main_frame, text="Phone", font=("Helvetica", 12), bg="#f2f2f2", fg="#555555").pack(pady=5)
        self.signup_phone_entry = tk.Entry(self.main_frame, font=("Helvetica", 12), width=30)
        self.signup_phone_entry.pack(pady=5)

        # Sign up button
        tk.Button(self.main_frame, text="Sign Up", font=("Helvetica", 12), bg="#4CAF50", fg="white", width=15,
                  command=self.signup).pack(pady=20)

        # Back to login button
        tk.Button(self.main_frame, text="Back to Login", font=("Helvetica", 12), bg="#f44336", fg="white", width=15,
                  command=self.show_login_page).pack(pady=5)
    """
    After signup button is pressed on user login page. Create signup frame, clear window, and place frame on window
    """
    def show_signup_page(self):
        
        #clear main frame
        self.clear_frame()
        
        #signup title
        tk.Label(self.main_frame, text="Sign Up", font=("Arial", 24)).pack(pady=20)
        
        #name entry box
        tk.Label(self.main_frame, text="Name").pack(pady=5)
        self.signup_name_entry = tk.Entry(self.main_frame)
        self.signup_name_entry.pack(pady=5)
        
        #email entry box
        tk.Label(self.main_frame, text="Email").pack(pady=5)
        self.signup_email_entry = tk.Entry(self.main_frame)
        self.signup_email_entry.pack(pady=5)
        
        #password entry box
        tk.Label(self.main_frame, text="Password").pack(pady=5)
        self.signup_password_entry = tk.Entry(self.main_frame, show="*")
        self.signup_password_entry.pack(pady=5)
        
        #phone number entry box
        tk.Label(self.main_frame, text="Phone").pack(pady=5)
        self.signup_phone_entry = tk.Entry(self.main_frame)
        self.signup_phone_entry.pack(pady=5)
        
        #sign up button to continue sign up and go to user login page
        tk.Button(self.main_frame, text="Sign Up", command=self.signup).pack(pady=20)
        
        #cancel signup and go to login page
        tk.Button(self.main_frame, text="Back to Login", command=self.show_login_page).pack(pady=5)

    """
    After admin login button is pressed on user login page. Create admin login frame, clear window, and place frame 
    """
    def show_admin_login_page(self):
        # Clear main frame
        self.clear_frame()

        # Define styles
        title_font = ("Arial", 24, "bold")
        label_font = ("Arial", 14)
        entry_font = ("Arial", 12)
        button_font = ("Arial", 14, "bold")
        bg_color = "#f0f8ff"  # Light blue background
        button_color = "#007acc"  # Blue button
        button_active_color = "#005f99"  # Darker blue on hover
        text_color = "#2a2a2a"  # Dark text color

        # Set background color for the main frame
        self.main_frame.configure(bg=bg_color)

        # Admin login title
        tk.Label(
            self.main_frame, text="Admin Login", font=title_font, bg=bg_color, fg=text_color
        ).pack(pady=20)

        # Email entry box
        tk.Label(
            self.main_frame, text="Email", font=label_font, bg=bg_color, fg=text_color
        ).pack(pady=10)
        self.admin_email_entry = tk.Entry(self.main_frame, font=entry_font, width=30)
        self.admin_email_entry.pack(pady=5)

        # Password entry box
        tk.Label(
            self.main_frame, text="Password", font=label_font, bg=bg_color, fg=text_color
        ).pack(pady=10)
        self.admin_password_entry = tk.Entry(
            self.main_frame, show="*", font=entry_font, width=30
        )
        self.admin_password_entry.pack(pady=5)

        # Login button
        tk.Button(
            self.main_frame,
            text="Login",
            command=self.admin_login,
            font=button_font,
            bg=button_color,
            fg="white",
            activebackground=button_active_color,
            activeforeground="white",
            relief="raised",
        ).pack(pady=20)

        # Signup button to go to admin signup page
        tk.Button(
            self.main_frame,
            text="Admin Sign Up",
            command=self.show_admin_signup_page,
            font=button_font,
            bg="#ffc107",  # Amber button
            fg="black",
            activebackground="#e6a700",
            activeforeground="black",
            relief="raised",
        ).pack(pady=10)

        # Back button to go back to user login page
        tk.Button(
            self.main_frame,
            text="Back to Login",
            command=self.show_login_page,
            font=button_font,
            bg="#d9534f",  # Red button
            fg="white",
            activebackground="#c9302c",
            activeforeground="white",
            relief="raised",
        ).pack(pady=10)
    
    """
    After admin signup button is pressed on admin login page. Create admin signup frame, clear window, and place frame 
    """
    def show_admin_signup_page(self):
        # Clear main frame
        self.clear_frame()
        
        # Configure background color
        self.main_frame.configure(bg="#f0f4f8")  # Light background color
        
        # Title label with enhanced styling
        tk.Label(
            self.main_frame,
            text="Admin Sign Up",
            font=("Arial", 28, "bold"),
            fg="#2c3e50",          # Dark blue-gray color
            bg="#f0f4f8"           # Matching the frame background
        ).pack(pady=20)
        
        # Input field styling
        entry_bg_color = "#ecf0f1"  # Light gray for entry boxes
        label_fg_color = "#34495e"  # Darker text color for labels
        entry_font = ("Arial", 14)
        
        # Function to create labeled entry fields
        def create_entry(label_text, show_char=None):
            tk.Label(
                self.main_frame,
                text=label_text,
                font=("Arial", 14, "bold"),
                fg=label_fg_color,
                bg="#f0f4f8"
            ).pack(pady=5)
            
            entry = tk.Entry(self.main_frame, font=entry_font, bg=entry_bg_color, show=show_char)
            entry.pack(pady=5, ipadx=5, ipady=5)
            return entry
        
        # Name entry box
        self.admin_signup_name_entry = create_entry("Name")
        
        # Email entry box
        self.admin_signup_email_entry = create_entry("Email")
        
        # Password entry box
        self.admin_signup_password_entry = create_entry("Password", show_char="*")
        
        # Phone number entry box
        self.admin_signup_phone_entry = create_entry("Phone")
        
        # Button styling
        button_style = {
            "font": ("Arial", 14, "bold"),
            "bg": "#2980b9",          # Blue color for buttons
            "fg": "white",            # White text for contrast
            "activebackground": "#1f618d",  # Darker blue when pressed
            "activeforeground": "white",
            "padx": 20,
            "pady": 10
        }
        
        # Sign Up button
        tk.Button(
            self.main_frame,
            text="Sign Up",
            command=self.admin_signup,
            **button_style
        ).pack(pady=20)
        
        # Back button
        tk.Button(
            self.main_frame,
            text="Back to Admin Login",
            command=self.show_admin_login_page,
            bg="#95a5a6",          # Gray color for back button
            fg="white",
            activebackground="#7f8c8d",
            activeforeground="white",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10
        ).pack(pady=10)
    """
    After login button is pressed on user login page. Search for matching email and password.
    Error message if not found. Main page displayed if found
    """
    def login(self):
        
        #get email and password from entry box
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        #search for customer with email and password
        mycursor.execute("SELECT * FROM customers WHERE email=%s AND password=%s", (email, password))
        
        #fetch the user 
        user = mycursor.fetchone()
        
        #if user exists
        if user:
            #get userID and go to user main page
            self.user_id = user[0]
            self.show_user_main_page()
        
        #user does not exist
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    """
    After signup button is pressed on user signup page. Insert customer into database. 
    Show success message and load user login frame
    """
    def signup(self):
        # get data from entry boxes
        name = self.signup_name_entry.get()
        email = self.signup_email_entry.get()
        password = self.signup_password_entry.get()
        phone = self.signup_phone_entry.get()
        
        # create customer and insert into database
        mycursor.execute("INSERT INTO customers (name, email, password, phone) VALUES (%s, %s, %s, %s)", 
                        (name, email, password, phone))
        mydb.commit()

        # Store the user's name in self.user_name
        self.user_name = name
        
        # success message and return to user login page
        messagebox.showinfo("Success", "Signup successful")
        self.show_user_main_page()  # Show main page after successful signup


    """
    After login button is pressed on admin login page. Search for matching email and password.
    Error message if not found. Main admin page displayed if found
    """
    def admin_login(self):
        
        #get email and password from entry boxes
        email = self.admin_email_entry.get()
        password = self.admin_password_entry.get()
        
        #find admin that has email and password
        mycursor.execute("SELECT * FROM admins WHERE email=%s AND password=%s", (email, password))
        
        #fetch the admin
        admin = mycursor.fetchone()
        
        #if user exists
        if admin:
            #get adminID and go to admin main page
            self.admin_id = admin[0]
            self.show_admin_main_page()
        
        #if user does not exist
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    """
    After signup button is pressed on admin signup page. Insert admin into database. 
    Show success message and load admin login frame
    """
    def admin_signup(self):
        
        #get admin info from entry boxes
        name = self.admin_signup_name_entry.get()
        email = self.admin_signup_email_entry.get()
        password = self.admin_signup_password_entry.get()
        phone = self.admin_signup_phone_entry.get()
        
        #create admin and insert into database
        mycursor.execute("INSERT INTO admins (name, email, password, phone) VALUES (%s, %s, %s, %s)", 
                         (name, email, password, phone))
        mydb.commit()
        
        #success message and return to admin login page
        messagebox.showinfo("Success", "Admin signup successful")
        self.show_admin_login_page()

    """
    Create main frame for user. Clear window and display frame
    """
    def show_user_main_page(self):
        # Clear frame
        self.clear_frame()

        # Define styles
        title_font = ("Arial", 24, "bold")
        welcome_font = ("Arial", 30, "italic")  # Large font for welcome message
        button_font = ("Arial", 14, "bold")
        points_font = ("Arial", 12, "bold")  # Font for loyalty points counter
        bg_color = "#f0f8ff"  # Light blue background
        treeview_color = "#e6f7ff"  # Slightly lighter blue for treeview
        button_color = "#007acc"  # Blue button
        button_active_color = "#005f99"  # Darker blue on hover
        text_color = "#2a2a2a"  # Dark text color
        welcome_color = "#4CAF50"  # Friendly green color for the welcome message
        points_color = "#ff5722"  # Orange color for loyalty points counter

        # Set main frame background
        self.main_frame.configure(bg=bg_color)

        # Display dropdown menu
        self.setup_menu(self.show_login_page)

        # Welcome message at the top
        tk.Label(
            self.main_frame,
            text=f"Welcome Renter!",  # Display the welcome message with user's name
            font=welcome_font,
            bg=bg_color,
            fg=welcome_color,
        ).pack(pady=20)  # Extra padding to make it stand out


        self.points = 0  # Example value, fetch or calculate based on user
        tk.Label(
            self.main_frame,
            text=f"Loyalty Points: {self.points}",
            font=points_font,
            bg=bg_color,
            fg=points_color,
        ).place(relx=0.85, rely=0.05, anchor="ne")  # Top-right corner position

        # User main page title
        tk.Label(
            self.main_frame, text="Available Cars", font=title_font, bg=bg_color, fg=text_color
        ).pack(pady=20)

        # Treeview to display cars
        self.car_tree = ttk.Treeview(
            self.main_frame,
            columns=("car_id", "make", "model", "year", "price"),
            show="headings",
            style="Custom.Treeview"
        )

        # Treeview headings
        self.car_tree.heading("car_id", text="Car ID")
        self.car_tree.heading("make", text="Make")
        self.car_tree.heading("model", text="Model")
        self.car_tree.heading("year", text="Year")
        self.car_tree.heading("price", text="Price")

        # Apply custom treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", background=treeview_color, font=("Arial", 12))
        style.configure("Custom.Treeview.Heading", font=("Arial", 14, "bold"), background="#d0eaff")

        # Put treeview on the main frame
        self.car_tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Enter car information into treeview
        self.load_cars()

        # Frame to hold buttons
        btn_frame = tk.Frame(self.main_frame, bg=bg_color)
        btn_frame.pack(pady=20)

        # Book car button
        tk.Button(
            btn_frame,
            text="Book Car",
            command=self.book_car_page,
            font=button_font,
            bg=button_color,
            fg="white",
            activebackground=button_active_color,
            activeforeground="white",
            relief="raised",
        ).pack(side=tk.LEFT, padx=10)

        # View bookings button
        tk.Button(
            btn_frame,
            text="View Bookings",
            command=self.view_bookings_page,
            font=button_font,
            bg="#ffc107",  # Amber button for variety
            fg="black",
            activebackground="#e6a700",
            activeforeground="black",
            relief="raised",
        ).pack(side=tk.LEFT, padx=10)


    """
    Create main frame for admin. Clear window and display frame
    """
    def show_admin_main_page(self):
        # Clear main frame
        self.clear_frame()

        # Define styles
        title_font = ("Arial", 24, "bold")
        welcome_font = ("Arial", 30, "italic")  # Large font for welcome message
        button_font = ("Arial", 14, "bold")
        bg_color = "#f0f8ff"  # Light blue background
        treeview_color = "#e6f7ff"  # Slightly lighter blue for treeview
        button_color = "#007acc"  # Blue button
        button_active_color = "#005f99"  # Darker blue on hover
        text_color = "#2a2a2a"  # Dark text color
        welcome_color = "#4CAF50"  # Friendly green color for the welcome message

        # Set main frame background
        self.main_frame.configure(bg=bg_color)

        # Setup main frame for admin main page
        self.setup_menu(self.show_admin_login_page)

        # Welcome message at the top
        tk.Label(
            self.main_frame,
            text="Welcome back, Admin!",
            font=welcome_font,
            bg=bg_color,
            fg=welcome_color,
        ).pack(pady=20)  # Extra padding to make it stand out

        # Manage cars title
        tk.Label(
            self.main_frame, text="Manage Cars", font=title_font, bg=bg_color, fg=text_color
        ).pack(pady=20)

        # Create treeview to view cars
        self.car_tree = ttk.Treeview(
            self.main_frame,
            columns=("car_id", "make", "model", "year", "price"),
            show="headings",
            style="Custom.Treeview",
        )

        # Treeview headings
        self.car_tree.heading("car_id", text="Car ID")
        self.car_tree.heading("make", text="Make")
        self.car_tree.heading("model", text="Model")
        self.car_tree.heading("year", text="Year")
        self.car_tree.heading("price", text="Price")

        # Apply custom treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", background=treeview_color, font=("Arial", 12))
        style.configure(
            "Custom.Treeview.Heading", font=("Arial", 14, "bold"), background="#d0eaff"
        )

        # Put treeview on the main frame
        self.car_tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Enter car information into treeview
        self.load_cars()

        # Frame to hold buttons
        btn_frame = tk.Frame(self.main_frame, bg=bg_color)
        btn_frame.pack(pady=20)

        # Update car button
        tk.Button(
            btn_frame,
            text="Update Car",
            command=self.update_car_page,
            font=button_font,
            bg=button_color,
            fg="white",
            activebackground=button_active_color,
            activeforeground="white",
            relief="raised",
        ).pack(side=tk.LEFT, padx=10)

        # View bookings button
        tk.Button(
            btn_frame,
            text="View Bookings",
            command=self.view_all_bookings_page,
            font=button_font,
            bg="#ffc107",  # Amber button for variety
            fg="black",
            activebackground="#e6a700",
            activeforeground="black",
            relief="raised",
        ).pack(side=tk.LEFT, padx=10)

        # Add car button
        tk.Button(
            self.main_frame,
            text="Add Car",
            command=self.add_car_page,
            font=button_font,
            bg="#5cb85c",  # Green button for action
            fg="white",
            activebackground="#4cae4c",
            activeforeground="white",
            relief="raised",
        ).pack(pady=20)

    """
    After book car button is clicked for user. Open window to confirm booking details.
    """
    def book_car_page(self):
        # Get selected car
        selected_car = self.car_tree.selection()

        # If no car is selected
        if not selected_car:
            messagebox.showerror("Error", "No car selected")
            return

        # Get carID
        car_id = self.car_tree.item(selected_car[0])["values"][0]

        # Create new window
        self.car_booking_window = tk.Toplevel(self.root)
        self.car_booking_window.title("Book Car")
        self.car_booking_window.geometry("400x570")

        # Define styles
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)
        button_font = ("Arial", 14, "bold")
        bg_color = "#f7f9fc"  # Soft light gray-blue
        text_color = "#2a2a2a"  # Dark text color
        button_color = "#007acc"  # Blue button
        button_active_color = "#005f99"  # Darker blue on hover

        # Set window background
        self.car_booking_window.configure(bg=bg_color)

        # Helper function to create labeled entries
        def create_labeled_entry(parent, label_text, font, var_name, state=tk.NORMAL):
            tk.Label(
                parent, text=label_text, font=label_font, bg=bg_color, fg=text_color
            ).pack(pady=5)
            entry = tk.Entry(parent, font=font, state=state)
            entry.pack(pady=5)
            return entry

        # From date entry box
        tk.Label(
            self.car_booking_window, text="From Date (YYYY-MM-DD)", font=label_font, bg=bg_color, fg=text_color
        ).pack(pady=5)
        self.from_date_entry = tk.Entry(self.car_booking_window, font=entry_font)
        self.from_date_entry.pack(pady=5)

        # To date entry box
        tk.Label(
            self.car_booking_window, text="To Date (YYYY-MM-DD)", font=label_font, bg=bg_color, fg=text_color
        ).pack(pady=5)
        self.to_date_entry = tk.Entry(self.car_booking_window, font=entry_font)
        self.to_date_entry.pack(pady=5)

        # Radio button variable
        self.payment_method = tk.StringVar(value="card")  # Default to card

        # Radio buttons
        tk.Label(
            self.car_booking_window, text="Payment Method", font=label_font, bg=bg_color, fg=text_color
        ).pack(pady=10)
        radio_frame = tk.Frame(self.car_booking_window, bg=bg_color)
        radio_frame.pack(pady=5)

        tk.Radiobutton(
            radio_frame,
            text="Payment Card",
            variable=self.payment_method,
            value="card",
            font=label_font,
            bg=bg_color,
            fg=text_color,
            command=self.toggle_payment_method,
        ).pack(side=tk.LEFT, padx=10)

        tk.Radiobutton(
            radio_frame,
            text="Use Points",
            variable=self.payment_method,
            value="points",
            font=label_font,
            bg=bg_color,
            fg=text_color,
            command=self.toggle_payment_method,
        ).pack(side=tk.LEFT, padx=10)

        # Cardholder name entry box
        self.carholder_name = create_labeled_entry(
            self.car_booking_window, "Cardholder Name", entry_font, "carholder_name"
        )

        # Payment card info entry box
        self.card_num = create_labeled_entry(
            self.car_booking_window, "Payment Card Number", entry_font, "card_num"
        )

        # CVV entry box
        self.cvv_num = create_labeled_entry(
            self.car_booking_window, "CVV Number", entry_font, "cvv_num"
        )

        # Points entry box
        self.points = create_labeled_entry(
            self.car_booking_window, "Points", entry_font, "points", state=tk.DISABLED
        )

        # Book button
        tk.Button(
            self.car_booking_window,
            text="Book",
            command=lambda: self.book_car(car_id),
            font=button_font,
            bg=button_color,
            fg="white",
            activebackground=button_active_color,
            activeforeground="white",
            relief="raised",
        ).pack(pady=20)

     

    # Add toggle method
    def toggle_payment_method(self):
        if self.payment_method.get() == "card":
            self.carholder_name.config(state=tk.NORMAL)
            self.card_num.config(state=tk.NORMAL)
            self.cvv_num.config(state=tk.NORMAL)
            self.points.config(state=tk.DISABLED)
        else:
            self.carholder_name.config(state=tk.DISABLED)
            self.card_num.config(state=tk.DISABLED)
            self.cvv_num.config(state=tk.DISABLED)
            self.points.config(state=tk.NORMAL)

    # Add function to add points
    
    def add_points_to_user(self, customer_id, points_to_add):
        """
        Adds points to a customer's profile in the database.
        """
        try:
            query = "UPDATE customers SET points = points + %s WHERE customer_id = %s"
            self.db_cursor.execute(query, (points_to_add, customer_id))
            mydb.commit()  # Commit changes to the database
            messagebox.showinfo("Success", f"{points_to_add} points have been added to your account!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to update points: {e}")

    # Update book_car to add points if "Payment Card" is selected
    def book_car(self, car_id):
        if self.payment_method.get() == "card":
            self.add_points_to_user(self.current_user_id, 10)  # Add 10 points to the user's profile
        else:
            # Deduct points logic or other booking logic using points
            pass

        # Rest of the booking logic here

    """
    After Book button is clicked on book car window. Insert order into database
    """
    def book_car(self, car_id):
        
        #get from and to date from entry box
        from_date = self.from_date_entry.get()
        to_date = self.to_date_entry.get()
        
        #check for booking conflicts
        mycursor.execute("""
            SELECT * FROM orders
            WHERE car_id = %s
            AND ((from_date <= %s AND to_date >= %s)
            OR (from_date <= %s AND to_date >= %s)
            OR (from_date >= %s AND to_date <= %s))
        """, (car_id, from_date, from_date, to_date, to_date, from_date, to_date))
        
        #fetch conflicts
        conflict = mycursor.fetchall()
        
        #if conflict exists
        if conflict:
            messagebox.showerror("Error", "Car is already booked for the selected dates.")
        
        #no conflict
        else:
            
            #create and insert order
            mycursor.execute("INSERT INTO orders (customer_id, car_id, from_date, to_date, status) VALUES (%s, %s, %s, %s, %s)", 
                            (self.user_id, car_id, from_date, to_date, "Booked"))
            mydb.commit()
            
            #success message and close booking window
            messagebox.showinfo("Success", "Car booked successfully")
            self.car_booking_window.destroy()
    
    """
    After view bookings button is clocked on user main page. Open new window to display orders
    """
    def view_bookings_page(self):
        # Create a new window
        self.bookings_window = tk.Toplevel(self.root)
        self.bookings_window.title("My Bookings")
        self.bookings_window.geometry("1200x400")
        self.bookings_window.configure(bg="#f0f4f8")  # Light background color

        # Title label with enhanced styling
        tk.Label(
            self.bookings_window,
            text="My Bookings",
            font=("Arial", 28, "bold"),
            fg="#2c3e50",          # Dark blue-gray color
            bg="#f0f4f8"           # Matching the window background
        ).pack(pady=20)

        # Create Treeview with striped row colors
        style = ttk.Style()
        style.theme_use("clam")  # Use a clean, modern theme
        style.configure("Treeview",
                        background="#ecf0f1",
                        foreground="#2c3e50",
                        rowheight=30,
                        fieldbackground="#ecf0f1",
                        font=("Arial", 12))
        style.map('Treeview', background=[('selected', '#3498db')])  # Highlight color when row is selected

        # Heading style for the Treeview
        style.configure("Treeview.Heading",
                        font=("Arial", 14, "bold"),
                        background="#2980b9",
                        foreground="white")

        # Create Treeview to display order information
        self.bookings_tree = ttk.Treeview(
            self.bookings_window,
            columns=("make", "model", "year", "from_date", "to_date", "status"),
            show="headings"
        )

        # Treeview headings with adjusted text alignment
        self.bookings_tree.heading("make", text="Make", anchor="center")
        self.bookings_tree.heading("model", text="Model", anchor="center")
        self.bookings_tree.heading("year", text="Year", anchor="center")
        self.bookings_tree.heading("from_date", text="From Date", anchor="center")
        self.bookings_tree.heading("to_date", text="To Date", anchor="center")
        self.bookings_tree.heading("status", text="Status", anchor="center")

        # Set column width
        self.bookings_tree.column("make", width=150, anchor="center")
        self.bookings_tree.column("model", width=150, anchor="center")
        self.bookings_tree.column("year", width=100, anchor="center")
        self.bookings_tree.column("from_date", width=200, anchor="center")
        self.bookings_tree.column("to_date", width=200, anchor="center")
        self.bookings_tree.column("status", width=150, anchor="center")

        # Add striped rows
        self.bookings_tree.tag_configure('evenrow', background='#d5dbdb')
        self.bookings_tree.tag_configure('oddrow', background='#ecf0f1')

        # Pack the Treeview with padding
        self.bookings_tree.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)

        # Call method to load orders into Treeview
        self.load_bookings()

    """
    After view all bookings button is clocked on admin main page. Open new window to display orders
    """
    def view_all_bookings_page(self):
        # Create window for bookings page
        self.all_bookings_window = tk.Toplevel(self.root)
        self.all_bookings_window.title("All Bookings")
        self.all_bookings_window.geometry("1200x500")
        self.all_bookings_window.configure(bg="#f0f4f8")  # Light background color

        # Title label with enhanced styling
        tk.Label(
            self.all_bookings_window,
            text="All Bookings",
            font=("Arial", 28, "bold"),
            fg="#2c3e50",          # Dark blue-gray color
            bg="#f0f4f8"           # Matching the window background
        ).pack(pady=20)

        # Create Treeview with striped row colors
        style = ttk.Style()
        style.theme_use("clam")  # Use a clean, modern theme
        style.configure("Treeview",
                        background="#ecf0f1",
                        foreground="#2c3e50",
                        rowheight=30,
                        fieldbackground="#ecf0f1",
                        font=("Arial", 12))
        style.map("Treeview", background=[("selected", "#3498db")])  # Highlight color when row is selected

        # Heading style for the Treeview
        style.configure("Treeview.Heading",
                        font=("Arial", 14, "bold"),
                        background="#2980b9",
                        foreground="white")

        # Create Treeview to display order information
        self.all_bookings_tree = ttk.Treeview(
            self.all_bookings_window,
            columns=("order_id", "customer_id", "car_id", "from_date", "to_date", "status"),
            show="headings"
        )

        # Treeview headings with adjusted text alignment
        headings = [
            ("order_id", "Order ID"),
            ("customer_id", "Customer ID"),
            ("car_id", "Car ID"),
            ("from_date", "From Date"),
            ("to_date", "To Date"),
            ("status", "Status")
        ]

        for col, text in headings:
            self.all_bookings_tree.heading(col, text=text, anchor="center")
            self.all_bookings_tree.column(col, width=150, anchor="center")

        # Add striped rows
        self.all_bookings_tree.tag_configure("evenrow", background="#d5dbdb")
        self.all_bookings_tree.tag_configure("oddrow", background="#ecf0f1")

        # Pack the Treeview with padding
        self.all_bookings_tree.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)

        # Label and Entry for Customer ID
        tk.Label(
            self.all_bookings_window,
            text="Customer ID",
            font=("Arial", 14, "bold"),
            fg="#34495e",
            bg="#f0f4f8"
        ).pack(pady=5)

        self.customerID_entry = tk.Entry(self.all_bookings_window, font=("Arial", 14), bg="#ecf0f1")
        self.customerID_entry.pack(pady=5, ipadx=5, ipady=5)

        # Button styling
        button_style = {
            "font": ("Arial", 14, "bold"),
            "bg": "#2980b9",          # Blue color for button
            "fg": "white",            # White text for contrast
            "activebackground": "#1f618d",  # Darker blue when pressed
            "activeforeground": "white",
            "padx": 20,
            "pady": 10
        }

        # Button to send email to late user
        tk.Button(
            self.all_bookings_window,
            text="Email User",
            command=self.email_user,
            **button_style
        ).pack(pady=20)

        # Load order information into the Treeview
        self.load_all_bookings()
    """
    After clicking email user button, send email to user
    """
    def email_user(self):
        
        #get email using customer ID
        customer_id = self.customerID_entry.get()
        mycursor.execute("SELECT email FROM customers WHERE customer_id=%s;", (customer_id,))
        email = mycursor.fetchone()
        
        #email found
        if email:
            messagebox.showinfo("Success","Successfully sent email to customer")
        
        #email not found
        else:
            messagebox.showerror("Error","Customer email not found")

    """
    After update car button is selected on admin main page. Open new window for entries of car information
    """
    def update_car_page(self):
        
        #get car selected in treeview
        selected_car = self.car_tree.selection()
        
        #if no car selected
        if not selected_car:
            messagebox.showerror("Error", "No car selected")
            return
        
        #get carID of selection
        car_id = self.car_tree.item(selected_car[0])["values"][0]
        
        #create new window to update car 
        self.car_update_window = tk.Toplevel(self.root)
        self.car_update_window.title("Update Car")
        self.car_update_window.geometry("400x300")
        
        #make entry box
        tk.Label(self.car_update_window, text="Make").pack(pady=5)
        self.update_make_entry = tk.Entry(self.car_update_window)
        self.update_make_entry.pack(pady=5)
        
        #model entry box
        tk.Label(self.car_update_window, text="Model").pack(pady=5)
        self.update_model_entry = tk.Entry(self.car_update_window)
        self.update_model_entry.pack(pady=5)
        
        #year entry box
        tk.Label(self.car_update_window, text="Year (YYYY)").pack(pady=5)
        self.update_year_entry = tk.Entry(self.car_update_window)
        self.update_year_entry.pack(pady=5)
        
        #price entry box
        tk.Label(self.car_update_window, text="Price").pack(pady=5)
        self.update_price_entry = tk.Entry(self.car_update_window)
        self.update_price_entry.pack(pady=5)
        
        #update button to update the car information in db
        tk.Button(self.car_update_window, text="Update", command=lambda: self.update_car(car_id)).pack(pady=20)

    """
    After update button is clicked on update car window. Update car information on database and reload cars on main page
    """
    def update_car_page(self):
        # Get car selected in treeview
        selected_car = self.car_tree.selection()

        # If no car selected
        if not selected_car:
            messagebox.showerror("Error", "No car selected")
            return

        # Get carID of selection
        car_id = self.car_tree.item(selected_car[0])["values"][0]

        # Create new window to update car
        self.car_update_window = tk.Toplevel(self.root)
        self.car_update_window.title("Update Car")
        self.car_update_window.geometry("400x400")
        self.car_update_window.configure(bg="#f0f4f8")  # Light background color

        # Title label
        tk.Label(
            self.car_update_window,
            text="Update Car Information",
            font=("Arial", 20, "bold"),
            fg="#2c3e50",       # Dark blue-gray color
            bg="#f0f4f8"
        ).pack(pady=20)

        # Entry field styling
        entry_bg_color = "#ecf0f1"  # Light gray background for entries
        label_fg_color = "#34495e"  # Darker text color for labels
        entry_font = ("Arial", 14)

        # Function to create labeled entry fields
        def create_entry(label_text):
            tk.Label(
                self.car_update_window,
                text=label_text,
                font=("Arial", 14, "bold"),
                fg=label_fg_color,
                bg="#f0f4f8"
            ).pack(pady=5)

            entry = tk.Entry(self.car_update_window, font=entry_font, bg=entry_bg_color)
            entry.pack(pady=5, ipadx=5, ipady=5, fill=tk.X, padx=20)
            return entry

        # Make entry box
        self.update_make_entry = create_entry("Make")

        # Model entry box
        self.update_model_entry = create_entry("Model")

        # Year entry box
        self.update_year_entry = create_entry("Year (YYYY)")

        # Price entry box
        self.update_price_entry = create_entry("Price")

        # Button styling
        button_style = {
            "font": ("Arial", 14, "bold"),
            "bg": "#27ae60",           # Green button color
            "fg": "white",             # White text for contrast
            "activebackground": "#229954",  # Darker green when pressed
            "activeforeground": "white",
            "padx": 20,
            "pady": 10
        }

        # Update button to update the car information in the database
        tk.Button(
            self.car_update_window,
            text="Update",
            command=lambda: self.update_car(car_id),
            **button_style
        ).pack(pady=20)
    """
    After add button is clicked on add car window. Insert new car into database and reload cars on main page.
    """
    def add_car(self):
        
        #get car info
        make = self.add_make_entry.get()
        model = self.add_model_entry.get()
        year = self.add_year_entry.get()
        price = self.add_price_entry.get()
        
        #create car and insert into db
        mycursor.execute("INSERT INTO cars (make, model, year, price) VALUES (%s, %s, %s, %s)", 
                         (make, model, year, price))
        mydb.commit()
        messagebox.showinfo("Success", "Car added successfully")
        
        #close add car window 
        self.car_add_window.destroy()
        
        #reload cars in main treeview
        self.load_cars()
    
    """
    Clear tree view then retrieve car information from database and insert into tree view
    """
    def load_cars(self):
        
        #iterate through treeview
        for i in self.car_tree.get_children():
            
            #delete car
            self.car_tree.delete(i)
            
        #retrieve all cars 
        mycursor.execute("SELECT * FROM cars")
        
        #fetch all car data
        cars = mycursor.fetchall()
        
        #for each car
        for car in cars:
            
            #insert into treeview
            self.car_tree.insert("", "end", values=car)

    """
    Clear tree view then retrieve order information from database and insert into tree view of user booking window
    """
    def load_bookings(self):
        
        #iterate through treeview
        for i in self.bookings_tree.get_children():
            
            #delete order
            self.bookings_tree.delete(i)
            
        #change status if order is late
        mycursor.execute("UPDATE orders SET status = 'Late' WHERE to_date < CURDATE() AND status = 'Booked'")
        
        #retrieve all orders where order customerID is equal to userID
        mycursor.execute("SELECT c.make, c.model, c.year, o.from_date, o.to_date, o.status FROM orders o JOIN cars c ON o.car_id=c.car_id WHERE o.customer_id=%s", 
                         (self.user_id,))
        
        #fetch all orders
        bookings = mycursor.fetchall()
        
        #iterate through orders
        for booking in bookings:
            
            #insert into treeview
            self.bookings_tree.insert("", "end", values=booking)

    """
    Clear tree view then retrieve order information from database and insert into tree view of admin booking window    
    """
    def load_all_bookings(self):
        
        #iterate through all bookings
        for i in self.all_bookings_tree.get_children():
            
            #delete booking
            self.all_bookings_tree.delete(i)
            
        #change status if order is late
        mycursor.execute("UPDATE orders SET status = 'Late' WHERE to_date < CURDATE() AND status = 'Booked'")
        
        #retrieve all orders
        mycursor.execute("SELECT * FROM orders")
        
        #fetch all orders
        bookings = mycursor.fetchall()
        
        #iterate through orders
        for booking in bookings:
            
            #insert into treeview
            self.all_bookings_tree.insert("", "end", values=booking)
            
    """
    Create menu bar at top of main pages for logout/exit  
    """
    def setup_menu(self, logout_command):
        
        #create menubar
        menubar = tk.Menu(self.root)

        #create menu in menubar
        filemenu = tk.Menu(menubar, tearoff=0)
        
        #add logout command to return to user/admin login page
        filemenu.add_command(label="Logout", command=logout_command)
        
        #add exit command to exit program
        filemenu.add_command(label="Exit", command=self.root.quit)
        
        #add dropdown in menu
        menubar.add_cascade(label="File", menu=filemenu)
        
        #configure menu of main window
        self.root.config(menu=menubar)

    """
    Wipe window
    """
    def clear_frame(self):
        
        #iterate through main frame
        for widget in self.main_frame.winfo_children():
            
            #delete
            widget.destroy()

def main():
    
    #create root object
    root = tk.Tk()

    #create CarRentalService GUI
    app = CarRentalService(root)

    #run GUI
    root.mainloop()

main()
