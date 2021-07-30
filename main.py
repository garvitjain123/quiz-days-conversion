import unittest

#IMPORTING SOLUTION FUNCTION
from solution import solution

class Test(unittest.TestCase):
    
    def test_sunday_and_monday_only(self):
        
        test_date_dic = {
            "2020-01-05" : 14,
            "2020-01-06" : 2
        }
        
        test_res = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14}
        
        result = solution(test_date_dic)
        
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
        
    def test_sunday_and_monday_reverse(self):
        
        test_date_dic = {
            "2020-01-05" : 2,
            "2020-01-06" : 14
        }
        
        test_res = {'Mon': 14, 'Tue': 12, 'Wed': 10, 'Thu': 8, 'Fri': 6, 'Sat': 4, 'Sun': 2}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
        
        
    def test_insufficient_data(self):
        
        test_date_dic = {
            "2020-01-05" : 14
        }
        
        result = solution(test_date_dic)
        self.assertEqual(result, "AVAILABLE DATA INSUFFICIENT")
        
    def test_one_days_missing(self):
        
        test_date_dic = {
            "2020-01-01" : 6,
            "2020-01-04" : 12,
            "2020-01-07" : 4,
            "2020-01-03" : 10,
            "2020-01-05" : 14,
            "2020-01-06" : 2
        }
        
        test_res = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
    
    def test_two_days_missing(self):
        
        test_date_dic = {
            "2020-01-01" : 6,
            "2020-01-04" : 12,
            "2020-01-07" : 4,
            "2020-01-05" : 14,
            "2020-01-06" : 2
        }
        
        test_res = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
            
    def test_three_days_missing(self):
    
        test_date_dic = {
            "2020-01-01" : 6,
            "2020-01-07" : 4,
            "2020-01-05" : 14,
            "2020-01-06" : 2
        }
        
        test_res = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
            
    def test_four_days_missing(self):
    
        test_date_dic = {
            "2020-01-01" : 6,
            "2020-01-05" : 14,
            "2020-01-06" : 2
        }
        
        test_res = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 'Fri': 10, 'Sat': 12, 'Sun': 14}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])

    def test_random_dates(self):
        
        test_date_dic = {
            "2021-09-22" : 55,
            "1971-01-01" : 22,
            "2000-05-15" : 12,
            "2021-08-01" : 90
        }
        
        test_res = {'Mon': 12, 'Tue': 33, 'Wed': 54, 'Thu': 38, 'Fri': 22,  'Sat': 56, 'Sun': 90}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
            
            
    def test_sunday_or_monday_not_available(self):
        
        test_date_dic = {
            "2021-09-22" : 55,
            "1971-01-01" : 22,
            "2000-05-15" : 12,
        }
        
        result = solution(test_date_dic)
        self.assertEqual(result, "ENTRIES FOR MONDAY/SUNDAY NOT AVAILABLE")
        
        
    def test_input_given(self):
        
        test_date_dic = {
            "2020-01-01": 4,
            "2020-01-02": 4,
            "2020-01-03": 6,
            "2020-01-04": 8,
            "2020-01-05": 2,
            "2020-01-06": -6,
            "2020-01-07": 2,
            "2020-01-08": -2,
        }
        
        test_res = {'Mon': -6, 'Thu': 4, 'Wed': 2, 'Tue': 2, 'Fri': 6, 'Sat': 8, 'Sun': 2}
        
        result = solution(test_date_dic)
        for item in result.keys():
            self.assertEqual(result[item],  test_res[item])
        
        
if __name__ == "__main__":
    unittest.main()
