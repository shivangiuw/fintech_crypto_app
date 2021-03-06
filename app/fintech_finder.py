# Cryptocurrency Wallet

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################
# Step 1- Part 1: Add your mnemonic seed phrase (provided by Ganache) to the `.env` file.

################################################################################
# Step 1 - Part 2:
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=150)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 3:
# Call the `generate_account` function and save it as the variable `account`
# This function will create the Fintech Finder
# customer???s (in this case, your) HD wallet and Ethereum account.

account= generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 4:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer???s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(w3, account.address))

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(f"Hourly rate: {hourly_rate}")

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# Part 1:
# Fintech Finder customers will select a fintech professional from the
# application interface???s drop-down menu, and then input the amount of time(hours) for
# which they???ll hire the worker. 

# Calculate total `wage` for the candidate by multiplying the candidate???s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = float(candidate_database[person][3]) * float(hours)

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(f"Total wage: {wage}")

##########################################
# Part 2:
# Now that the application can calculate a candidate???s wage, to send an Ethereum blockchain
# transaction that pays the hired candidate,
# add logic to the `if` statement that sends the appropriate information to
# the `send_transaction` function (imported from the `crypto_wallet`
# script file). Inside the `if` statement, add the following functionality:
        #  From the `account` instance, the application will be able to access the
        #  `account.address` information that is needed to populate the `from` data
        # attribute in the raw transaction.
        #- The `candidate_address` (which will be created and identified in the
        # sidebar when a customer selects a candidate). This will populate the `to`
        # data attribute in the raw transaction.
        # - The `wage` value. This will be passed to the `toWei` function to
        # determine the wei value of the payment in the raw transaction.

    # * Save the transaction hash that the `send_transaction` function returns
    # as a variable named `transaction_hash`, and have it display on the
    # application???s web interface.

if st.sidebar.button("Send Transaction"):
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, candidate_address, wage )

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()

################################################################################
