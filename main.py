class MakeClass:
    def __init__(self, name, assignments, teacher, room, time):
        self.assignments = assignments
        self.name = name
        self.teacher = teacher
        self.time = time
        self.room = room

    def getAssignments(self):
        allAssignments = ""
        for i in self.assignments:
            allAssignments += "\n" + i[0] + " is due on " + i[1] + " at " + i[2]
        return allAssignments

    def organizeForFile(self):
        return f'Class: {self.name}\nTeacher: {self.teacher}\nRoom: {self.room}\nTime: {self.time}\nAssignments: {self.getAssignments()}\n\n'

    def __str__(self):
        return f'{self.name} is taught by {self.teacher} in room {self.room} at {self.time}'


def writeToFile(data):
    with open('classes.txt', 'w') as file:
        for i in data:
            file.write(i.organizeForFile())
        file.close()


classes = []

if __name__ == "__main__":
    print("would you like to import you classes from classes.txt? (y/n)")
    if input() == "y":
        combined = ""
        assignmentsImported = []
        with open('classes.txt', 'r') as file:
            wholeFile = ""
            howManyClasses = 0
            for line in file.readlines():
                if line.__contains__("Class: "):
                    howManyClasses += 1
                wholeFile += line
            # print(wholeFile + "\n" + str(howManyClasses))
            for i in range(howManyClasses):
                combined += wholeFile.split("Class: ")[i + 1].split("Assignments: ")[0]
                print(wholeFile.split("Assignments: ")[1])
                nameImported = combined.split("\n")[0]
                teacherImported = combined.split("\n")[1].split("Teacher:")[1]
                roomImported = combined.split("\n")[2].split("Room:")[1]
                timeImported = combined.split("\n")[3].split("Time:")[1]
                classes.append(
                    MakeClass(nameImported, assignmentsImported, teacherImported, roomImported, timeImported))
                combined = ""
                assignmentsImported = []
    while True:
        print("would you like to add a class? (y/n)")
        if input() == "y":
            className = input("What is the name of the class? ")
            teacher = input("Who is the teacher? ")
            room = input("What room is the class in? ")
            time = input("What time is the class? ")
            assignments = []
            assignmentNum = int(input("How many assignments do you have? "))
            for i in range(assignmentNum):
                assignmentName = input("What is the name of the assignment? ")
                dueDate = input("What is the due date? ")
                dueTime = input("What is the due time? ")
                assignments.append((assignmentName, dueDate, dueTime))

            classes.append(MakeClass(className, assignments, teacher, room, time))
            print("Class added!")
            writeToFile(classes)
        else:
            print("would you like to see your classes? (y/n)")
            if input() == "y":
                for i in classes:
                    print(i)
            else:
                print("would you like to see your next due assignment? (y/n)")
                if input() == "y":
                    for i in classes:
                        print(i.getAssignments())
