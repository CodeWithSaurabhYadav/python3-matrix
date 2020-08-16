#/usr/bin/bash

cp -rf matrix $PREFIX/bin
chmod 777 $PREFIX/bin/matrix
mv ../python3-matrix $PREFIX/share
cd $HOME
echo -e "\e[3;33mMatrix Is Sucessfully installed on Your System\nType matrix to run the martrix\e[0m"
echo -e "\e[2;31mYou need to run \e[2;34mpip install colored \e[0m\e[2;31mbefore you run the matrix\e[0m"
