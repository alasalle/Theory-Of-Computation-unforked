import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# Read HTML file
html_file = open(filename, 'r')
source_code = html_file.read() 


# Set up regex
matches = re.findall(r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&;\/\/=]*)", source_code)


# Find links using regex, save in list called 'matches'


# Check matches, print results
# Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'

answer_data = list()
with open('answers.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
      for link in row:
        answer_data.append(link)

# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print(result)