import pandas_datareader.data as web

class data_manager:
    
    def __init__(self,instruments, start_dt, end_dt, source='google'):
        self.raw_data = web.DataReader(instruments, source, start_dt, end_dt)
        self.items = list(self.raw_data.items) 
        
    def get_close(self, stock=False):
        if stock == False:
            return self.raw_data['Close']
        else:
            return self.raw_data['Close'][stock]