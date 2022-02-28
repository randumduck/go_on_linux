#!/bin/bash
echo "Go Installation version go1.17.7"
echo -e "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n"
mkdir /root/GOO
cd /root/GOO
wget https://go.dev/dl/go1.17.7.linux-amd64.tar.gz
tar -C /usr/local/ -xzf go1.17.7.linux-amd64.tar.gz
echo "#go variables" >> ~/.bashrc
echo "export GOPATH=/root/go-workspace" >> ~/.bashrc
echo "export GOROOT=/usr/local/go" >> ~/.bashrc
echo "PATH=$PATH:$GOROOT/bin/:$GOPATH/bin" >> ~/.bashrc

source ~/.bashrc
go version
