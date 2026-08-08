print("Lisa's Study Tracker!")

import pandas as pd
import os
from datetime import datetime
import time

filename = "study_sessions.csv"
goal_file = "goals.csv"

if not os.path.exists(filename):
    df = pd.DataFrame(columns=[
        "Date",
        "Activity",
        "Minutes",
        "Notes"
    ])
    df.to_csv(filename, index=False)

if not os.path.exists(goal_file):
    df = pd.DataFrame(columns=[
        "Goal",
        "Status"
    ])
    df.to_csv(goal_file, index=False)

def add_session():
    activity = input("What are you working on? (Reading/Writing/Grading/Other):")

    minutes = input("How long?")

    notes = input("Anything to remember?")

    date = datetime.now().strftime("%Y-%m-%d")

    new_session = pd.DataFrame([{
        "Date": date,
        "Activity": activity,
        "Minutes": minutes,
        "Notes": notes }])

    df = pd.read_csv(filename)

    df = pd.concat([df, new_session], ignore_index=True)

    df.to_csv(filename, index=False)

    print("Session saved!")


def view_sessions():
    df = pd.read_csv(filename)

    print("\nYour Study Sessions:")
    print(df)

def study_summary():
    df = pd.read_csv(filename)

    total_minutes = df["Minutes"].astype(int).sum()

    print("\nStudy Summary:")
    print("Total study time:", total_minutes, "minutes")
    print("Total study time:", round(total_minutes / 60, 2), "hours")

    print("\nTime by activity:")
    print(df.groupby("Activity")["Minutes"].sum())

def add_goal():
    goal = input("What is your goal? ")

    new_goal = pd.DataFrame([{
        "Goal": goal,
        "Status": "Not Completed"
    }])

    df = pd.read_csv(goal_file)

    df = pd.concat([df, new_goal], ignore_index=True)

    df.to_csv(goal_file, index=False)

    print("Goal added!")

def view_goals():
    df = pd.read_csv(goal_file)

    print("\nYour Research Goals:")
    print(df)

def complete_goal():
    df = pd.read_csv(goal_file)

    print("\nYour Research Goals:")
    print(df)

    goal_number = int(input("Which goal did you complete? "))

    df.loc[goal_number, "Status"] = "Completed"

    df.to_csv(goal_file, index=False)

    print("Goal updated!")

def start_timer():
    minutes = int(input("How many minutes do you want to study? "))

    seconds = minutes * 60

    print("Timer started!")

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60

        print(f"{mins}:{secs:02d}", end="\r")

        time.sleep(1)

        seconds -= 1

    print("\nStudy session complete!")

while True:
    print("\nWhat would you like to do?")
    print("1. Add study session")
    print("2. View sessions")
    print("3. Start study timer")
    print("4. View study summary")
    print("5. Add goal")
    print("6. View goals")
    print("7. Complete goal")
    print("8. Exit")

    choice = input("Choose an option:")

    if choice == "1":
        add_session()

    elif choice == "2":
        view_sessions()

    elif choice == "3":
        start_timer()
        save = input("Would you like to save this session? (y/n):")
        if save.lower() == "y":
            add_session()

    elif choice == "4":
        study_summary()

    elif choice == "5":
        add_goal()

    elif choice == "6":
        view_goals()

    elif choice == "7":
        complete_goal()

    elif choice == "8":
        print("See you later!")
        break

    else:
        print("Please choose an option.")
