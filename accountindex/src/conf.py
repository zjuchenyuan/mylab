# coding=utf-8

APP_KEY = '3055924094'
APP_SECRET = 'b6b6d43c54e5a69f1b1db53510d64c10'
CALLBACK_URL = 'http://local.host/callback'

BUSINESS_TOKEN = (u'2.00VOpbvCyNKigBaa66e6d97b0Ndtsr', 1390113079)

HTTP_HOST = '127.0.0.1:80'

#cooperator sina weibo"
CO_APP_KEY = '1547264682'
CO_APP_SECRET = 'bad08151c2e95a73ac217c02cd1a646d'
CO_CALLBACK_URL = 'http://cooperator.iwommaster.com/callbackV3.do?forcelogin=true'
SERVER_ADDR = 'http://cooperator.iwommaster.com'
ACCESS_TOKEN = [u'2.00le6_hCyNKigBb1546d7fddCemfQE', 1890497200]

REPOST_TASK = 'reposts'
COMMENT_TASK = 'comments'

TASK_API_ARG = {
    REPOST_TASK:('statuses__repost_timeline', 'reposts'),
    COMMENT_TASK: ('comments__show', 'comments'),
}

TASKLIST_TABLE = 'tasklist'
ACCOUNT_TWEET_TABLE = 'account_tweet'
ACCOUNT_GROWTH_TABLE = 'account_growth'
DIRECTAT_TABLE = 'direct_at'
EXPOSURE_TALBE = 'tweet_exposure'
INTERACT_TABLE = 'interact_tweet_'
FANS_TABLE = 'fans_'
FRIENDS_TABLE = 'Weibo_User_Profile'
RELATION_TABLE = 'Weibo_User_Relationship'
FANS_TREND = 'fans_trend'
FANS_ACTIVITY_TABLE = 'fans_activity'
REPORT_TABLE = 'report'
ACCOUNT_LAB = 'account_lab'
ORI_TWEETS = 'original_tweets'
WORD_DICT = 'word_dict'

TOP_LIMIT = 1.0 * 10 ** 4

OP_MAIL_From = 'nolan.liu@cicdata.com'
OP_MAIL_Tos = ['nolan.liu@cicdata.com']
OP_MAIL_SBUJECT ='[accountindex_error]'

QUESTION_KEYWORDS = u"请问,咨询,求助,怎么办,我想问,什么办法,怎么治疗,是不是,哪里,为什么,有没有,提问".split(',')

USER_FIELDS = ('id', 'screen_name', 'name', 'province', 'city', 'location', 'description', \
                'url', 'profile_image_url', 'profile_url', 'domain', 'weihao', 'gender', \
                'followers_count', 'friends_count', 'statuses_count','favourites_count', \
                'created_at', 'following', 'allow_all_act_msg', \
                'geo_enabled', 'verified', 'verified_type', 'remark', 'allow_all_comment', \
                'avatar_large', 'avatar_hd', 'verified_reason', 'follow_me', 'online_status', 'bi_followers_count', 'lang',
                )

PROB=0.85
