'''
  This is the config file which includes all ccnfiguation info here
'''
# RDS config
_DB_CONF = {
 'host':'database-1.chb5mphqelwh.us-east-1.rds.amazonaws.com',
 'port':3306,
 'user':'admin',
 'passwd':'database',
 'db':'instacart'
}


# Redshift config
_REDSHIFT_CONF = {
  'host':'redshift-cluster-1.ct6fvtggxdia.us-east-1.redshift.amazonaws.com',
  'port':5439,
  'user':'awsuser',
  'password':'Database12',
  'database':'dev'  # this is the database name
}


