monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Feb"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Hex", "Not a valid key"))
print(monthConversions.get(input("Enter month: ")))
