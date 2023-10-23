#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct. 23rd, 2023
# This program asks the user to enter a number between 1 and 12
# and tells the user what month that integer represents


def main():
    # Get the user's number
    month = input("Enter an integer between 1 and 12: ")

    # Using match case, find what month the user's number represents
    match month:
        case "1":
            print("1 represents January")

        case "2":
            print("2 represents February")

        case "3":
            print("3 represents March")

        case "4":
            print("4 represents April")

        case "5":
            print("5 represents May")

        case "6":
            print("6 represents June")

        case "7":
            print("7 represents July")

        case "8":
            print("8 represents August")

        case "9":
            print("9 represents September")

        case "10":
            print("10 represents October")

        case "11":
            print("11 represents November")

        case "12":
            print("12 represents December")

        case _:
            print("Enter a valid number.")


if __name__ == "__main__":
    main()
