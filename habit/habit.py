class Habit:
    def __init__(self, habit_id, name, description, priority, frequency, startTime, endTime, isComplete = False):
        self.id = habit_id
        self.name = name
        self.description = description
        self.priority = priority
        self.frequency = frequency
        self.startTime = startTime
        self.endTime = endTime
        self.isComplete = isComplete
        self.elapsedTime = endTime - startTime
        self.streak = 0
        self. history = {"Highest streak":0}

    # If the habit has been complete, set it as True, increase the completeCount and the streak
    def set_isComplete(self):
        if not self.isComplete:
            self.isComplete = True
            self.streak += 1

    # If the user fail to complete their habit, we need to check first if this has been the highest streak in history, if so
    # store that in the history_dict and set the streak back to zero
    def fail_habits(self):
        self.isComplete = False

        if self.history["Highest streak"] < self.streak:
            self.history["Highest streak"] = self.streak

        self.streak = 0

    # Display the habit
    def __str__(self):
        return f"""
            ===== Habit Info =====
            
            Name: {self.name}
            Description: {self.description}
            Priority: {self.priority}
            Frequency: {self.frequency}
            Completed: {self.isComplete}
            Current Streak: {self.streak}
            Highest Streak: {self.history["Highest streak"]}
            """


    # When time comes to work with db
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS HABIT (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            priority INTEGER NOT NULL,
            Frequency INTEGER NOT NULL,
            startTime INTEGER NOT NULL,
            endTime INTEGER NOT NULL,
            ISComplete INTEGER NOT NULL,
            elapsedTime INTEGER NOT NULL,
            streak INTEGER NOT NULL"""

    def save_db(self):
        sql = """
            INSERT I N TO  HABIT (id, name, description, priotity, frequency, startime, endTime, IsComplete, elapsedTime, streak)
            VALUES (?, ?) 
            """
