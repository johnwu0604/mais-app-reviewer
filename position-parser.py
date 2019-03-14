import pandas as pd

mapping = {
    'VP Finance': ['Question 0', 'Question 1'],
    'VP Events (Industry)': ['Question 2', 'Question 3', 'Question 4'],
    'VP Events (Community)': ['Question 5', 'Question 6', 'Question 7'],
    'VP Communications': ['Question 8', 'Question 9', 'Question 10'],
    'Academic Lecturer (2)': ['Question 11', 'Question 12', 'Question 13', 'Question 17'],
    'Technical Project Manager (2-4)': ['Question 14', 'Question 15', 'Question 16'] 
}

''' Creates and saves the relevant spreasheet '''
def createSpreadsheet(position, applications):
    sheet = applications.copy()
    # drop irrelevant questions
    for pos, questions in mapping.items():
        if pos != position:
            for q in questions:
                sheet.drop([q], axis=1, inplace=True)
    # drop all appliants not applying for specified position
    sheet.drop(sheet.loc[(sheet['First Choice']!=position) & (sheet['Second Choice']!=position) & (sheet['Third Choice']!=position)].index, inplace=True)
    sheet.to_csv('{}.csv'.format(position), index=False)

''' Main method '''
if __name__ == '__main__':
        
    # load applications
    apps = pd.read_csv('applications.csv')

    # create seperate spreadsheets for each app
    for key, value in mapping.items():
        createSpreadsheet(key, apps)

