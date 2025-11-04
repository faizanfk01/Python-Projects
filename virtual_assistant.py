import webbrowser
import win32com.client
import speech_recognition as sr
import requests
import json
import time
import os
from openai import OpenAI
from websites import websites

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 2

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        print("Speech service is unavailable.")
        return ""

def open_ai(prompt):
  client = OpenAI(
    api_key="your-api-here"
  )

  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
      {"role": "system", "content": "You are a helpful virtual assistant. Be helpful, polite, and concise. Respond clearly and directly"},
      {"role": "user", "content": prompt},
    ]
  )
  print(completion.choices[0].message.content)
  speaker.Speak(completion.choices[0].message.content)

def news():
  api_key = "your-api-here"
  speaker.Speak("What type of news do you want?: ")
  print("What type of news do you want?: ")
  query = take_command()

  url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

  r = requests.get(url)

  news = json.loads(r.text)

  for article in news["articles"]:
      print(f"Title: {article["title"]}")
      print(f"Description: {article["description"]}")
      speaker.Speak(f"Title: {article["title"]}")
      speaker.Speak(f"Description: {article["description"]}")
      print()
      print("-----------------------------------------")
      command = take_command().lower()
      
      if "panda" in command:
        speaker.speak("Yes, I am Listening")
        print("Yes, I am Listening")
        process_command()
        break

def save_credentials():
    print("Say the name of the website or app: ")
    speaker.Speak("Say the name of the website or app: ")
    website = take_command().capitalize()
    email = input(f"Enter the email for {website}: ")
    password = input(f"Enter the password for {website}: ")

    with open("credentials.txt", "a") as file:
        file.write(f"{website} | Email: {email} | Password: {password}\n")

    print(f"\nEmail and password for '{website}' saved successfully!\n")
    speaker.Speak(f"Email and password for '{website}' saved successfully!")
    print("What do you want to do next?")
    speaker.Speak("What do you want to do next?")


def view_credentials():
    print("Enter the website or app name to view credentials: ")
    speaker.Speak("Enter the website or app name to view credentials: ")
    website = take_command().capitalize()
    found = False

    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                if website.lower() in line.lower():
                    print(f"Here are your credentials for {website}: ")
                    speaker.Speak(f"Here are your credentials for {website}: ")
                    print("🔐", line.strip())
                    time.sleep(2)
                    print("What do you want to do next?")
                    speaker.Speak("What do you want to do next?")
                    found = True
        if not found:
            print(f"No credentials found for {website}.")
            speaker.Speak(f"No credentials found for {website}.")
    except FileNotFoundError:
        speaker.Speak("No data file found. Save something first!")
        print("No data file found. Save something first!")


def run_credential_program():
    print("\nWelcome to Email & Password Manager")
    speaker.Speak("Welcome to Email & Password Manager")
    while True:
      print("Do you want to [save] credentials or [view] data? say 'exit' to quit: ")
      speaker.Speak("Do you want to save credentials or view data? say 'exit' to quit.")
      choice = take_command().lower()
      if "save" in choice :
          save_credentials()
      elif "view" in choice :
          view_credentials()
      elif "exit" in choice:
          print("Goodbye!")
          speaker.Speak("Goodbye!")
          break
      else:
          print("Invalid choice. Please say 'save', 'view', or 'exit'.\n")
          speaker.Speak("Invalid choice. Please say 'save', 'view', or 'exit'.")

data_file = "employees_details.txt"

def extract_emp_id(line):
    try:
        return line.strip().split("Employee ID: ")[-1].strip()
    except IndexError:
        return ""

def is_valid_text(text):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'.")
    return all(c in allowed for c in text)

def id_exists(emp_id):
    try:
        with open(data_file, "r") as file:
            for line in file:
                if extract_emp_id(line) == str(emp_id):
                    return True
    except FileNotFoundError:
        return False
    return False


