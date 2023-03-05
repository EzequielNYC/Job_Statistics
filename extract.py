from config import connection


from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import functools as ft

#prepairing connection to database

engine = create_engine(connection)

#pulling data
session = Session(engine)

#reflect the tables in the database
Base = automap_base()
Base.prepare(engine, reflect=True)


#mapping classes
jobs = Base.classes.jobs
skills = Base.classes.skills
salaries = Base.classes.salaries 


#build quereis to pull all amazon data 
jobs_result = session.query(jobs)
skills_result = session.query(skills)
salaries_result = session.query(salaries)

# creating each dateframe
jobs_df = pd.read_sql(sql = jobs_result.statement, con = engine.connect())
skills_df = pd.read_sql(sql = skills_result.statement, con = engine.connect())
salaries_df = pd.read_sql(sql = salaries_result.statement, con = engine.connect())

#merging 
dfs = [jobs_df,skills_df,salaries_df]
df_merged = ft.reduce(lambda  left,right: pd.merge(left,right,on=['id'], how='outer'), dfs)

df_merged.to_csv("/Users/ezequielesparza/Job_Statistics/data/joined_data.csv",index = False)