#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="fulop.barna",
    password="hatyatya",
    like_per_day=320,
    comments_per_day=0,
    tag_list=['bleachmyfilm', 'lookslikefilm', 'madewild', 'welivetoexplore', 'innaturewetrust', 'campingcollective', 'mountainstories', 'roomtheplanet', 
    		'moodygrams', 'photohunted', 'headvisuals', 'wondermore', 'lightroom_md_ro', 'featurepalette', 'moodpassion', 'cheadsmagazine', 
    		'wearethepeoplemagazine', 'streetstyle', 'moodyports', 'vsco', 'vscoportrait', 'gramkilla', 'instamood', 'creativesontherise', 
    		'trendhunter', 'portsvision', 'lifestyle',
    		'roamtheplanet', 'keepexploring', 'letsgosomewhere', 'nationalgeographic', 'travel', 'beautifulworld', 'exploretheglobe', 'exploretheglobe', 'traveladdict',
			'ig_exquisite', 'fantastic_earth', 'nature_wizards', 'landscape', 'landscape_capture', 'landscape_captures', 'landscape_hunter', 'landscape_lover', 
			'landscape_lovers', 'landscape_photography', 'landscapehunter', 'landscapelover', 'landscapelovers', 'landscapephotography', 'landscapephotomag', 
			'landscapephotos', 'landscapes', 'landscapeshot', 'landscapeslovers', 'landscape_specialist', 'natgeo', 'nationalgeographic', 'naturephotography', 'nature_prefection', 
			'ourplanetdaily',
			'portrait_ig', 'portrait_mood', 'portrait_page', 'portrait_perfection', 'portrait_planet', 'portrait_shot', 'portrait_shots', 'portrait_universe', 'portrait_vision', 
			'portraitphotography', 'portraitphotographyawards', 'portraitphotographys', 'portraits_ig', 'portraits_universe', 'portraitsession', 'portraitsfromtheworld', 
			'portraitshoot', 'portraitshot', 'portraitsmag', 'portraitsociety', 'portraitsofficial', 'portraitsshots', 'portraitstream', 'portraitstudio', 
			'portraitstyles', 'portraitsvision', 'portraitsvisuals', 'portraiture', 'postthepeople'
    		],
    tag_blacklist=['nsfw', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=93,
    follow_per_day=196,
    follow_time=1 * 60,
    unfollow_per_day=312,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=[])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
