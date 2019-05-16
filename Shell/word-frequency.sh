# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt|xargs|sed "s/ /\n/g"|sort -r|uniq -c|sort -r|awk '{print $2" "$1}'