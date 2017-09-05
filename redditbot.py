import praw
import config
import time
import re
import datetime
import os
import json


def bot_login():
	print_output("\nLogging in...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,			# Messy stuff at the beginning
			client_secret = config.client_secret,
			user_agent = "r/rotmg autoremoval bot")
	print_output("I've logged on!\n")

	return r


limit = 5
version = "v1.2"
Question_thread_goal = 50
Fame_train_goal = 10
Guild_recruitment_goal = 10
Lost_halls_goal = 10
Returning_player_goal = 10
boolean = 0

#Discords:

#[/r/rotmg discord](https://discord.gg/rotmg)

#[PitchOTMG](https://discord.gg/s5c8rKw)

#[Fame Train](https://discord.gg/pVGQe7g)

#[Tombs 24/7 (pitch but for tombs)](https://discord.gg/uupCfMc)

#[Public Lost Halls](https://discord.gg/q5zY3)

weekly_question_thread_link = "https://www.reddit.com/r/RotMG/6vmfh3" # Posted August 23th





# Changelog: 
# 
# v0.1 - Bot is able to reply to comments and posts. (8/16)
# v0.2 - Bot is able to reply to posts based on their title and content (8/17)
# v0.3 - Fixed bug regarding fame train section, added Guild Recruitment (8/17)
# v0.4 - Improved syntax for posts on the developer end, no change on user end (8/18)
# v0.5 - Bot no longer replies to the same post multiple times (8/18)
# v0.6 - Whitelist of users implemented (8/18)
# v0.7 - Whitlist actually works now (8/18)
# v0.8 - Added a significant number of cases, including temporary and miscellaneous (8/18)
# v0.9 - Bot sends a modmail when automod posts the weekly question thread (8/19)
# v1.0 - Enough cases have been added to declare the bot complete; there are no know bugs. (8/20)
# v1.1 - Added a !discords command to list all discords (8/27)
# v1.2 - All terminal output is now also written to a text file (9/1)
# v1.3 (CURRENT) - New !tag add command to tag posts with a custom string (9/4)
#
# PLANNED: 
# 
# v1.4 - !tag get command to display all the posts with a certain tag
# v1.5 - !help command to show all commands, including their aliases, and some info about the bot.
# v2.0 - Bot is able to reply to common comments on the weekly question Thread






# Main Function