def add_employee():
    print("\nAdd New Employee")
    speaker.Speak("Add New Employee")
    while True:
        speaker.Speak("Enter employee name: ")
        name = input("Enter employee name: ").title().strip()
        if is_valid_text(name):
            break
        else:
            print("Name should not contain numbers or special characters.")
            speaker.Speak("Name should not contain numbers or special characters.")

    while True:
        speaker.Speak("Enter employee role: ")
        role = input("Enter employee role: ").title().strip()
        if is_valid_text(role):
            break
        else:
            print("Role should not contain numbers or special characters.")
            speaker.Speak("Role should not contain numbers or special characters.")

    while True:
        speaker.Speak("Enter Employee salary: ")
        salary = input("Enter Employee salary: ")
        if salary.isdigit():
            salary = int(salary)
            break
        else:
            print("Salary should be a valid number.")
            speaker.Speak("Salary should be a valid number.")

    while True:
        speaker.Speak("Enter employee ID: ")
        emp_id = input("Enter employee ID: ")
        if emp_id.isdigit() and not id_exists(emp_id):
            emp_id = int(emp_id)
            break
        else:
            print("Invalid or duplicate Employee ID.")
            speaker.Speak("Invalid or duplicate Employee ID.")

    with open(data_file, 'a+') as f:
        f.seek(0)
        if f.read().strip():
            f.write("\n")
        f.write(f"The Employee name is: {name} | His/Her Role: {role} | Salary: Rs. {salary} | Employee ID: {emp_id}")
        print(f"\n{name} added successfully!")
        speaker.Speak(f"{name} added successfully!")


def view_employees():
    print("\nView Employee Details")
    speaker.Speak("View Employee Details")
    speaker.Speak("Enter the name, role, or employee ID to search: ")
    employee = input("Enter the name, role, or employee ID to search: ").strip()
    found = False
    results = []
    try:
        with open(data_file, "r") as file:
            for line in file:
                if employee.isdigit():
                    if extract_emp_id(line) == employee:
                        results.append(f"{line.strip()}")
                        found = True
                else:
                    if employee.lower() in line.lower():
                        results.append(f"{line.strip()}")
                        found = True
        if found:
            print("\nEmployee Details are:\n")
            speaker.Speak("Employee Details are:")
            for result in results:
                print(result)
                speaker.Speak(result)

        else:
            print(f"No details found for {employee}.")
            speaker.Speak(f"No details found for {employee}.")

    except FileNotFoundError:
        print("No data file found. Save something first!")
        speaker.Speak("No data file found. Save something first!")

def update_employee():
    print("\nUpdate Employee Details")
    speaker.Speak("Update Employee Details")
    while True:
        speaker.Speak("Enter the Employee ID to update: ")
        emp_id = input("Enter the Employee ID to update: ").strip()
        updated_lines = []
        found = False
        try:
            with open(data_file, "r") as file:
                for line in file:
                    if extract_emp_id(line) == emp_id:
                        print(f"\nFound: {line.strip()}\n")
                        speaker.Speak(f"Found: {line.strip()}")
                        while True:
                            speaker.Speak("New name: ")
                            name = input("New name: ").title().strip()
                            if is_valid_text(name):
                                break
                            else:
                                print("Name should not contain numbers or special characters.")
                                speaker.Speak("Name should not contain numbers or special characters.")

                        while True:
                            speaker.Speak("New role: ")
                            role = input("New role: ").title().strip()
                            if is_valid_text(role):
                                break
                            else:
                                print("Role should not contain numbers or special characters.")
                                speaker.Speak("Role should not contain numbers or special characters.")

                        try:
                            while True:
                                speaker.Speak("New salary: ")
                                salary = input("New salary: ").strip()
                                if salary.isdigit():
                                    break
                                else:
                                    print("Salary should be a valid number.")
                                    speaker.Speak("Salary should be a valid number.")

                        except ValueError:
                            print("Please enter a valid number for salary.")
                            speaker.Speak("Please enter a valid number for salary.")
                            return
                        
                        updated_line = f"The Employee name is: {name} | His/Her Role: {role} | Salary: Rs. {salary} | Employee ID: {emp_id}\n"
                        updated_lines.append(updated_line)
                        found = True
                    else:
                        updated_lines.append(line)

            if found:
                with open(data_file, "w") as file:
                    file.writelines(updated_lines)
                print("\nEmployee details updated successfully!")
                speaker.Speak("Employee details updated successfully!")
                break
            else:
                print("No employee found with that ID.")
                speaker.Speak("No employee found with that ID.")

        except FileNotFoundError:
            print("No data file found. Add some employees first!")
            speaker.Speak("No data file found. Add some employees first!")
            break


