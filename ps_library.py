
"""Library for downloading and getting statistics from a debian repository"""

import os
import random
import urllib.request

from bs4 import BeautifulSoup

url='http://ftp.uk.debian.org/debian/dists/stable/main/'

def get_links(url:str, arch:str='')->list:
    """
        This function gets the links from the repository, used as a helper function for recursion in get_path().
    Arguments:
        url: repository url from where the files will be downloaded
        arch: architecture passed as argument in the CLI
    Returns:
        list: list of links from the url
    """
    
    # downloads the html page
    with urllib.request.urlopen(url) as response:
           raw_html = response.read()

    soup = BeautifulSoup(raw_html, 'html.parser')
    
    link_list=[]
    
    # fetch the links to folders/files in the page
    for link in soup.find_all('a'):
        
        if arch in link.get('href'):
            link_list.append(link.get('href'))
            
    return link_list


def get_path(url:str, arch:str='')->list:
    """
        This function gets the links from the repository, using a helper function to fetch all links that are not folders and uses recursion to fetch the links inside this lower level. (get the files inside a folder, that is inside another folder)
    Arguments:
        url: repository url from where the files will be downloaded
        arch: architecture passed as argument in the CLI
    Returns:
        list: nested list of links from the url, links from folders in the url, which can be other folders
    """
    
    link_list=get_links(url, arch)
    
    file_list=[]
    
    for link in link_list:
        
        # finds the links inside the folders recursively
        if link[-1]=='/' and link[-3:]!='../':
            file_list.append(get_path(url+link))
        
        # appends the links to a list
        elif link[-1]!='/':
            file_list.append(url+link)
            
    return file_list


def get_clean_links(url:str, arch:str)->list:
    """
        This function gets the links from get_path() and reduces it to a single list of links to files, eliminating the complexy of list of lists of lists of lists of lists...
    Arguments:
        url: repository url from where the files will be downloaded
        arch: architecture passed as argument in the CLI
    Returns:
        list: list of links from the url
    """
    
    print('Fetching data for {}...'.format(arch))
    
    res=get_path(url,arch)
    
    # checks if the architecture existes within the links
    if len(res)!=0:
    
        # transforms the list of lists of lists in a single string without unecessary characters/levels
        new_list=str(res).replace('[','').replace(']','').replace('\'','').replace(' ','').replace(url,'')
        files=new_list.split(',')    
    
        return files
    
    else:
        
        return res

    
def make_folders(url:str, files:list):
    """
        This function creates the folder structure, it was designed to be used in threaded execution, so the files in a lower level could be downloaded without needing to wait for the upper level to be downloaded and created.
    Arguments:
        url: repository url from where the files will be downloaded
        files: list of links to create the folder's structure
    """
    
    path='/home/jack/Documents/Github/canonical-technical-assessment/downloads/'
    
    print('Creating the folders...')
    
    for file in files:
                
        # removes the file from the path, to create the folders
        remove=file.split('/')[-1]
        mydir=file.replace(remove,'')
        dir_path=path+mydir
        os.makedirs(dir_path, exist_ok = True)
        
        
def download_file(url:str, files:list):
    """
        This function downloads the files fetched in the function get_clean_links
    Arguments:
        url: repository url from where the files will be downloaded
        files: list of links to create the files in folder's structure
    """
    
    print('Downloading the files...')
    
    # this is where the files will be saved
    path='/home/jack/Documents/Github/canonical-technical-assessment/downloads/'
    
    for file in files:

        url_download = url+file
        
        # checks if the file already exists
        if os.path.exists(path+file) == False:
            
            print('Get: '+file)
            urllib.request.urlretrieve(url_download, path+file)
        
        elif os.path.exists(path+file):
            
            print('File already exists: '+file)
            

def main(arch:str):
    """
        This function orchestrates the workflow, first calls get_clean_links(), which calls the get_path() that calls get_links(), after verifying if the input achitecture exists, creates the folders, makes the download and creates the statistics.
    Arguments:
        arch: architecture passed as argument in the CLI
    """ 
    
    files=get_clean_links(url, arch)
    
    if len(files)==0:
        print('Architecture {} not found.'.format(arch))
    
    else:
        make_folders(url,files)    
        download_file(url,files)  
