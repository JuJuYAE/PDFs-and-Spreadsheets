#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[3]:


import csv


# In[4]:


#Open the file 


# In[5]:


data = open ("example.csv")


# In[6]:


data


# In[7]:


csv_data = csv.reader(data)


# In[8]:


data_lines = list(csv_data)


# In[14]:


data_lines[0]


# In[12]:


len(data_lines)


# In[15]:


for line in data_lines[:5] : 
    print(line)


# In[19]:


data_lines[10][3]


# In[22]:


file_to_output = open("to_save_file.csv",mode="w",newline = "")


# In[24]:


csv_writer = csv.writer(file_to_output, delimiter = ",")


# In[25]:


csv_writer.writerow(["a","b","c"])


# In[26]:


file_to_output.close()


# In[29]:


f = open("to_save_file.csv", mode = "a" , newline = "")


# In[30]:


csv_writer = csv.writer(f)


# In[31]:


csv_writer.writerow(["1","2","3"])


# In[32]:


f.close()


# In[38]:


get_ipython().system('pip install PyPDF2')
import PyPDF2


# In[39]:


f = open("Working_Business_proposal.pdf", "rb")


# In[1]:


import PyPDF2


# In[2]:


f = open("Working_Business_proposal.pdf", "rb")


# In[5]:


pdf_reader = PyPDF2.PdfReader(f)


# In[10]:


len(pdf_reader.pages)


# In[11]:


page_number = 0 
page_one = pdf_reader.pages[0]


# In[12]:


page_one_text = page_one.extract_text()


# In[13]:


page_one_text


# In[24]:


f.close()


# In[25]:


f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)


# In[26]:


page_number = 0
page_one = pdf_reader.pages[0]


# In[27]:


pdf_writer = PyPDF2.PdfWriter()


# In[28]:


pdf_writer.add_page(page_one);


# In[29]:


pdf_output = open("Some_New_Doc.pdf","wb")


# In[30]:


pdf_writer.write(pdf_output)


# In[21]:


f.close()


# In[31]:


f = open ("Working_Business_Proposal.pdf", "rb")



pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for num in range (len(pdf_reader.pages)) : 
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())


# In[39]:


pdf_text[4]


# In[ ]:




