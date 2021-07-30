from datetime import datetime
from collections import OrderedDict

def solution(test_date_dic):

    def get_day_from_date(date):
        form = "%Y-%m-%d"
        datetime_str = datetime.strptime(date, form).strftime('%A')[:3]
        
        return datetime_str
        
    
    def get_days_count(date_obj):
        
        days_obj = OrderedDict()
        days_obj["Mon"] = 0
        days_obj["Tue"] = 0
        days_obj["Wed"] = 0
        days_obj["Thu"] = 0
        days_obj["Fri"] = 0
        days_obj["Sat"] = 0
        days_obj["Sun"] = 0
        
        
        if len(date_obj.keys()) < 2:
            return "AVAILABLE DATA INSUFFICIENT"
            
        for date,counter in date_obj.items():
            days_obj[get_day_from_date(date)] += counter
            
        if days_obj["Sun"] == 0 or days_obj["Mon"] == 0:
            return "ENTRIES FOR MONDAY/SUNDAY NOT AVAILABLE"
        
        keys = list(days_obj.keys())
        
        # print(days_obj)
        
        i = 0
        while i < len(keys):
            if days_obj[keys[i]] == 0:
                
                #CHECK FOR ALL MISSING DAYS VALUES
                j = i + 1
                while days_obj[keys[j]] == 0:
                    j += 1
                
                #FINDING THE APPROPRIATE INTERVAL    
                interval = (days_obj[keys[j]] - days_obj[keys[i-1]])//(j - i  + 1)
        
                #ADDING THE INTERVAL TO THE MISSING ENTRIES
                for k in range(i, j+1):
                    days_obj[keys[k]] = days_obj[keys[k-1]] + interval
                
                i = j
                    
            i  += 1
                
        return dict(days_obj)
            
    res = get_days_count(test_date_dic)
    return res


if __name__ == "__main__":
    
    test_date_dic = {
        "2020-01-01" : 6,
        "2020-01-04" : 12,
        "2020-01-07" : 4,
        "2020-01-03" : 10,
        "2020-01-05" : 14,
        "2020-01-06" : 2
        
    }
    
    def printer(days):
        for key, val in days.items():
            print(key + ": " + str(val))
            
    res = solution(test_date_dic)
    
    printer(res)
    


    