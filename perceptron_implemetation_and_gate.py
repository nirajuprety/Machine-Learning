#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[7]:


np.version.version


# In[19]:


def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0


# In[ ]:





# In[20]:


#design Perceptron model
#x is inputs w is weights and b is for bias
def perceptronModel(x, w, b):
    #(w1x1+w2x2+w3x3+........+wnxn) + b
    v = np.dot(w, x) + b
    #checks either the v is greater than  0 or not
    y = unitStep(v)
    return y


# In[ ]:





# In[10]:


#at initial we take weights as w1=0, w2=0 and let bias b = 0.5(we can take any value)
def AND_logicFunction(x):
    w = np.array([0, 0])
    b = 0.5
    return perceptronModel(x, w, b)


# In[11]:


#simply making the input data set for percetron model
test1 = np.array([0, 0])
test2 = np.array([0, 1])
test3 = np.array([1, 0])
test4 = np.array([1, 1])


# In[24]:


print("AND({}, {}) = {}".format(0, 0, AND_logicFunction(test1)))
print("AND({}, {}) = {}".format(0, 1, AND_logicFunction(test2)))
print("AND({}, {}) = {}".format(1, 0, AND_logicFunction(test3)))
print("AND({}, {}) = {}".format(1, 1, AND_logicFunction(test4)))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




