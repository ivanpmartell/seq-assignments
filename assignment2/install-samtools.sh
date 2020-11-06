#Install necessary libraries
sudo apt install zlib1g-dev
sudo apt-get install libncurses5-dev
sudo apt-get install libbz2-dev
sudo apt-get install liblzma-dev
sudo apt-get install libcurl4-gnutls-dev
#Download samtools and extract
wget https://github.com/samtools/samtools/releases/download/1.11/samtools-1.11.tar.bz2
bzip2 -d samtools-1.11.tar.bz2
tar -xvf samtools-1.11.tar
cd samtools-1.11/
#Install samtools
sudo ./configure
sudo make
sudo make install