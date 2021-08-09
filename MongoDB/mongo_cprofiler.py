#!/usr/bin/env python3
# 06/07/2021
# Dev: Cody Yarger
# Assignment 06 - Profiling and Performance - MongoDB Social Network

'''
This module employs the cProfile and pstats libraries to profile methods used
in social network model
'''

# pylint: disable=C0103
import cProfile
import pstats
import main
import socialnetwork_model as sn


def profile(fun, *args):
    '''
        Takes a function and employs cprofile and pstats to perform Profiling
        param fun: function to be profiled
        param *args: arguments passed to the subject function being profiled
    '''

    # profile object
    prof = cProfile.Profile()
    # profile function
    prof.enable()
    fun(*args)
    prof.disable()

    # create stats report in metadata file format
    fun_name = fun.__name__
    file = open(fun_name + '_multi_' + '.md', 'w')
    p = pstats.Stats(prof, stream=file)
    p.strip_dirs().sort_stats('cumulative').print_stats(50)
    file.close()
    return prof


if __name__ == '__main__':

    mongo = sn.MongoDBConnection()
    with mongo:

        db = mongo.connection.media

        # collection in database
        UserAccounts = db['UserAccounts']
        UserAccounts.delete_many({})
        StatusUpdates = db['StatusUpdates']
        StatusUpdates.delete_many({})

        # instantiate user and status collection
        user_collection = main.init_user_collection(db)
        status_collection = main.init_status_collection(db)

        # ======================================================================
        # load users and status
        profile(main.load_users, "accounts", user_collection)
        profile(main.load_status_updates, "status_updates", status_collection)

        # # ======================================================================
        # # add users and status
        # profile(main.add_user, "userid", "email", "name", "last_name", user_collection)
        # profile(main.add_status, "userid", "statusid", "text", status_collection)
        #
        # # ======================================================================
        # # update users and status
        # profile(main.update_user, "userid", "email", "name", "last_name", user_collection)
        # profile(main.update_status, "statusid", "userid", "text", status_collection)
        #
        # # ======================================================================
        # # search users and status
        # profile(main.search_user, "userid", user_collection)
        # profile(main.search_status, "statusid", status_collection)
        #
        # # ======================================================================
        # # delete users and status
        # profile(main.delete_status, "statusid", status_collection)
        # profile(main.delete_user, "userid", user_collection)
