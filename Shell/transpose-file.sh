# Read from the file file.txt and print its transposed content to stdout.
IFS=$'\n'

length=`head -1 file.txt|wc -w`

for c in `seq 1 $length`
do

cat file.txt|awk '{a='$c';printf("%s", $a);print ""}'|xargs

done