s_name = ["ram", "shyam", "gopal", "krishna", "Kung"]
s_percent = [48, 45, 90, 20, 60, 55]


def marksheet(s_name: list, s_percent: list) -> dict:
    """This function takes two lists (i.e. student_names and
    student_percents) as arguments, uniquely filter student_names as
    well as student_percents greater than 50 and returns the dictionary
    with key as student_name and value as student_percent

    Args:
        s_name (list): list of student names
        s_percent (list): list of student percents

    Returns:
        dict: dictionary of s_name and s_percent
         in a key: value pair
    """
    required_student = []
    [required_student.append(name) for name in s_name if name not in required_student]
    percent_greater_than_50 = [percent for percent in s_percent if percent > 50]
    student_result = student_result = {
        student[0]: student[1]
        for student in zip(required_student, percent_greater_than_50)
    }
    return student_result


print(marksheet(s_name, s_percent))
