import ConfigParser
from bot import Bot

config = ConfigParser.RawConfigParser()
config.read('settings.cfg')

if __name__ == '__main__':
    bot = Bot(subreddit = config.get('reddit', 'subreddit'),  
              queryType = config.get('reddit', 'queryType'),
              timer = int(config.get('timer', 'seconds')),
              limit = int(config.get('reddit', 'limit')))
    bot.run()