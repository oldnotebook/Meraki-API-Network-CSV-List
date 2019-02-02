# This is for Python version 3.7.  Created by Nate Revello 2019 Jan 18

# Save the curl output to a file named "Network list.txt" in the same directory as this script
#user@host ~ $ curl -L -H 'X-Cisco-Meraki-API-Key: <your api key here>' -H 'Content-Type: application/json' -X GET 'https://api.meraki.com/api/v0/organizations/<your org id here>/networks'
# To run this script; open a CMD prompt, cd to the directory of the script and curl output saved as the "Network list.txt" file, then run 'py MerakiNetworkIDReformatScript.py'


import csv

input_file = open("Network list.txt","r") # open the file with the network list.
input_text = input_file.read()
#print(input_text) # to test input.
input_file.close() # close the input file since it's not needed anymore.
split_output = input_text.split("},{") # split the sections into a list
# print(split_output) # test output
#split_length = len(split_output) # get the number of sections in the list
#print(split_length) # output the number of entries/sections in the list.
#print(split_output[4]) # misc test for single entry output

clean_list = list() # create a new list for cleaned up text

headers = "id,organizationId,name,timeZone,tags,type,configTemplateId,disableMyMerakiCom,disableRemoteStatusPage\n" # set the headers.  \n is needed for a new line

file_open = "false" # set this to false
try:
	output_file = open("Meraki Network List.csv","w",newline="") # create output file.
	#output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	output_file.write(headers) # write the headers
except PermissionError:
	print("\n*** Output file is probably already open.  Please close the file (Meraki Network List.csv) and re-run. ***\n")
	file_open = "true" # set the variable if the exception/error occurs
	
if file_open == "false": # if the file is open, then the program won't go through the rest of the work.
	for line in split_output: # go through the list, one entry at a time. line = counter variable
		#print("line: ",line) # output the line as a test.
		#print(len(line)) # output the number of characters in that list entry.
		line = line.replace("{","") # remove {
		line = line.replace("}","") # remove }
		#print("after clean-up line: ",line) # output the line after any modifications.
		
		clean_list.append(line) #append the new line to the updated list (no curly braces).

		line_list = list() # create a new list for each line	
		line_list = line.split(',') # split each line into it's own list.
		#print("Number of list items: ",len(line_list)) # example of output: Number of list items:  8
		#print("line_list: ") 
		#print(line_list)# print out the split line list: 
		#print() # blank line for testing
		
		# create column variables.  blanked out for formatting/testing
		id = 'blank'
		organization_id = 'blank'
		name = 'blank'
		time_zone = 'blank'
		tags = 'blank'
		type = 'blank'
		config_template_id = 'blank'
		disable_my_meraki_com = 'blank'
		disable_remote_status_page = 'blank'
		
		csv_line = id+","+organization_id+","+name+","+time_zone+","+tags+","+type+","+config_template_id+","+disable_my_meraki_com+","+disable_remote_status_page # create the line / clear out variables for each new line
		#print("csv_line before splitting words: ",csv_line) # test output.  should just be commas
		#print() # blank line for testing
		
		for word in line_list: # go through the line since it's a set
			#print("word: ",word) # example output: word:  "id":"N_################"
			#print()
			word_list = list() # create a list for each "word" in the line.
			word_list = word.split(":")
			# print("word_list",word_list) # example output: word_list [['"id"', '"N_###################"']]
			
			if '"id"' in word_list:
				#split text and remove extra quotes
				#print("yes, 'id' is here")
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				id = word_list[1] # set the variable.
				#print("id value: ", word_list[1]) # this prints the second item in the list--which happens to be the value.  example output: id value:  N_#################
				#print() #blank line for testing
				#write value to variable to be written to csv line.
			if '"organizationId"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				organization_id = word_list[1] # set the variable.
				#print("organizationId value: ", word_list[1])
			if '"name"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				name = word_list[1] # set the variable.
				#print("name value: ", word_list[1])
			if '"timeZone"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				time_zone = word_list[1] # set the variable.
				#print("timeZone value: ", word_list[1])
			if '"tags"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				tags = word_list[1].strip() # set the variable and remove whitespace at the beginning and end.
				#print("tags value: ", word_list[1])
			if '"type"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				type = word_list[1] # set the variable.
				#print("type value: ", word_list[1])	
			if '"configTemplateId"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				config_template_id = word_list[1] # set the variable.
				#print("configTemplateId value: ", word_list[1])		
			if '"disableMyMerakiCom"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				disable_my_meraki_com = word_list[1] # set the variable.
				#print("disableMyMerakiCom value: ", word_list[1])		
			if '"disableRemoteStatusPage"' in word_list:
				word_list[1]=word_list[1].replace('"', "") # remove double quotes
				disable_remote_status_page = word_list[1] # set the variable.
				#print("disableRemoteStatusPage value: ", word_list[1])
		
		#print() # blank line for testing	
		csv_line = id+","+organization_id+","+name+","+time_zone+","+tags+","+type+","+config_template_id+","+disable_my_meraki_com+","+disable_remote_status_page+"\n" # create the line with updated variables.  Start a new line at the end of the line.
		#print("csv_line after splitting words: ",csv_line) # test output.  should just be commas
		#print() # blank line for testing
		#break # break out of the loop for testing.  AKA--if enabled it'll only go through one line.
		
		output_file.write(str(csv_line)) # write the line to the file
	output_file.close() # close the output file since it's not needed anymore.
	print("Complete")
#print(clean_list) # output the list as a verification
