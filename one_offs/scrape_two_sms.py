import os
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import requests
import pickle

schd = BlockingScheduler()

def get_sports_job_postings():
    """
    Takes in integer argument for last page of results to be included in list of results
    Returns 25 x (number of pages included) job postings off of TeamworkOnline.com with job title, organization, and link to job posting
    """
    # Gather HTML code from TeamworkOnline.com
    url = 'https://www.teamworkonline.com/jobs-in-sports'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, features='lxml')
    matches = soup.findAll(name='h3')
    orgs = soup.findAll(name='span', attrs={'class': 'icon-bullet__content icon-bullet__content--recent-job-card'})
    links = soup.findAll(name='a', attrs={'class': 'result-cta button button--wire'})
        
    # Create lists for job title, organization, and link to posting
    joblist = []
    orglist = []
    linklist = []
    for match in matches:
        joblist.append(match.text)
    
    for org in orgs:
        orglist.append(org.text)
        
    for link in links:
        linklist.append('https://www.teamworkonline.com/' + link.get('href'))

    # Eliminate certain responses since they're just ads for the site
    joblist = [x for x in joblist if x != 'Know when your application is reviewed.']
    joblist = [x for x in joblist if x != 'Teamwork Online Individual Resume and Profile Review']    
    orglist = [x for x in orglist if 'Sports Jobs in' not in x]

    # Create zipped list of all three data points
    all_list = [i + ' | ' + j + ' | ' + k for i, j, k in zip(joblist, orglist, linklist)]

    # Write master list to text file to compare each running with it to only print new jobs
    with open ('/Users/User/Desktop/falck_workspace/one_offs/other_files/two_jobs.txt', 'rb') as f:
        old_all_list = pickle.load(f)

    just_new = set(all_list) - set(old_all_list)
    too_many = 'Too many job postings...'

    # Check if the set of differences between the old set and new set is empty, then print only the differences
    isEmpty = (len(just_new) == 0)
    total_entry = []
    if isEmpty:
        total_entry += ['No new postings.']
    else:
        for entry in just_new:
            entrysplit = entry.split('|')
            post = '\n- ' + entrysplit[0] + ' at ' + entrysplit[1] + '\n'
            total_entry.append(post)
    
    # Turn list of all new jobs into one string
    return_string = ' '.join(total_entry)
      
    # Overwrite the old text file with new data so when it's run again, it only compares postings to the last time function was run
    with open('/Users/User/Desktop/falck_workspace/one_offs/other_files/two_jobs.txt', 'wb') as f:
        pickle.dump(all_list, f)

    if len(return_string)>1600:
        return too_many
    else:
        return return_string
    

if __name__ == "__main__":
    get_sports_job_postings()
