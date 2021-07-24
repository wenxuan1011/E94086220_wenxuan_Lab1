#!/usr/bin/env python
# coding: utf-8

# In[1]:


#撰寫 class
class Nine_Coins:
    def __init__(self,num):  #initialize
        self.num=num  #將輸入的數設為 self.num
        self.binary='{:09b}'.format(self.num)  #將輸入的數轉為二進位制
        #令 self.state 為 HT 組合的字串
        self.state=str(self.binary)  #令二進位的值為字串
        self.state=self.state.replace('0','H')  #將'0'改為'H'
        self.state=self.state.replace('1','T')  #將'1'改為'T'
    
    #宣告 toss function
    def toss(self):
        import random  #引用 random module
        self.num=random.randint(0,511)  #將 self.num 改為 0~511 間的任一數
        #因 elf.num 被改變，故要重新宣告 self.binary 和 self.state
        self.binary='{:09b}'.format(self.num)
        self.state=str(self.binary)
        self.state=self.state.replace('0','H')
        self.state=self.state.replace('1','T')
    
    #引用 __repr__ 印出 self.state
    def __repr__(self):
        return f'Nine_Coins: {self.state}'
    
    #引用 __str__ 印出 self.binary 和 self.num
    def __str__(self):
        return f'binary:{self.binary} and decimal:{self.num}'


# In[ ]:




