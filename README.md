## INSTRUCTIONS 

Debian uses *deb packages to deploy and upgrade software. The packages are stored in repositories and each repository contains the so called "Contents index". The format of that file is well described here: https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices

 

Your task is to develop a python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them. An example output could be:

 

#### ./package_statistics.py amd64
 

    <package name 1>    <number of files>
    <package name 2>    <number of files>
          ...                  ...
    <package name 10>   <number of files>
 
   

You can use the following Debian mirror:   http://ftp.uk.debian.org/debian/dists/stable/main/. 

Please try to follow Python's best practices in your solution. Hint: there are tools that can help you verify your code is compliant. In-line comments are appreciated.

Please do your work in a local Git repository. Your repo should contain a README that explains your thought process and approach to the problem, and roughly how much time you spent on the exercise. When you are finished, create a tar.gz of your repo and submit it to the link included in this email. Please do not make the repository publicly available.
 
Note: We are interested not only in quality code, but also in seeing your approach to the problem and how you organize your work.

## Approach

I first read the instructions a few times to make sure I understood what was needed and then started thinking about possible solutions, which gave me the idea of using requests or BeautifulSoup for the html part, then Regex for dealing with text. I remembered this because I have done a bit of webscrapping in the past when implementing a module in my internship. The CLI was something new. After getting a first understanding of the problem, I started setting some tasks to get myself in a path to develop the solution:

    1. Get the links from the main page using a html parser;
    2. Download the files;
    3. Create a simple CLI according to the specifications;
    4. Comment the code and organize the private repository;
    5. Develop a basic statistics solution and ask about the packages;
    6. Pack the repository;
    7. Double check everything and send.
    
Time spent on development: 14h
    
## Usage

First you will need to give permissions to the file and then execute the command to fetch the data, download the file and create the statistics. You can choose the architectures from two options, passing an argument, example: ./package_statistics.py arm64 or ./package_statistics.py udeb-arm64.

    Options: amd64, udeb-amd64, arm64, udeb-arm64...
    1. chmod +x package_statistics.py;
    2. execute ./package_statistics.py <architecture>.
