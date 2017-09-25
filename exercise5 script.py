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


############question 3##############