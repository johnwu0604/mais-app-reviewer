import pandas as pd

mapping =  [
        {
            'position': 'VP Finance',
            'questions': [
                {
                    'id': 0,
                    'text': 'Do you have any previous experience within EUS? Or holding a previous VP Finance position at McGill? If so, which one?',
                },
                {
                    'id': 1,
                    'text': 'Do you have any previous experience working with finance and budgeting? Elaborate.',
                }
            ]
        },
        {
            'position': 'VP Events (Industry)',
            'questions': [
                {
                    'id': 2,
                    'text': 'Give an example of an event you have organized for a large audience - please feel free to link us to an event page or a website as well.',
                },
                {
                    'id': 3,
                    'text': 'What has been your favourite event in the Montreal AI community (including McGill AI events) and why?',
                },
                {
                    'id': 4,
                    'text': 'Describe what a successful AI hackathon looks like. What is the key to accomplishing this?',
                }
            ]
        },
        {
            'position': 'VP Events (Community)',
            'questions': [
                {
                    'id': 5,
                    'text': 'If you became VP Events for McGill AI, what McGill club would you collaborate with and why?',
                },
                {
                    'id': 6,
                    'text': 'What events should the McGill AI Society continue holding next year? What new events should we create? Why?',
                },
                {
                    'id': 7,
                    'text': 'The McGill AI Society has struggled in cultivating a strong AI community on campus. As VP Events (Community) of the McGill AI Society, what would you do?',
                }
            ]
        },
        {
            'position': 'VP Communications',
            'questions': [
                {
                    'id': 8,
                    'text': 'Provide us with a link to your design portfolio, or samples of graphic design. (Please feel free to attach anything that you feel is indicative of your current abilities, whether it be a a link to a social media platform you were responsible for maintaining, or a folder of graphics you’ve made in the past),',
                },
                {
                    'id': 9,
                    'text': 'Name three components of a successful marketing strategy. In your role as VP Comms for the McGill AI Society, how would you implement and ensure that these strategies are carried out?',
                },
                {
                    'id': 10,
                    'text': 'How would your past experience(s) prepare you for a VP Communications position with the McGill AI Society?',
                }
            ]
        },
        {
            'position': 'Academic Lecturer (2)',
            'questions': [
                {
                    'id': 11,
                    'text': 'Briefly describe your machine learning background',
                },
                {
                    'id': 12,
                    'text': 'Link us to materials that demonstrate your understanding of fundamental machine learning algorithms (this can be an ML project on github, a personal experiment, paper review, mathematical derivations, etc)',
                },
                {
                    'id': 13,
                    'text': 'Do you have experience hosting workshops or teaching others. If so, elaborate.',
                },
                {
                    'id': 17,
                    'text': 'Describe a field/area in machine learning that you are passionate about.'
                }
            ]
        },
        {
            'position': 'Technical Project Manager (2-4)',
            'questions': [
                {
                    'id': 14,
                    'text': 'Describe your journey on how you learned ML. How would you use this experience to mentor others?',
                },
                {
                    'id': 15,
                    'text': 'Have you ever managed a project. Describe in more detail about the process and result.',
                },
                {
                    'id': 16,
                    'text': 'Describe in detail an AI/ML project you have worked on. Explain your mathematical approach, discuss the libraries you used, and summarize the results. Attach a link to the project.',
                }
            ]
        }
    ]

''' Gets the user input on the position they want to review '''
def getPositionInput():
    text = '\nWhat position would you like to review (enter the number)? \n \n'
    for index, item in enumerate(mapping):
        text += '{}) {} \n'.format(index,item['position'])
    text += '\n'
    position_index = input(text)
    print('\n\n\n\nREVIEWING {} APPLICATIONS (Press ENTER to iterate to next application/question).... \n\n\n'.format(mapping[int(position_index)]['position'].upper()))
    return position_index

''' Main method '''
if __name__ == '__main__':

    # Get position to review
    position_index = getPositionInput()

    # load applications
    apps = pd.read_csv('{}.csv'.format(mapping[int(position_index)]['position']))

    # iterate through positions and view details
    input()
    for index, row in apps.iterrows():
        # Print basic info
        print('{} {} {} ({}) \n'.format(row['Name'], row['Year'], row['Faculty'], row['Degrees']).upper())
        input()

        # Print position choices
        print('First Choice: {} \nSecond Choice: {} \nSecond Choice: {} \n\n'.format(row['First Choice'], row['Second Choice'], row['Third Choice']))
        input()

        # Print questions
        for q in mapping[int(position_index)]['questions']:
            print('{}\n'.format(q['text']).upper())
            print('{}\n\n'.format(row['Question {}'.format(q['id'])]))
            input()

        # Print resume url only at the end so we take the time to read questions first
        print('Resume URL: {}\n\n\n'.format(row['Resume']))
        input()




