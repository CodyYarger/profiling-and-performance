#!/usr/bin/env python3
# 05/28/2021
# Dev: Cody Yarger
# Assignment 05 - MongoDB
'''
User status Classes for social network project
'''

# pylint: disable=R0801
# pylint: disable=R0903
import pymongo as pm
from loguru import logger
#import pysnooper


class UserStatusCollection():
    '''
        Contains a collection of User Status objects
    '''

    def __init__(self, database):
        self.database = database
        logger.info('New UserStatusCollection instantiated')

    # @pysnooper.snoop()
    def add_status(self, status_id, user_id, status_text):
        '''
            Adds new status to user status collection
        '''
        if self.database.UserAccounts.find_one({'_id': user_id}):

            new_status_doc = {"_id": status_id,
                              "user_id": user_id,
                              "status_text": status_text
                              }
            try:
                self.database.StatusUpdates.insert_one(new_status_doc)
                logger.info(f'New status: {status_id} - added to database')
                return True
            except pm.errors.DuplicateKeyError:
                logger.info(f'Status UD: {status_id} - already in database')
                return False
        else:
            return False

    def modify_status(self, status_id, user_id, status_text):
        '''
            Modifies user status
        '''
        if (self.database.UserAccounts.find_one({'_id': user_id}) and
                self.database.StatusUpdates.find_one({'_id': status_id})):

            modify_satus_doc = {"_id": status_id,
                                "user_id": user_id,
                                "status_text": status_text
                                }
            self.database.StatusUpdates.update_one({'_id': status_id},
                                                   {'$set': modify_satus_doc})
            logger.info('Status: {_id} - modified')
            return True
        logger.info('No Status: {status_id} - in database')
        return False

    def delete_status(self, status_id):
        '''
            Deletes user status
        '''
        if self.database.StatusUpdates.find_one({'_id': status_id}):
            self.database.StatusUpdates.delete_one({'_id': status_id})
            logger.info('Status: {_id} - deleted')
            return True
        logger.info('No Status: {status_id} - in database')
        return False

    # @pysnooper.snoop()
    def search_status(self, status_id):
        '''
            Searches for user status
        '''
        if self.database.StatusUpdates.find_one({'_id': status_id}):
            query = {"_id": status_id}
            return self.database.StatusUpdates.find_one(query)
        logger.info('No Status: {status_id} - in database')
        return False
