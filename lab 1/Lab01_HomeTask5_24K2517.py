rules = {
    'IT Support': ('wifi', 'laptop', 'password', 'login'),
    'Finance': ('fee', 'challan', 'scholarship', 'payment'),
    'Academics': ('grade', 'transcript', 'course', 'attendance'),
    'Library': ('book', 'borrow', 'journal')
}

complaints = [
    ("wifi is not working in lab", "IT Support"),
    ("forgot my student login password", "IT Support"),
    ("where to submit semester fee challan", "Finance"),
    ("scholarship installment not received", "Finance"),
    ("want to register an elective course", "Academics"),
    ("need my semester transcript copy", "Academics"),
    ("how to borrow this book", "Library"),
    ("where is the lost and found office", "General Office")
]

def route(complaint, rules, fallback='General Office'):
    dept = fallback
    for key, value in rules.items():
        for word in value:
            if word.lower() in complaint.lower():
                return key
    return dept

def evaluate(*results, **info):
    print(f'Analyst: {info['analyst']}')
    print(f'Date: {info['date']}')
    correct = 0
    incorrect = 0
    for text, predicted, actual in results:
        print(f'Complaint: {text} \n Predicted: {predicted}\n Actual: {actual}\n----------------------')
        if predicted == actual:
            correct+=1
        else:
            incorrect+=1
    
    print(f'Correct Predictions: {correct} \n Incorrect Predictions: {incorrect}')


results = []
for text, actual in complaints:
    predicted = route(text, rules)
    results.append((text, predicted, actual))

evaluate(*results, analyst="Khadeejah", date="Fall 2026")
