#!/usr/bin/env python


# coding: utf-8

# In[16]:


#tuple

tuple_scoops = (3,1,4,1,5,9,2,6,5,4)


# A tuple is a list that is immutable, cannot be changed or modified as a list can.

#Examples are details like country names, etc.


# In[15]:

print(tuple_scoops)


# In[3]:


type(tuple_scoops)


# In[4]:


tuple[3]


# In[5]:


tuple_scoops[3]


# In[7]:


#sets narrow down only to the unique values contained within it. 


# In[9]:


daily_pints = {1,2,3}


print(daily_pints)


# In[10]:


type(daily_pints)


# In[13]:


pints_daily = {1,3,3,2,3,4,6,4,2,3,4}

print(pints_daily)


# In[41]:


mr_john_wick = {0,1,2,3}

mrs_jadie_wick = {4,5,6,7}


# In[19]:


print(mr_john_wick)


# In[23]:


print(mrs_jadie_wick)


# In[24]:


print(mr_john_wick | mrs_jadie_wick)
#this shows us the combined unique values across both sets 


# In[34]:


boy_wick = {8,9,10,0,1,2,3}


# In[35]:


print(boy_wick)


# In[27]:


print(mr_john_wick|mrs_jadie_wick|boy_wick)


# In[42]:


#ampersand shows what data values overlap across the different sets.

print(mr_john_wick & mrs_jadie_wick & boy_wick)


# In[43]:


print(mr_john_wick & boy_wick)


# In[44]:


#there is the subraction sign in sets which subtracts
#the unique values in the set at the right hand side.


# In[47]:


mr_john_wick = {0,1,2,3}
mrs_jadie_wick = {4,5,6,7}

print(mr_john_wick - mrs_jadie_wick)


# In[49]:


#if we swap the variable places, the values in 
#mrs_jadie_wick will become visible instead, having
#subtracted the values of john_wick.


# In[50]:


print(mrs_jadie_wick - mr_john_wick)


# In[51]:


#whereas this ^ shows values that are not in the two
#sets. So the value is either in set A or in set B


# In[52]:


print(mr_john_wick ^ mrs_jadie_wick)


# In[ ]:




