#!/bin/sh

#1. use the testcase.rb file we have in this directory.
cat testcase.rb
#2. get radamsa to mutate it, then store that into a new file.
for i in `seq -w 1 99999`
do
       	cat testcase.rb | radamsa > test-cases/testcase-$i.rb
	echo "----------------------------------------------------"
	timeout 10s ruby -W0 test-cases/testcase-$i.rb > /dev/null
	if [ $? -eq 0 ]
	then
		rm testcases/testcase-$i.rb
	fi

done
