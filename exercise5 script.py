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

#check dataframe
print swage

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
#Count number of females
Topfemales = 0
for female in Top10:
    Topfemales = Topfemales + 1 #(this part doesn't work)
list.count(Top10females)        
############question 3##############


