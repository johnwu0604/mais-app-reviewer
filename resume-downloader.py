import pandas as pd
import requests
import os

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":

    # load applications
    apps = pd.read_csv('applications.csv')

    # make resumes directory
    resume_dir = 'resumes'
    if not os.path.exists(resume_dir):
        os.makedirs(resume_dir)

    # download resumes
    failed_resumes = []
    for index, row in apps.iterrows():
        name = row['Name']
        resume_url = row['Resume']
        print('Downloading resume for: {}'.format(name))
        if 'drive.google.com/file/d/' in resume_url and '/view' in resume_url:
            resume_id = resume_url.split('/d/')[1].split('/view')[0]
            destination = './{}/{}.pdf'.format(resume_dir, name)
            download_file_from_google_drive(resume_id, destination)
        elif '?id=' in resume_url:
            resume_id = resume_url.split('?id=')[1]
            destination = './{}/{}.pdf'.format(resume_dir, name)
            download_file_from_google_drive(resume_id, destination)
        else:
            failed_resumes.append(name)

    # print out the list of resumes that failed
    print('\n\nThe following resumes failed to download: {}'.format(failed_resumes))


    