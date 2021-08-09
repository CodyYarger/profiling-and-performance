#!/usr/bin/env python3
# 05/28/2021
# Dev: Cody Yarger
# Assignment 05 - MongoDB

'''
    Provides a basic frontend
'''
import sys
from datetime import datetime
#import pysnooper
from loguru import logger
import main
import socialnetwork_model as sn


log_file = datetime.now().strftime('log_%m_%d_%Y.log')
logger.add(log_file, level='INFO')


# user_collection database
user_coll = {}


# @pysnooper.snoop()
def load_users():
    '''
        Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')
    if not main.load_users(filename, user_collection):
        print('Error loading user accounts')
    else:
        print('User accounts loaded')
        # logger.info(f"{filename} data loaded successfully")


# @pysnooper.snoop()
def load_status_updates():
    '''
        Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    if not main.load_status_updates(filename, status_collection):
        print('Error loading user status')
    else:
        print('User status loaded')
        # logger.info(f"{filename} data loaded successfully")


# @pysnooper.snoop()
def add_user():
    '''
        Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')

    if not main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name,
                         user_collection
                         ):
        print('An error occurred while trying to add new user')
    else:
        print('User was successfully added')


# @pysnooper.snoop()
def update_user():
    '''
        Updates information for an existing user
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')

    if not main.update_user(user_id,
                            email,
                            user_name,
                            user_last_name,
                            user_collection
                            ):
        print('An error occurred while trying to update user')
    else:
        print('User was successfully updated')


# @pysnooper.snoop()
def search_user():
    '''
        Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    query = main.search_user(user_id, user_collection)

    if not query:
        print('ERROR: User does not exist')
    else:
        print(f'User ID: {query["_id"]}')
        print(f'Email: {query["email"]}')
        print(f'Name: {query["user_name"]}')
        print(f'Last name: {query["user_last_name"]}')


# @pysnooper.snoop()
def delete_user():
    '''
        Deletes user from the database
    '''
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print('An error occurred while trying to delete user')
    else:
        print('User was successfully deleted')
        print('Associated user status deleted')


# @pysnooper.snoop()
def add_status():
    '''
        Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(user_id, status_id, status_text, status_collection):
        print('An error occurred while trying to add new status')
    else:
        print('New status was successfully added')


# @pysnooper.snoop()
def update_status():
    '''
        Updates information for an existing status
    '''
    status_id = input('Status ID: ')
    user_id = input('User ID: ')
    status_text = input('Status text: ')
    if not main.update_status(status_id,
                              user_id,
                              status_text,
                              status_collection
                              ):
        print('Error updating status')
    else:
        print('Status was successfully updated')


# @pysnooper.snoop()
def search_status():
    '''
        Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')
    try:
        query = main.search_status(status_id, status_collection)
    except AttributeError:
        print('Error searching status')
    try:
        print(f'Status ID: {query["_id"]}')
        print(f'User ID: {query["user_id"]}')
        print(f'Status text: {query["status_text"]}')
    except TypeError:
        print('Error searching status')

# @pysnooper.snoop()


def delete_status():
    '''
        Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print('Error deleting status')
    else:
        print('Status was successfully deleted')


def quit_program():
    '''
        Quits program
    '''
    sys.exit()


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

        menu_options = {
            'A': load_users,
            'B': load_status_updates,
            'C': add_user,
            'D': update_user,
            'E': search_user,
            'F': delete_user,
            'H': add_status,
            'I': update_status,
            'J': search_status,
            'K': delete_status,
            'Q': quit_program
        }
        while True:
            user_selection = input("""
                                A: Load user database
                                B: Load status database
                                C: Add user
                                D: Update user
                                E: Search user
                                F: Delete user
                                H: Add status
                                I: Update status
                                J: Search status
                                K: Delete status
                                Q: Quit

                                Please enter your choice: """)
            if user_selection.upper() in menu_options:
                menu_options[user_selection.upper()]()
            else:
                print('Invalid option')
