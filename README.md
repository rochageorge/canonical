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

I first read the instructions a few times to make sure I understood what was needed and then started thinking about possible solutions, which gave me the idea of using requests or BeautifulSoup for the html part, then maybe Regex for dealing with text. The CLI was something new. After getting a first understanding of the problem, I started setting some tasks to get myself in a path to develop the solution:

    1. Get the links from the main page using a html parser;
    2. Download the files;
    3. Create a simple CLI according to the specifications;
    4. Comment the code and organize the private repository;
    5. Develop a basic statistics solution and ask about the packages;
    6. Pack the repository;
    7. Double check everything and send.
    
Time spent on development: 14h
    
## Usage

First you will need to give permissions to the file and then execute the command to fetch data, download the file and create the statistics. You can choose the architectures from two options, passing an argument, example: ./package_statistics.py arm64 or ./package_statistics.py udeb-arm64.

    Architecture: amd64, udeb-amd64, arm64, udeb-arm64...
    
    1. source venv/bin/activate
    2. chmod +x package_statistics.py
    3. ./package_statistics.py <architecture>
    4. deactivate
    
Example-1:

    $./package_statistics.py udeb-amd64
    Downloading the files...
    Get: Contents-udeb-amd64.gz


    1. debian-installer/brltty-udeb                                 	373
    2. debian-installer/espeak-ng-data-udeb                         	292
    3. debian-installer/espeak-data-udeb                            	275
    4. debian-installer/sound-modules-5.10.0-10-amd64-di            	231
    5. debian-installer/sound-modules-5.10.0-13-amd64-di            	231
    6. debian-installer/nic-modules-5.10.0-10-amd64-di              	153
    7. debian-installer/nic-modules-5.10.0-13-amd64-di              	153
    8. debian-installer/nic-wireless-modules-5.10.0-10-amd64-di     	139
    9. debian-installer/nic-wireless-modules-5.10.0-13-amd64-di     	139
    10. debian-installer/libgdk-pixbuf-2.0-0-udeb                    	111
    
 Example-2:
    
    $ ./package_statistics.py amd64
    Downloading the files...
    Get: Contents-amd64.gz


    1. devel/piglit                                                 	51784
    2. science/esys-particle                                        	18015
    3. libdevel/libboost1.74-dev                                    	14333
    4. math/acl2-books                                              	12668
    5. golang/golang-1.15-src                                       	9015
    6. libdevel/liboce-modeling-dev                                 	7434
    7. net/zoneminder                                               	7002
    8. libdevel/paraview-dev                                        	6178
    9. kernel/linux-headers-5.10.0-13-amd64                         	6149
    10. kernel/linux-headers-5.10.0-10-amd64                         	6148
