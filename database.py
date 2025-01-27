import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
#DETA_KEY = st.secrets["DETA_KEY"]

DETA_KEY = 'b0toqshk_AHhhwAXr39XPXGufjDgc38fSNHWSKL86'

# Initialize with a project key

deta = Deta(DETA_KEY)

#deta = 'QeZU3ZD3_Ue3rqfGGnJYVaXB71HErcV4LvyVvmXGj'

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

