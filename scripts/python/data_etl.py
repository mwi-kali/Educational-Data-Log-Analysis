# This Python script connects to a PostgreSQL database and utilizes Pandas to obtain data and create a data frame
import psycopg2
import pandas as pd
import pandas.io.sql as psql
from datetime import datetime

# Connect to the PostgreSQL database, Establish a connection to the database by creating a cursor object
host = "localhost" 
port_number = "5432" 
database_name = "moodle"
user_name = "postgres"
password = "secrets"
conn = psycopg2.connect(host=host, port=port_number, dbname=database_name, user=user_name, password=password)

# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def pull(sql_query, database = conn):
    table = psql.read_sql(sql_query, database, parse_dates=['timecreated'])
    return table

dedication_time = pull("SELECT * FROM mdl_logstore_standard_log")

def user_dedication_per_login(df_user_in,
                              verbose=0,
                              infilter = dict(eventname=['user_login_failed','notification']),
                              equalfilter = dict(action=['failed','loggedout'])):
    '''
        Purpose:
        Compute time between login and last activity. 
        To be improved:
        (1) Right now we assume a uniform dedication time between login and last activity.
        For future we can improve the dedication time by considering an approperiate weight 
        which reflects which activities the person did, upweighting read & write cruds, and 
        removing idle times, for example a user viewed a dashboard and didn't do anything 
        for 20mins afterwards. 
        Note:
        - 12 April 2019 - first implementation by Y. Fantaye
    '''
    
    #define output variables
    dt = {'logintime':[], 
          'timespent':[],
          'timespent_seconds':[],
          'deltalogin':[],
          'nactivities':[]
         }        
    tot_dedication_time = 0

    
    #** Filter -- remove failed login/email/etc from user logs 
    mask = None
    for k,vlist in infilter.items():
        for v in vlist:
            if verbose>0: print('applying infilter verb=%s, val=%s: '%(k,v) )
            m = df_user_in[k].map(lambda x: not v in x)
            if mask is None:
                mask = m
            else:
                mask = mask & m
    
    #for all filter with ==
    for k,v in equalfilter.items():
        if verbose>0: print('applying equalfilter verb=%s, val=%s: '%(k,v))
        m = df_user_in[k].map(lambda x: x != v)
        #m = df_user_in[k].map(lambda x:x.strip()) != v
        mask = mask & m
    
    # applied the combined filters 
    df_user = df_user_in[mask].copy()

    #if no activity after filter return empty
    if len(df_user)<1:
        if verbose>0: 
            print('Current user does not have any activity after filtering out the following:')
            print('  * ')
        df = pd.DataFrame.from_dict(dt)
        df = df.set_index('logintime')
        return df, tot_dedication_time 
        
        
    #set index to timecreated
    df_user.index = df_user['timecreated'].map(lambda x:pd.to_datetime(x,unit='s'))

    #sort dataframe by index/time
    df_user = df_user.sort_index()

    #get sorted user login times
    login_times = df_user[df_user['action']=='loggedin'].index

    #tfmt = "%Y-%m-%d %H:%M:%S"
    tfmt = "%I:%M:%S%p"

    if verbose>0:
        print('****** user log counts before and after filtering: ',len(df_user_in), len(df_user))
        print('***** logedin times *****')
        print(login_times)
        print('**************************')    


    #get the oldest login
    time_prev_login = login_times[0]

    for time_next_login in login_times[1:]:
        #consequetive login time difference
        tlogin_diff = time_next_login-time_prev_login
        
        if verbose>0:                    
            s = 'time_prev_login=%s, time_next_login=%s, hrs_after_prev_login=%s'
            print( s%(time_prev_login, time_next_login, tlogin_diff ) )

        #filter the activities of the current login                        
        mask = (df_user.index >= time_prev_login) & (df_user.index < time_next_login) 

        #basend on filter, get last activity and the maximum time
        last_activity = df_user[mask]
        
        if len(last_activity)>1:
            time_last_activity = last_activity.index.max()

            #calculate time difference. If timecreated is in unix time, unit is in seconds
            tdiff = time_last_activity - time_prev_login
            tdiff_seconds = tdiff.seconds
            #
            tot_dedication_time += tdiff_seconds
            
            if verbose>0:
                print('** ----- #activities = %s, Dedicatin time = %s -----'%(len(last_activity),tdiff) )
                if tdiff.total_seconds()>36000:
                    print('--------exceptional login activity with ---------')
                    print('-------------------------------------------------')            
                    print(last_activity[['eventname','crud']])
                    print('')            
        else:            
            tdiff = 0
            tdiff_seconds = 0
            
        #output variables
        dt['logintime'].append(time_prev_login)
        dt['timespent'].append(tdiff)
        dt['timespent_seconds'].append(tdiff_seconds),
        dt['deltalogin'].append(tlogin_diff)
        dt['nactivities'].append(len(last_activity))


        #set previous login to current login time
        time_prev_login = time_next_login
        
    df = pd.DataFrame.from_dict(dt)
    df = df.set_index('logintime')
    return df, tot_dedication_time
  
    
def dedication_per_user(dfgrp,verbose=0):
    tottime = {}
    dfstat = {}
    sstat = {x:[] for x in ['UserId','LoginCount','TotalTimeSpent','ActivitiesCount','MeanLoginTime']}
    
    df_user = pull("SELECT id AS userid FROM mdl_user")
    userids = list(df_user['userid'])

    for userid in userids:
        if userid>0 and not userid in [0,1,2,3,4]:
            if len(userids)>0:
                try:
                    df,tuser = user_dedication_per_login(dfgrp[dfgrp['userid']==userid],verbose=verbose)
                except IndexError:
                    continue
            else:
                df,tuser = None,0
            # 
            sstat[userid] = userid
            #
            tottime[userid] = tuser
            dfstat[userid] = df
            
            if verbose>0 and userid%30 == 0:
                print('iloop=%s, userid=%s, total dedication time=%s'%(i,userid, tuser))
    
    dfstat = pd.Series(tottime)
    return dfstat


dedication_time = dedication_per_user(dedication_time)
dedication_time = pd.DataFrame(dedication_time)

#Compute login and activity counts
login_counts = pull("SELECT u.id AS User_ID ,COUNT(*) AS Login_Count FROM mdl_logstore_standard_log AS l JOIN mdl_user AS u ON l.userid = u.id WHERE action = 'loggedin' GROUP BY u.id")

activity_counts = pull("SELECT userid AS User_ID,COUNT(*) AS Activity_Count FROM mdl_logstore_standard_log GROUP BY userid")

#country and gender for each user
country_gender = pull("SELECT id AS User_ID,country AS Country, gender AS Gender FROM mdl_user")

#Group students as top 1%, 5%, 10%, 25%
#Login count

login_counts.to_csv('data/login_counts.csv', index=False)

#Activity count

activity_counts.to_csv('data/activity_counts.csv', index=False)

#Dedication time

dedication_time.to_csv('data/dedication_time.csv')

country_gender.to_csv('data/country_gender.csv', index=False)