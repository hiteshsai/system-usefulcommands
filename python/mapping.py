import sys

file1 = open('ip.txt', 'r')
file2 = open('Hostname.txt', 'r')

line1=[x.strip() for x in list(file1)]
line2=[x.strip() for x in list(file2)]



dictionary = dict(zip(line1, line2))


for key, value in dictionary.items():
    print("- {  \"hostname\": ""\"%s\", \"visiblename\": ""\"%s\"}" % (key, value))
