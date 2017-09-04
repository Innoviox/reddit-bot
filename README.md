The goal of the bot is to detect various types of posts that aren't allowed on r/rotmg and remove them. This is done through searching (regex) for keywords in the title and then leaving a comment on the post if it has a certain keyword(s)

There is a second bot, reddit-discord-bot, that searches comments for commands instead of posts. I could have done it in one file but that would require multithreading (I think) and I don't really know/want to learn how to do that. So, multiple files it is for now.

Everything in the code should be commented fairly well. If it isn't please leave a comment/pull request so I can make it more clear!

In the beginning of redditbot.py where it references config.py, that is a separate file that I will not be uploading. Literally all it contains is my secret, client_id and username. I just have it separately so I can share redditbot.py and not have to worry about giving away the keys to my account.

redditbot.py won't comment on any post made by someone in the user_whitelist, but will still reply to comments with a command in them.

Changelogs can be found near the top of each bot's code.
