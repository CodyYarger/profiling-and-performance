#!/usr/bin/env python3
# 05/28/2021
# Dev: Cody Yarger
# Assignment 05 - MongoDB
'''
User Classes for social network project
'''

# pylint: disable=R0903
from loguru import logger
#import pysnooper
import pymongo as pm


class UserCollection():
    '''
        Contains a collection of Users objects
    '''

    def __init__(self, database):
        self.database = database
        logger.info("New UserCollection instantiated")

    # @pysnooper.snoop()
    def add_user(self, user_id, email, user_name, user_last_name):
        '''
            Adds a new user to user collection
        '''
        new_user_doc = {"_id": user_id,
                        "email": email,
                        "user_name": user_name,
                        "user_last_name": user_last_name
                        }
        try:
            self.database.UserAccounts.insert_one(new_user_doc)
            logger.info(f'New user: {user_id} - added to database')
            return True
        except pm.errors.DuplicateKeyError:
            logger.info(f'User ID: {user_id} - already in database')
            return False

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
            Modifies an existing user
        '''
        if self.database.UserAccounts.find_one({'_id': user_id}):
            modify_user_doc = {"_id": user_id,
                               "email": email,
                               "user_name": user_name,
                               "user_last_name": user_last_name
                               }

            self.database.UserAccounts.update_one({'_id': user_id},
                                                  {'$set': modify_user_doc})
            logger.info('User: {user_id} - data modified')
            return True
        logger.info('No User: {user_id} - in database')
        return False

    def delete_user(self, user_id):
        '''
            Deletes an existing user
        '''
        if self.database.UserAccounts.find_one({'_id': user_id}):
            self.database.UserAccounts.delete_one({'_id': user_id})
            self.database.StatusUpdates.delete_many({'user_id': user_id})
            logger.info('User: {user_id} and Status deleted')
            return True
        logger.info('No User: {user_id} - in database')
        return False

    # @pysnooper.snoop()
    def search_user(self, user_id):
        '''
            Searches for user data
        '''
        if self.database.UserAccounts.find_one({'_id': user_id}):
            query = {"_id": user_id}
            logger.info('User: {user_id} - found')
            return self.database.UserAccounts.find_one(query)
        logger.info('No User: {user_id} - in database')
        return False