def main(r, posts_replied_to):  # No idea why it needs r
	print_output("Start of a fresh run:")
	count = 0
	now = datetime.datetime.now()
	for submission in r.subreddit('rotmg').new(limit=limit): # For each of the submissions on r/rotmg/new, up to submission # limit...
		try:
		
			count = count + 1   # Numbering each of the submissions for easy reading in the terminal

			# Nasty set of if statements for each regex needing to be checked, very inneficient but it works
			# A demo with comments is below:

			# infractions = 0   # number of penalty points accumulated

			# matcher = re.search("Does",submission.title)    # Regex for the if statement, chenges every if statement

			# if(matcher != None):   # If the matcher found something in the body of the post
			# 	print_output("Success!")				# Debugger
			#	infractions = infractions + 10     # Add penalty points
			

			print_output("\n    " + str(count) + ": " + submission.title)
			author = submission.author    # Getting a reddit user object
			print_output("       Author: " + author.name)    # Gets the username of the reddit user



			if(author.name == "AutoModerator"):
				if(submission.id not in posts_replied_to):
					r.subreddit('rotmg').message('Automated WQT update message', 'Please update the relevant links for the new weekly question thread! Here is the '+
						'link: https://www.reddit.com/r/RotMG/%s' % submission.id)

					print_output("        I've sent a message to the mods! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")

					
				else:
					print_output_output("    I've already sent a modmail!")





			























			# Start of Question Thread Checker


			infractions = 0  	  

			matcher = re.search(".+\?",submission.title)   # Question mark at the end of the title
			if(matcher != None):
				infractions = infractions + 40
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 1")

			matcher = re.search("(?i)(which|what) (character|pet|weapon|character) (?:\w+ ?){0,4}"+
				" (max|feed|fuse|hatch|equip|buy|)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 50
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 2 \n")

			matcher = re.search("(?i)(how|what) (good|bad|terrible|awesome|amazing|okay)" +
			" (?:\w+ ?){0,5} (skull|robe|spell|helm|wand|bow|armor|UT|shield|trap|ring|ability)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 50 
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 3 \n")

			matcher = re.search("(?i)(^Questio(n|ns)|quick question)$",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 50
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 5 \n")


			matcher = re.search("(?i)Question (?:\w+ ?){0,4} (pet|pet stones|pets)",submission.selftext+submission.selftext)
			if(matcher != None):
				infractions = infractions + 50
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 6 \n")


			matcher = re.search("(?i)New player (?:\w+ ?){0,6} advice",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 50
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 8 \n")



			if(infractions >= Question_thread_goal and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):
				#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Question.** Please comment your question on the [stickied weekly question thread] (" +
						weekly_question_thread_link + ") instead of making a post on the subreddit, thank you! \n \n" +  
						"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")

					print_output("        I've left a weekly  question thread comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")

					
				else:
					print_output("    This post has already been replied to!")
									

			# End of Question Thread Checker


		














			# Start of Fame Train Checker

			infractions = 0

			matcher = re.search("(?i)Looking for (?:\w+ ?){0,4} \w+train discord",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 9 \n")




			matcher = re.search("(?i)(where|what) is (?:\w+ ?){0,4} (\w*train|\w*train discord)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 11 \n")

			matcher = re.search("(?i)what server (?:\w+ ?){0,4} \w*train",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 12 \n")

			if(infractions >= Fame_train_goal and author.name not in whitelisted_users):		
				if(submission.id not in posts_replied_to):
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Fame Train.** The Fame Train, previously located on the server EUN2, now moves around to whichever " + 
						"realm provides the best fpm (fame per minute). Their current location can be found in the #click-here-for-train channel of their discord: "+
						"https://discord.gg/sXRRQth. \n \n" +
						"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + " ^) ^| ^(Reply to leave feedback)")
					print_output("        I've left a fame train comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")

				else:
					print_output("    This post has already been replied to!")

			# End of Fame Train Checker


			












			# Start of Guild Recruitment Checker

			infractions = 0

			matcher = re.search("(?i)(Recruiting for)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 13 \n")

			matcher = re.search("(?i)Looking for (?:\w+ ?){0,3} guild",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 14 \n")

			matcher = re.search("(?i)Requirement (?:\w+ ?){0,4} (./8|fame)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 17 \n")

			matcher = re.search("(?i)recruitment post",submission.title)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 18 \n")


			if(infractions >= Guild_recruitment_goal and author.name not in whitelisted_users):	
				if(submission.id not in posts_replied_to):	
					#submission.remove(spam=False) (Not on a moderator account atm)

					submission.reply("**Autodetect: Guild Recruitment/Looking to join a guild.** Please post over at the " +
					"[Realmeye Forums'] (https://www.realmeye.com/forum/c/guilds) guild recruitment section instead of reddit, thanks! \n \n" +
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + " ^) ^| ^(Reply to leave feedback)")

					print_output("        I've left a guild recruitment comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")

			# End of Guild Recruitment Checker


			


















	#def checkMatch(matcher, infractions, infractionIncrement, debug):
	#	print_output("          Infractions: %s" % str(infractions))
	#	print_output("          Number: %s \n" % debug)
	#	return(infracions + infractionIncrement)

	# 	matcher = re.search("(?i)(where|what) (?:\w+ ?){0,4} (halls|lost|LH|lost Halls) (discord|invite)",submission.title)
	#	infractions = chechMatch(matcher, infractions, 10, 13)





			# Beginning of Lost Halls Checker

			infractions = 0

			matcher = re.search("(?i)(where|what) (?:\w+ ?){0,4} (halls|lost|LH|lost halls) (discord|invite)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 19 \n")


			matcher = re.search("(?i)Looking for (?:\w+ ?){0,4} (Lost|halls|LH|lost halls) (discord|invite)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 23 \n")

			matcher = re.search("(?i)(Link|invite) (?:\w+ ?){0,4} (halls|lost|LH|lost halls|lost hall) discord",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 23 \n")


			matcher = re.search("(?i)Discord link (?:\w+ ?){0,4} (halls|lost|LH|lost halls|lost hall)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 25 \n")

			matcher = re.search("(?i)(halls|lost|LH|lost halls|lost hall) discord?",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 27 \n")



			if(infractions >= Lost_halls_goal and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Lost Halls discord.** The Public Lost Halls discord can be found here:  https://discord.gg/EKFPG73. \n \n"
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					print_output("        I've left a Lost Halls comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")

			# End of Lost Halls Checker



















			# Beginning of Returning Player Checker

			infractions = 0

			matcher = re.search("(?i)(What|what's|anything) (changed|new)",submission.title)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 28 \n")



			if(infractions >= Returning_player_goal and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Returning Player. Please check the [Developement History]" + 
					"(https://www.realmeye.com/wiki/development-and-release-history) on Realmeye and all the [Official Posts](https://www.reddit.com" +
					"/r/RotMG/search?sort=new&restrict_sr=on&q=flair%3AOfficial%2BDeca) made " +
					"by Deca on reddit for what's changed since you've been gone! \n \n"
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					
					print_output("        I've left a Returning Player comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")


				# End of Returning Player Checker


















				# Beginning of Misc Checkers (No goal variable, no breaks inbetween)

			infractions = 0

			matcher = re.search("(?i)(is a scammer|are scammers|scammed me|mark" + 
				" (?:\w+ ?){0,7} as scammers|mark (?:\w+ ?){0,7} as a scammer)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 29 \n")

			matcher = re.search("(?i)(is a hacker|I recorded someone hacking)",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 31 \n")




			if(infractions >= 10 and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Scam Report.** This is not the place for any type of report - [send a support" + 
					" ticket to deca] (http://decagames.desk.com/customer/portal/emails/new) if you want to report him/them, or you can post to /r/RotMGDLS/.\n\n" +
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					
					print_output("        I've left a Misc Report comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")

				

			infractions = 0


			matcher = re.search("(?i)(?:\w+ ?){0,7}(awesome|good|terrible|amazing|incredible|worst|best|insane|average) roll",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 33 \n")



			if(infractions >= 10 and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Picture of rolls.** Rolls are a [banned post](https://www.reddit.com/r/RotMG/wiki/bannedposts) on the subreddit,"+
					" please delete your post or a mod will remove it shortly! \n \n"
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					
					print_output("        I've left a Picture of Rolls comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")

			infractions = 0



			matcher = re.search("(?i)Where (?:\w+ ?){0,5} deca support",submission.title+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 34 \n")

			matcher = re.search("(?i)Deca support link",submission.title)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 35 \n")

			matcher = re.search("(?i)Where (?:\w+ ?){0,5} deca support",submission.selftext+submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 36 \n")



			if(infractions >= 10 and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Looking for Deca Suport.** Deca support can be found here: " +
					" http://decagames.desk.com/customer/portal/emails/new \n \n"
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					
					print_output("        I've left a Deca Support comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")


			infractions = 0



			matcher = re.search("(?i)(trooms|\d+ trooms|\d+ treasure rooms|most treasure rooms|most trooms)",submission.title)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 38 \n")



			if(infractions >= 10):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Picture of trooms.** Troom pictures are a [banned post]" +
					"(https://www.reddit.com/r/RotMG/wiki/bannedposts) on the subreddit," +
					" please delete your post or a mod will remove it shortly! \n \n"
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					
					print_output("        I've left a Troom comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")


					# End of Misc Checkers


















					# Beginning of temp checkers (Only relevant for a short amount of time and after that they will be removed)

			Infractions = 0

			matcher = re.search("(?i)(Muledump\?|Muledump is broken|how do I fix muledump)",submission.title)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 39 \n")

			matcher = re.search("(?i)(Muledump is broken|how do I fix muledump)",submission.selftext)
			if(matcher != None):
				infractions = infractions + 10
				print_output("          Infractions: " + str(infractions))
				print_output("          Number: 40 \n")

			if(infractions >= 10 and author.name not in whitelisted_users):
				if(submission.id not in posts_replied_to):		
					#submission.remove(spam=False) (Not on a moderator account atm)
					submission.reply("**Autodetect: Complaint about muledump.** Muledump is currently broken because all the requests from every computer are going"+
					" through the same IP, causing deca to block that IP and thus block all the muledumps. This was not intentional, as stated by Krathan, " + 
					"and they are working on a fix.\n \n In the meantime, if you only want to see your fame bonuses, " +
					"[here is a tutorial for it] (https://www.reddit.com/r/RotMG/comments/6tyxr3/), credit to u/Dragonlogesh \n \n"
					"--- \n \n ^(I am a bot, and this action was performed automatically) ^| ^(Version: " + version + ") ^| ^(Reply to leave feedback)")
					
					print_output("        I've left a Muledump Complaint comment! \n")

					posts_replied_to.append(submission.id)

					with open ("posts_replied_to.txt", "a") as f:
						f.write(submission.id + "\n")
					
				else:
					print_output("    This post has already been replied to!")

					# End of temp checkers


					infractions = 0
		except:
			time.sleep(300)












	



			
	print_output("\n The time is " + str(now.hour) + ":" + str(now.minute) + "\n Finished! Sleeping for 5 minutes... \n")   # Gives the time that it finished at
	time.sleep(300)   # Sleeps for 5 minutes




def print_output(string):
	print(string)
	f = open("output.txt","a+")
	f.write(string)
	f.close()
	






def get_saved_posts():
	if not os.path.isfile("posts_replied_to.txt"):
		posts_replied_to = []
	else:
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")   # Entries in the list are divided by new lines
			posts_replied_to = list(filter(None, posts_replied_to))  # Dunno what this does, it works though

	return posts_replied_to


def get_whitelisted_users():
	if not os.path.isfile("whitelisted_users.txt"):
		whitelisted_users = []
	else:
		with open("whitelisted_users.txt", "r") as f:
			whitelisted_users = f.read()
			whitelisted_users = whitelisted_users.split("\n")
			whitelisted_users = list(filter(None, whitelisted_users))

	return whitelisted_users


posts_replied_to = get_saved_posts()

r = bot_login()  # Not sure what this does either honestly, but it works
posts_replied_to = get_saved_posts()		# Creating lists from .txt files for use above
whitelisted_users = get_whitelisted_users()

#r.subreddit('rotmg').message('test', 'Sorry about this ping, I had to make sure that the bot worked. \n \n - bot tybug')
#print_output("It worked?")

while True:
	main(r, posts_replied_to)   # Runs the main function cotninuously when redditbot.py is run




#   Notes for myself:
#	
#	reddit.subreddit(subreddit).message(title, body)
#   submission.selftext = body of a text post, empty line for link posts
#   submission.author = author of a post
#   submission.remove(spam=False) = removes a post
#   re.search(pattern, string)
#	submission.title = title of a post
#	comment.reply("I am a cat") = how to reply to a comment
#	print_outputnow.year, now.month, now.day, now.hour, now.minute, now.second
# 			2015 		5		  6 	    8 		  53 		  40
