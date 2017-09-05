import praw
import time
import rotmg_discords_bot_config
import re
import os
import json


def bot_login():
	print_output("Loggin in...")
	r = praw.Reddit(username = rotmg_discords_bot_config.username,
			password = rotmg_discords_bot_config.password,
			client_id = rotmg_discords_bot_config.client_id,			# Messy stuff at the beginning, r = reddit
			client_secret = rotmg_discords_bot_config.client_secret,
			user_agent = "tybug's discord bot")
	print_output("I've logged on!")

	return r


version = "v1.1"


#	Changelog:
#	v0.1 (CURRENT) - Bot can reply to comments based on their content (8/19)
#	v1.0 - Bot monitors all new comments and replies to commands (8/20)
#   v1.1 - All terminal output is now also written to a text file (9/1)
#
#	PLANNED
#
#	v2.0 - Bot responds to comments with multiple commands only once, with multiple discord links in that comment


def main(r, comments_replied_to):

	if not os.path.isfile("dictionary.json"):
		d = {}   #Initializing dictionary
		f = open("dictionary.json",'w')
		json.dump(d, f)   # Creating file 
		f.close()

	count = 0

	for comment in r.subreddit('rotmg').stream.comments():
		try:
			print_output(comment.body + "\n\nhttps://www.reddit.com/r/RotMG/comments/%s//%s \n---- \n " %(comment.submission, comment.id))
		
			try:
				words = comment.body.split(" ")
				index = words.index("!tag")

				if(index >= 0):

					command = words[index + 1]
					tag = words[index + 2]

					with open("dictionary.json", 'r') as f:
						d = json.load(f)

					key = "%s" %comment.submission

					if key in d and command == "add":

						print_output("I got to the first statement!")
						# It prints this statement

						# List of submissions mapping to a list of tags
						d[key].append(tag)

						# But not this one...So line 59 (the one two above this) is the one that's breaking things.
						
						print_output("\nI've added the tag %s to the post %s, but it was already in the dictionary\n\n" %(tag, comment.submission))

						
						if(comment.id not in comments_replied_to):
							comment.reply("I've added the tag %s to the post https://www.reddit.com/r/RotMG/comments/%s" %(tag, comment.submission))
							with open ("comments_replied_to.txt", "a") as f:
								f.write(comment.id + "\n")



					if key not in d and command == "add":

						print_output("I got to the second statement!")

						d[key] = [tag]
						print_output("\nI've added the tag %s to the post %s, it wasn't in the dictionary \n\n" %(tag, comment.submission))
						
						if(comment.id not in comments_replied_to):
							comment.reply("I've added the tag %s to the post https://www.reddit.com/r/RotMG/comments/%s" %(tag, comment.submission))
							with open ("comments_replied_to.txt", "a") as f:
								f.write(comment.id + "\n")

					with open("dictionary.json",'w') as f:
						json.dump(d, f)

					
					
			except:
				pass

	 

			matcher = re.search("(?i)(!train|!fametrain)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("The Fame Train, previously located on the server EUN2, now moves around to whichever realm " + 
						"provides the best fpm (fame per minute). Their current location can be found in the #click-here-for-train channel of their discord: "+
						"https://discord.gg/sXRRQth.\n \n" +
						"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
						" and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f: 			# a = writing the file
					f.write(comment.id + "\n")
				count = count + 1
				print_output("--------------- \n \nFame Train discord comment has been left.\n ---------------")





			matcher = re.search("(?i)(!LH|!Lost Halls|!lost halls)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("The public Lost Halls discord pops LH for as many people as they can get, to ensure its completion." +
				" \n \n Their discord can be found here: https://discord.gg/yWASJqd \n \n" +
						"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
						" and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("Lost Halls discord comment has been left.")







			matcher = re.search("(?i)(!pitch|!PitchOTMG|!POTMG)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("Pitch is a shatters subscription system where you pay two life a week to gain access to shatters bought with that life." +
					"\n \n The Pitch discord can be found here: https://discord.gg/s5c8rKw \n \n" +
					"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					" and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("Pitch discord comment has been left.")
			





			matcher = re.search("(?i)(!r/rotmg|!rotmg|!r-rotmg)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("The official r/rotmg discord can be found here: https://discord.gg/rotmg \n \n" +
					"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					" and this action was performed automatically) ^| ^(Version: " + version + ") ^) ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("r/rotmg discord comment has been left.")






			matcher = re.search("(?i)(!support|!supportlink|!Deca Support)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("Deca support - used for unban requests, hacker reports, and a host of other things - can be found here: "+
					"http://decagames.desk.com/customer/portal/emails/new \n \n" +
					"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					" and this action was performed automatically) ^| ^(Version: " + version + " ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("Deca Support comment has been left.")



			matcher = re.search("(?i)(!bannedposts)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("The list of banned posts for the subreddit can be found here: https://www.reddit.com/r/RotMG/wiki/bannedposts \n \n" +
					"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					" and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("Deca Support comment has been left.")


			matcher = re.search("(?i)(!bluenoser)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("Blunosers guide, an incredibly helpful resource for new players, can be found here: http://bluenosersguide.weebly.com/ \n \n" +
					"--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					" and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("Bluenosers guide comment has been left.")


			matcher = re.search("(?i)(!discord)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("Here are links to all the discords: \n\nPitchOTMG: https://discord.gg/s5c8rKw \n\n" +
					"Official Subreddit Discord: https://discord.gg/rotmg \n\nPublic Lost Halls discord: https://discord.gg/yWASJqd \n\n"+
					"Fame Train Discord: https://discord.gg/sXRRQth \n\n--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					"and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("All discords comment has been left.")

			matcher = re.search("(?i)(!help|!commands)",comment.body)
			if(matcher != None and comment.id not in comments_replied_to):
				comment.reply("Here are links to all the discords: \n\nPitchOTMG: https://discord.gg/s5c8rKw \n\n" +
					"Official Subreddit Discord: https://discord.gg/rotmg \n\nPublic Lost Halls discord: https://discord.gg/yWASJqd \n\n"+
					"Fame Train Discord: https://discord.gg/sXRRQth \n\n--- \n \n ^(My creator is Tybug2) ^| ^(I am a bot," +
					"and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")
				count = count + 1
				print_output("All discords comment has been left.")




		except: 
			time.sleep(60)

def print_output(string):
	print(string)
	f = open("output_rotmg_discords_bot.txt","a+")
	f.write(string)
	f.close()	



def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:  # r = reading the file
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")   # Entries in the list are divided by new lines
			comments_replied_to = list(filter(None, comments_replied_to))  # Dunno what this does, it works though

	return comments_replied_to




r = bot_login() 
comments_replied_to = get_saved_comments()
while True:
	main(r, comments_replied_to)
