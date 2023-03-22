
import tkinter as tk
from tkinter import messagebox


class Access23:

    def __init__(self):

        self.filename = ''
        self.e_username = tk.Entry
        self.e_password = tk.Entry
        self.e_confirm_password = tk.Entry

        self.return_value = False
        self.credential_window = tk.Tk()

        # self.root_window.protocol('WM_DELETE_WINDOWS')

    # Function definition that allows to create new username and password.
    def create_user(self, filename):

        self.filename = filename

        self.credential_window.title('Create user')
        self.credential_window.geometry('400x300')

        create_user_frame = tk.Frame(self.credential_window, padx=10, pady=10)

        l_username = tk.Label(create_user_frame, text='Create Username: ')
        l_username.grid(row=0, column=0, sticky=tk.E + tk.W)

        self.e_username = tk.Entry(create_user_frame)
        self.e_username.grid(row=0, column=1, sticky=tk.E + tk.W)

        l_password = tk.Label(create_user_frame, text='Create Password: ')
        l_password.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.e_password = tk.Entry(create_user_frame)
        self.e_password.grid(row=1, column=1, sticky=tk.E + tk.W)

        l_confirm_password = tk.Label(create_user_frame, text='Confirm Password: ')
        l_confirm_password.grid(row=2, column=0, sticky=tk.E + tk.W)

        self.e_confirm_password = tk.Entry(create_user_frame)
        self.e_confirm_password.grid(row=2, column=1, sticky=tk.E + tk.W)

        create_user_frame.pack(fill='both', side='top')

        btn_frame = tk.Frame(self.credential_window, padx=10, pady=10)

        btn_create = tk.Button(btn_frame, text='Create', command=self.record_user)
        btn_create.pack(side='left')

        btn_frame.pack(fill='both')

        self.credential_window.mainloop()

    # Function to check if both passwords entered are same and therefore write to a file
    def record_user(self):

        if not self.e_password.get() == self.e_confirm_password.get():
            messagebox.showinfo('Password Error', 'Passwords do not match. Try Again')
            self.e_username.delete(0, 'end')
            self.e_password.delete(0, 'end')
            self.e_confirm_password.delete(0, 'end')
            # return False

        else:
            with open(self.filename, 'w+', encoding='utf-8') as file:
                file.write(self.e_username.get() + ': ' + self.e_password.get() + '\n')

            messagebox.showinfo('Successful Operation', 'New User created')
            self.credential_window.destroy()

            # return True

    def check_user(self, filename):

        self.filename = filename

        self.credential_window.title('Check Credentials')
        self.credential_window.geometry('400x300')

        check_user_frame = tk.Frame(self.credential_window, padx=10, pady=10)

        l_username = tk.Label(check_user_frame, text='Username:')
        l_username.grid(row=0, column=0, sticky=tk.E + tk.W)

        self.e_username = tk.Entry(check_user_frame)
        self.e_username.grid(row=0, column=1, sticky=tk.E + tk.W)

        l_password = tk.Label(check_user_frame, text='Password:')
        l_password.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.e_password = tk.Entry(check_user_frame)
        self.e_password.grid(row=1, column=1, sticky=tk.E + tk.W)

        check_user_frame.pack(side='top', fill='both')

        # btn_login = tk.Button(self.root_window, text='Login', command=self.compare_credentials)
        # btn_login.pack(side='left')

        btn_frame = tk.Frame(self.credential_window, padx=10, pady=10)

        btn_login = tk.Button(btn_frame, text='Login', command=self.compare_credentials)
        btn_login.pack(side='left')

        btn_frame.pack(fill='both')

        self.credential_window.protocol('WM_DELETE_WINDOW', self.unsuccessful)
        self.credential_window.mainloop()

    def compare_credentials(self):

        with open(self.filename, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if i == 0:
                    username, password = line.replace('\n', '').split(': ')

        print(username + ' ' + password)

        if self.e_username.get() == username and self.e_password.get() == password:
            messagebox.showinfo('Credentials Matched', f'Welcome {username} ')
            self.credential_window.destroy()
            # return True

        else:
            messagebox.showinfo('Credential not Matched', f'Try Again ')
            self.e_username.delete(0, 'end')
            self.e_password.delete(0, 'end')
            # return False

    def unsuccessful(self):
        if messagebox.askyesno(title='Confirm', message='Do you want to exit. No user created'):
            exit()
