# quiz-days-conversion
This is a test project for converting a given dictionary of dates(in string format) to dictionary equivalent days dictionary

Installation Needed:
    
        1. Python 3.7+
        2. unittest module(available with python-3.7+)
        3. Collections module(available with python-3.7+)


This program takes the input of dates(Entries for the dates representing "Monday" and "Sunday" are essential for code completion) and outputs the days with the associated counter is provided.

**Example Input(AS PROVIDED):**

    dates = { "2020-01-01" : 6, "2020-01-04" : 12, "2020-01-07" : 4, "2020-01-03" : 10, "2020-01-05" : 14, "2020-01-06" : 2 }

**Example Output:**
  
    res = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14}
  
If there are values that are missing in between the days, the program will try to find the interval by doing the following things:
  1. Calculating the number of consecutive days with missing entries.
  2. The program will then sum the extremes and divide the sum by the no of missing entries to get an interval.
  3. It will return the dictionary to the calling function if all missing entries are replaced and no missing are present.
 
 
 **Example Input(AS PROVIDED):**
  
    dates = { "2020-01-01": 4, "2020-01-02": 4, "2020-01-03": 6, "2020-01-04": 8, "2020-01-05": 2, "2020-01-06": -6, "2020-01-07": 2, "2020-01-08": -2 }

**Example Output:**
    
    res = {'Mon': -6, 'Thu': 4, 'Wed': 2, 'Tue': 2, 'Fri': 6, 'Sat': 8, 'Sun': 2}
