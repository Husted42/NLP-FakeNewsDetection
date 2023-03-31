# DataScience 

Date: 31/03/2023


Extract the zip file ('news_cleaned_2018_02_13.csv') to a directory/folder, and rename it to 'csvFile.csv'. 
Ensure that both the data and notebook pipeline are in the same directory/folder. 
Run the pipeline. 
Note that the running time may vary depending on the computer on which the pipeline is run.

csv files:
csvFile.csv: The original dataset from fake news corpus, renamed 
readyData.csv: The first 100k rows of csvFile.csv
Columns: 0, id, type, content, inserted_at, meta_description, source
cleanedNews.csv: Cleaned version of readyData.csv
Result of the preprocessing section
milReadyData.csv: The first 5 mio rows of csvFile.csv
milcleanedNews.csv: Cleaned version of milReadyData.csv 
Result of the preprocessing section 
Split of cleandNews.csv:
split80_train.csv
split10_test.csv
split10_val.csv
Split of milcleanedNews.csv:
milsplit80_train.csv 
milsplit10_test.csv 
milsplit10_val.csv 

Sections
Setup
Takes csvFile.csv and gives readyData.csv/milReadyData.csv with the different amount of rows, so it’s ready for cleaning.
Data overview 1
Data types and null count
Preprocessing
Takes the readyData.csv/milReadyData.csv through a pipeline that does: Stemming, tokenizing, and regex. And gives cleanedNews.csv/milcleanedNews.csv
Data overview 2
Most used words
Word appearances 
Ready data for the baseline model
Splitting the cleaned file into 80/10/10 randomly, so that we have one for training, test and validation. 
Word embedding
Label to binary
Data overview 3
Scatter Plot of data
Words in wordToVec
Barchart of balance
Baseline model
Logistic regression models on the split80_train.csv/split10_test.csv/split10_val.csv files. 
Metrics
Advanced model
Grid Search 
GradientBoostingClassifer on the milsplit80_train.csv/milsplit10_test.csv/milsplit10_val.csv files. 
LIAR dataset
