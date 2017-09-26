###########question 1################
#load the dataset
import pandas
wages = pandas.read_csv("wages.csv")

#filter out columns of interest into a new dataframe
wages2 = wages[['gender', 'yearsExperience']].copy()

#drop duplicates from column 1 and 2
dwage=wages2.drop_duplicates(subset=['gender','yearsExperience'])

#sort columns
swage= dwage.sort_values(by=["gender", "yearsExperience"])

#write.csv
swage.to_csv('unique_gender_yearsExperience.csv', sep='\t')


####################question 2#################
#Limit to columns of interest
q2 = wages[['gender', 'yearsExperience', 'wage']].copy()
#sort by wage
sortedq2 = q2.sort_values(by=['wage'])
#select highest earner
Highest = sortedq2.tail(1)
#Print line for highest earner
print (Highest)
#select lowest earner
Lowest = sortedq2.head(1)
#Print line for lowest earner
print (Lowest)
#Find top 10 earners
Top10 = sortedq2.tail(10)

##Count number of females
#pulls out females from top 10
Topfemales=Top10.loc[Top10['gender'] == "female"]
#counts females in top 10
ctopfemale= Topfemales.gender.count()
print (ctopfemale)

############question 3##############
wages12 = wages[wages.yearsSchool==12] #selects people with 12 years of school
min12 = min(wages12.wage) #minimum wage of people with 12 years of school
wages16 = wages[wages.yearsSchool==16] #selects people with 16 years of school
min16 = min(wages16.wage) #minimum wage of people with 16 years of school
print(min16-min12)
