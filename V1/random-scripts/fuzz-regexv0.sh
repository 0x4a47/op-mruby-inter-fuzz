#!/bin/sh

#1. use the testcase.rb file we have in this directory.
cat testcase.rb
#2. get radamsa to mutate it, then store that into a new file.
for i in `seq -w 1 99999`
do
	cat regex-case | radamsa -m ft | ruby regexp.rb
	echo "----------------------------------------------------"
done