def delete_employee():
    print("\nDelete Employee")
    speaker.Speak("Delete Employee")
    while True:
        speaker.Speak("Enter the Employee ID to delete: ")
        emp_id = input("Enter the Employee ID to delete: ").strip()
        updated_lines = []
        found = False
        speaker.Speak("Are you sure? Type 'yes' to proceed: ")
        confirm = input("Are you sure? Type 'yes' to proceed: ").lower()
        if confirm != "yes":
            print("Action cancelled.")
            speaker.Speak("Action cancelled.")
            return
        else:
            with open(data_file, "r") as file:
                for line in file:
                    if extract_emp_id(line) == emp_id:
                        speaker.Speak("Deleting")
                        print(f"Deleting: {line.strip()}")
                        found = True
                        continue
                    if line.strip():
                        updated_lines.append(line.strip())

            if found:
                with open(data_file, "w") as file:
                    file.writelines("\n".join(updated_lines))
                print("\nEmployee deleted successfully!")
                speaker.Speak("Employee deleted successfully!")
                break
            else:
                print("No employee found with that ID.")
                speaker.Speak("No employee found with that ID.")


def run_employees_program():
    print("\nWelcome to the Employee Management System!")
    speaker.Speak("Welcome to the Employee Management System!")
    while True:
      print("\n---- MENU ----\n1️. Add Employee\n2️. View All Employees\n3️. View Employee\n4️. Update Employee\n5️. Delete Employee\n6️. Exit")
      choice = input("Choose an option: ").lower().strip()
      if "add" in choice or "1" in choice:
          add_employee()

      elif "all" in choice or "2" in choice:
        try:
            with open(data_file, "r") as file:
                speaker.Speak("All Employees:")
                print("\nAll Employees:\n")
                print(file.read())

        except FileNotFoundError:
            print("No data file found. Add employees first!")
            speaker.Speak("No data file found. Add employees first!")

      elif "view" in choice or "3" in choice:
          view_employees()

      elif "update" in choice or "4" in choice:
        update_employee()

      elif "delete" in choice or "5" in choice:
        delete_employee()

      elif "exit" in choice or "6" in choice:
          print("\nGoodbye! Have a productive day!\n")
          speaker.Speak("Goodbye! Have a productive day!")
          break
      
      else:
          print("Invalid choice. Please say 'add', 'view all', 'view employee', 'update', 'delete' or 'exit'.\n")
          speaker.Speak("Invalid choice. Please say 'add', 'view all', 'view employee', 'update', 'delete' or 'exit'.\n")


def process_command():
    
    command = take_command().lower()

    if "list" in command:
      print("Available websites:")
      for site in websites:
          print(f"- {site.capitalize()}")
      speaker.Speak(f"{len(websites)} websites available. Please type one.")

    elif "news" in command:
        news()
    
    elif "shutdown" in command:
       speaker.speak("Shutting down the computer")
       print("Shutting down the computer")
       time.sleep(2)
       os.system("shutdown /s /t 0")

    elif "restart" in command:
       speaker.speak("Restarting the computer")
       print("Restarting the computer")
       time.sleep(2)
       os. system("shutdown /r /t 0")

    elif "logout" in command:
       speaker.speak("Logging out of the computer")
       print("Logging out of the computer")
       time.sleep(2)
       os.system("shutdown /l")

    elif any(site in command for site in websites):
        for site in websites:
            if site in command:
                speaker.Speak(f"Opening {site}")
                print(f"Opening {site.capitalize()}")
                webbrowser.open(websites[site])
                break

    elif "password" in command or "credential" in command:
        run_credential_program()

    elif "employee" in command or "manage" in command:
        run_employees_program()

    else:
       open_ai(command)


if __name__ == "__main__":
  while True:
    if "hey" in take_command().lower():
      speaker.Speak("Yes, I am Listening")
      print("Yes, I am Listening")
      process_command()

    else:
       print("Waiting for the wake word!")
       continue
