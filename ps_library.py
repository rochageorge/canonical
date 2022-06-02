
"""Library for downloading and getting statistics from a debian repository"""

import os
import gzip
import urllib.request

from collections import Counter
from bs4 import BeautifulSoup

url='http://ftp.uk.debian.org/debian/dists/stable/main/'

arch_list = ['amd64', 'arm64', 'armel', 'armhf', 'i386', 'mips64el', 'mipsel', 'ppc64el', 's390x', 'udeb-all',
 'udeb-amd64', 'udeb-arm64', 'udeb-armel', 'udeb-armhf', 'udeb-i386', 'udeb-mips64el', 'udeb-mipsel',
 'udeb-ppc64el', 'udeb-s390x']


def get_links(url:str, arch:str='')->list:
    """
        This function gets the links from the repository.
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


def download_file(url:str, files:list):
    """
        This function downloads the files fetched in the function get_links
    Arguments:
        url: repository url from where the files will be downloaded
        files: list of links
    """
    print('Downloading the files...')
    
    path=os.getcwd()+'/'
    
    for file in files:

        url_download = url+file
        
        # checks if the file already exists
        if os.path.exists(path+file) == False:
            
            print('Get: '+file)
            urllib.request.urlretrieve(url_download, path+file)
        
        elif os.path.exists(path+file):
            
            print('File already exists: '+file)

            
def get_statistics(arch:str)->list:
    """
        This function creates the statistics from the architecture
    Arguments:
        arch: architecture passed as argument in the CLI
    """
    
    ct1=os.getcwd()+'/'+f'Contents-{arch}.gz'    

    packages_list=[]

    with gzip.open(ct1,'r') as buffer:        
        for line in buffer:        
            packages_list.append(str(line).split(' ')[-1])
            buffer.flush()

    counts = Counter(packages_list)    
    
    top_N=counts.most_common(10)
    
    return top_N


def print_statistics(top:tuple):
    """
        This function prints the statistics
    Arguments:
        top: a tuple with the package and the number of occurrences
    """
    
    print('\n')
    
    for i in range(0,len(top)):
    
        pack=top[i][0].replace("\\n'",'').ljust(60)
        count=top[i][1]

        print(f'{i+1}. {pack} \t{count}')

            
def main(arch:str):
    """
        This function orchestrates the workflow
    Arguments:
        arch: architecture passed as argument in the CLI
    """
        
    if arch in arch_list:
        
        files_download=[f'Contents-{arch}.gz']
        
        download_file(url,files_download)  
        
        topN=get_statistics(arch)
        
        print_statistics(topN)
        
    else:
        print('Architecure {} not found.\n'.format(arch))
        print(f'Architectures available: {arch_list} \n'.replace("\'","").replace('[','').replace(']',''))
        
        
    
