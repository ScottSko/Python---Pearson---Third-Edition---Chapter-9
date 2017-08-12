def main():

    course_room = {"CS101" : 3004, "CS102" : 4501, "CS103" : 6755, "NT110" : 1244, "CM241" : 1411}
    course_instructor = {"CS101" : "Haynes", "CS102" : "Alvarado", "CS103" : "Rich", "NT110" : "Burke", "CM241" : "Lee"}
    course_meeting = {"CS101" : "8:00 a.m.", "CS102" : "9:00 a.m.", "CS103" : "10:00 a.m.", "NT110" : "11:00 a.m.", "CM241" : "1:00 p.m."}

    get_info = input("Which course would you like information on? ")

    get_info_u = get_info.upper()

    if get_info_u in course_room and get_info_u in course_instructor and get_info_u in course_meeting:
        print("The room number is:", course_room[get_info_u])
        print("The Instructor is:", course_instructor[get_info_u])
        print("The class starts at:", course_meeting[get_info_u])
    else:
        print("That is not a valid course number.")

main()