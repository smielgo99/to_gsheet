#!/usr/bin/env python
# -*- coding: latin-1 -*-
import xml.etree.ElementTree as ET
import sys

def extract_data(file_in):
	tree = ET.parse(file_in)
	root = tree.getroot()
	US_list = []



	for item in root.iter('item'):
		title = item.find('title').text
		link = item.find('link').text
		status = item.find('status').text
		fixVersion = item.find('fixVersion').text
		sprints=[]

		
		
		customfields = item.find('customfields')
		for customfield in customfields:
			if customfield.attrib.get('id') == 'customfield_11000':
				customfieldvalues = customfield.find('customfieldvalues')
				for child in customfieldvalues:
					sprints.append(child.text)
		
		# print title
		# print link
		# print status
		# print fixVersion
		# print sprints
		# print format_to_gdocs(link, title)

		
		
		for sprint in sprints:
			print sprint
			us = UserStory(format_to_gdocs(link, title), status, sprint, fixVersion)
			us.getUS()
			print "---"
			US_list.append(us)

		

def format_to_gdocs(link, title):
	return("=HYPERLINK(\" " + link + ";\" "+ title + "\")")
	

class UserStory:

	def __init__(self, hyperlink, status, sprint, fixVersion):
		self.hyperlink = hyperlink
		self.status = status
		self.sprint = sprint
		self.fixVersion = fixVersion

	def getUS(self):
		print self.hyperlink
		print self.status
		print self.sprint
		print self.fixVersion


# def create_release_notes(file_in, file_out, platform, version):
# 	tree = ET.parse(file_in)
# 	root = tree.getroot()
	
	
# 	known_issues_list = []
# 	bug_list =[]
# 	user_story_list = []
# 	feature_list = []
# 	improvement_list = []
# 	task_list = []
# 	sub_task_list = []
# 	sub_bug_list = []


# 	for item in root.iter('item'):
# 		status = item.find('status').text
# 		issue_type = item.find('type').text
# 		issue_type = item.find('type').text


# 		if not(status=='Resolved' or status=='Closed'):
# 			'''es una known issue no se distingue por tipo '''
# 			known_issues_list.append(item)
# 		else:
# 			if issue_type == "Bug":				
# 				bug_list.append(item)
# 			elif issue_type == "User Story":
# 				user_story_list.append(item)
# 			elif issue_type == "Improvement":
# 				improvement_list.append(item)
# 			elif issue_type == "New Feature":
# 				feature_list.append(item)
# 			elif issue_type == "Task":
# 				task_list.append(item)	
# 			elif issue_type == "Sub-task":
# 				sub_task_list.append(item)	
# 			elif issue_type == "Sub-Bug":
# 				sub_bug_list.append(item)	



# 	fo = open(file_out,'w')
# 	add_header(platform, version, fo)

# 	parse_item_to_html_rrnn(known_issues_list, "Known Issues", fo)
# 	parse_item_to_html_rrnn(bug_list, "Bugs", fo)
# 	parse_item_to_html_rrnn(sub_bug_list, "Sub-Bug", fo)
# 	parse_item_to_html_rrnn(user_story_list, "User Story", fo)
# 	parse_item_to_html_rrnn(improvement_list, "Improvement", fo)
# 	parse_item_to_html_rrnn(feature_list, "New Feature", fo)
# 	parse_item_to_html_rrnn(task_list, "Task", fo)
# 	parse_item_to_html_rrnn(sub_task_list, "Sub-Task", fo)

# 	fo.write(BODY_END)
# 	fo.close()

# def parse_item_to_html_rrnn(item_list, jira_issue_type, f_out):
	
# 	if len(item_list) != 0:
# 		f_out.write(TAG_H2_INI + jira_issue_type + TAG_H2_END + "\n")

# 		f_out.write(TAG_UL_INI)

# 		for item in item_list:

# 			f_out.seek(0, 2)
# 		   	f_out.write(item_to_html(item))
# 		f_out.write(TAG_UL_END)




# def add_header(platform, version, f_out):
# 	f_out.seek(0, 2)

# 	header = 'Release Notes - TUGO ' + platform + ' - Release ' + version + TAG_H1_END +'\n'
# 	f_out.write(BODY_INI + header)

# def item_to_html(item):

# 	title = item.find('title').text.encode("cp1252")
# 	link = item.find('link').text
# 	key = item.find('key').text
# 	print key
# 	entrada = ITEM_INI + link + TAG_END + key + ITEM_END + title + TAG_IL_END +'\n'
	
# 	return entrada



if __name__ == '__main__':
    '''
      argumentos: file_in, file_out, platform, version
    '''
    if len(sys.argv) == 2:
     	file_in = sys.argv[1]
      	
      

      	extract_data(file_in)
    else:
      	print "Numero de parametros erroneo"
      	print "argumentos: file_in"

