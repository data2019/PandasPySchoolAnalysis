#!/usr/bin/env python
# coding: utf-8

# # PyCity School Analysis
# 1. Charter school types show better performace than District School types in all the scores. 
# 2. Overall students are performing better in english between (80 to 84%), than math (76 to 84%)

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[2]:


#Calculate the total number of schools
total_schools = len(school_data)
#Calculate the total number of students
total_students = len(student_data)
#Calculate the total budget
total_buget = school_data['budget'].sum()
#Calculate the average math score
avg_math_score = student_data['math_score'].mean()
#Calculate the average reading score
avg_reading_score = student_data['reading_score'].mean()
#Calculate the overall passing rate (overall average score)
overall_avg_score = ((avg_math_score + avg_reading_score)/2)
#Calculate the percentage of students with a passing math score (70 or greater)
passsing_math_score = (student_data['math_score'] >= 70).sum()
percent_math_passing = (passsing_math_score/len(student_data['math_score']))*100
#Calculate the percentage of students with a passing reading score (70 or greater)
passsing_reading_score = (student_data['reading_score'] >= 70).sum()
percent_reading_passing = (passsing_reading_score/len(student_data['reading_score']))*100

#Create a dataframe to hold the above results
District_Summary_df = pd.DataFrame({'Total Schools' : [total_schools], 'Total Students' : [total_students], 'Total Budget' :[total_buget], 'Average Math Score' : [avg_math_score], 'Average Reading Score':[avg_reading_score], '% Passing Math' : [percent_math_passing], '% Passing Reading' :  [percent_reading_passing], '% Overall Passing Rate' : [overall_avg_score]})

District_Summary_df


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[3]:


#group by School Name
school_groups = school_data_complete.set_index('school_name').groupby(['school_name'])
#find School type
school_type = school_data.set_index('school_name')['type']
#Calculate total students in each school
total_student = school_groups['Student ID'].count()
#Calculate total budget in each school
school_total_budget = school_data.set_index('school_name')['budget']
#Calculate budget per student in each school
per_stu_budget = school_total_budget/school_data.set_index('school_name')['size']
#Calculate average math score
total_math_score = school_data_complete.groupby(['school_name'])['math_score'].sum()
avg_math = total_math_score/total_student
#Calculate average reading score
total_reading_score = school_data_complete.groupby(['school_name'])['reading_score'].sum()
avg_reading = total_reading_score/total_student
#Calculate math score >= 70
pass_math_score = school_data_complete[school_data_complete['math_score'] >= 70].groupby('school_name')['math_score'].count()
pass_math_percent = (pass_math_score/total_student)*100
##Calculate reading score >= 70
pass_reading_score = school_data_complete[school_data_complete['reading_score'] >= 70].groupby('school_name')['reading_score'].count()
pass_reading_percent = (pass_reading_score/total_student)*100
#Calculate overall passing rate
overall_reading_rate = (pass_math_percent + pass_reading_percent)/2

#Adding all the calculated columns in dataframe
school_summary_df = pd.DataFrame({'School Type' : school_type, 'Total Students' : total_student, 'Total School Budget' : total_buget, 'Per Student Budget' : per_stu_budget, 'Average Math Score' : avg_math, 'Average Reading Score' : avg_reading, '% Passing Math' : pass_math_percent, '% Passing Reading' : pass_reading_percent, '% Overall Passing Rate' : overall_reading_rate})
school_summary_df

#Sort and display the top five schools in overall passing rate
top_performing = school_summary_df.sort_values('% Overall Passing Rate', ascending = False)
top_performing.head()


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[4]:


#Sort and display the five worst-performing schools
top_performing = school_summary_df.sort_values('% Overall Passing Rate')
top_performing.head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[5]:


#Create dataframe to hold average math score
grade_math_score = pd.DataFrame()
#Calclulate average math score for 9th
grade_math_score['9th'] = school_data_complete[school_data_complete['grade'] == '9th'].groupby('school_name')['math_score'].mean()
#Calclulate average math score for 10th
grade_math_score['10th'] = school_data_complete[school_data_complete['grade'] == '10th'].groupby('school_name')['math_score'].mean()
#Calclulate average math score for 11th
grade_math_score['11th'] = school_data_complete[school_data_complete['grade'] == '11th'].groupby('school_name')['math_score'].mean()
#Calclulate average math score for 12th
grade_math_score['12th'] = school_data_complete[school_data_complete['grade'] == '12th'].groupby('school_name')['math_score'].mean()

#formatting by setting index name blank
grade_math_score.index.name = ''
grade_math_score


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[6]:


#Create dataframe to hold average reading score
grade_reading_score = pd.DataFrame()
#Calclulate average reading score for 9th
grade_reading_score['9th'] = school_data_complete[school_data_complete['grade'] == '9th'].groupby('school_name')['reading_score'].mean()
#Calclulate average reading score for 10th
grade_reading_score['10th'] = school_data_complete[school_data_complete['grade'] == '10th'].groupby('school_name')['reading_score'].mean()
#Calclulate average reading score for 11th
grade_reading_score['11th'] = school_data_complete[school_data_complete['grade'] == '11th'].groupby('school_name')['reading_score'].mean()
#Calclulate average reading score for 12th
grade_reading_score['12th'] = school_data_complete[school_data_complete['grade'] == '12th'].groupby('school_name')['reading_score'].mean()

#formatting by setting index name blank
grade_reading_score.index.name = ''
grade_reading_score


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[7]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[8]:


# create dataframe with needed columns
school_spending_ranges = school_summary_df.loc[:, ['Average Math Score',
                                  'Average Reading Score','% Passing Math',
                                  '% Passing Reading','% Overall Passing Rate']]

#Calculate average score based on spending_bins 
school_spending_ranges['Spending Ranges (Per Student)'] = pd.cut(school_summary_df['Per Student Budget'], spending_bins, labels = group_names)
school_spending_ranges = school_spending_ranges.groupby('Spending Ranges (Per Student)').mean()
school_spending_ranges


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[9]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[10]:


# create dataframe with needed columns
school_size_score = school_summary_df.loc[:, ['Average Math Score',
                                  'Average Reading Score','% Passing Math',
                                  '% Passing Reading','% Overall Passing Rate']]

#Calculate average score as per size_bins
school_size_score['School Size'] = pd.cut(school_summary_df['Total Students'], size_bins, labels = group_names)
school_size_score = school_size_score.groupby('School Size').mean()
school_size_score


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[11]:


# create dataframe with needed columns
scores_School_type = school_summary_df[['School Type','Average Math Score',
                                  'Average Reading Score','% Passing Math',
                                  '% Passing Reading','% Overall Passing Rate',]]
#create a group based on school type
scores_School_type = scores_School_type.groupby('School Type').mean()
scores_School_type


# In[ ]:




