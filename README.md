# The goal of the bot is to detect various types of posts that aren't allowed on r/rotmg and remove them. This is done through searching (regex) for keywords in the title and then leaving a comment on the post if it has a certain keyword(s)

# There is a second bot, reddit-discord-bot, that searches comments for commands instead of posts. I could have done it in one file but that would require multithreading (I think) and I don't really know/want to learn how to do that. So, multiple files it is for now.

# Everything in the code should be commented fairly well. If it isn't please leave a comment/pull request so I can make it more clear!
