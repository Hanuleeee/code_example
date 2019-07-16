
# coding: utf-8

# In[3]:


def cal_upper(price):
    increment = price* 0.3
    upper_price = price+increment
    return upper_price

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price- decrement
    return lower_price

author = "pystock"

def run():
    print(cal_upper(100000))
    print(cal_lower(10000))
    print(__name__)
    
if __name__ == '__main__':
    run()
    
