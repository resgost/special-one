#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import time


# In[ ]:


time.sleep(35)


# In[3]:


file_path = r"C:\Users\thord\Downloads\special-one-main\special-one-main\predicciones.xlsm"
subprocess.run(["start", file_path], shell=True)

