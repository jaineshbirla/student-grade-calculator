"""
Student Grade Calculator
------------------------
A beginner-friendly CLI application that takes student scores,
calculates average and letter grades, and provides performance feedback.
"""

def get_letter_grade(average):
    """Returns letter grade and evaluation based on percentage average."""
    if average >= 90:
        return "A", "Excellent performance! Keep up the great work."
    elif average >= 80:
        return "B", "Very Good! Strong understanding of concepts."
    elif average >= 70:
        return "C", "Good effort. Room for improvement in a few areas."
    elif average >= 60:
        return "D", "Passed, but needs additional study and revision."
    else:
        return "F", "Needs Significant Improvement. Consider reviewing core topics."


def main():
    print("=" * 45)
    print("      STUDENT GRADE CALCULATOR & TRACKER     ")
    print("=" * 45)

    student_name = input("Enter Student Name: ").strip()
    
    # Get total number of subjects
    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    subjects = {}
    print("\n--- Enter Subject Marks (out of 100) ---")
    
    for i in range(1, num_subjects + 1):
        subject_name = input(f"Subject {i} Name: ").strip() or f"Subject {i}"
        while True:
            try:
                score = float(input(f"Enter marks for {subject_name} (0 - 100): "))
                if 0 <= score <= 100:
                    subjects[subject_name] = score
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numerical marks.")

    # Calculations
    total_marks = sum(subjects.values())
    max_possible = num_subjects * 100
    average_percentage = total_marks / num_subjects
    letter_grade, feedback = get_letter_grade(average_percentage)

    # Output Summary
    print("\n" + "=" * 45)
    print(f"             REPORT CARD: {student_name.upper()}")
    print("=" * 45)
    for subject, mark in subjects.items():
        print(f" - {subject:<20}: {mark:.1f} / 100")
    print("-" * 45)
    print(f" Total Score      : {total_marks:.1f} / {max_possible}")
    print(f" Average Percentage: {average_percentage:.2f}%")
    print(f" Final Grade       : {letter_grade}")
    print(f" Feedback          : {feedback}")
    print("=" * 45)


if __name__ == "__main__":
    main()
