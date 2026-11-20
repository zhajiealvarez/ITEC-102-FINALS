[17] MODULES

A Python module is a file or library that contains code we can use in a program.
Modules help us add features without writing everything ourselves.

This folder documents the three modules used in the Speed Typing Test:
1. Faker
2. Time
3. Statistics

----------------------------------------
1. FAKER MODULE
----------------------------------------

Purpose:
Faker is an external Python library that generates fake but realistic data.

How it is used in the Speed Typing Test:
Faker generates a sentence for the player to type. The number of words changes
depending on the selected difficulty.

Code:
    import faker

    fake = faker.Faker()
    sentence = fake.sentence(nb_words=6)

Explanation:
- import faker loads the Faker library.
- faker.Faker() creates a Faker object.
- fake.sentence() generates a sentence.
- nb_words sets the approximate number of words in the sentence.

Other uses:
Faker can generate sample names, email addresses, phone numbers, dates,
addresses, and other kinds of test data.

Installation:
    pip install faker

----------------------------------------
2. TIME MODULE
----------------------------------------

Purpose:
Time is a built-in Python module used for time-related operations.

How it is used in the Speed Typing Test:
It records when the player starts and finishes typing. The program subtracts
the starting time from the ending time to calculate how many seconds were used.

Code:
    import time

    start = time.time()
    # The player types here
    end = time.time()

    elapsed = end - start

Explanation:
- time.time() returns the current time as a timestamp.
- start stores the time before typing.
- end stores the time after typing.
- elapsed stores the total time taken.

Other uses:
The time module can also create delays with time.sleep(), work with timestamps,
and measure how long parts of a program take to run.

Installation:
No installation is needed. The time module is included with Python.

----------------------------------------
3. STATISTICS MODULE
----------------------------------------

Purpose:
Statistics is a built-in Python module used for statistical calculations.

How it is used in the Speed Typing Test:
It calculates the average WPM from the scores saved during the current session.

Code:
    import statistics

    scores = [30, 40, 50]
    average = statistics.mean(scores)

Explanation:
- statistics.mean() calculates the arithmetic average.
- It adds the values and divides their total by the number of values.
- In this example, the average is 40 WPM.

Other uses:
The module also provides functions for finding the median, mode, and standard
deviation of numerical data.

Installation:
No installation is needed. The statistics module is included with Python.

----------------------------------------
SUMMARY
----------------------------------------

Faker      - Generates the sentences used in the typing test.
Time       - Measures how long the player takes to type.
Statistics - Calculates the average WPM from the saved scores.
