# Part 2
# https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d

# Modified from py2 example to py36 env here

from flask import Flask
from flask import request
node = Flask(__name__)

# Store the transactions that
# this node has in a list
this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
    if request.method == 'POST':
        # On each new POST request,
        # we extract the transaction data
        new_txion = request.get_json()
        # Then we add the transaction to our list
        this_nodes_transactions.append(new_txion)
        # Because the transaction was successfully
        # submitted, we log it to our console
        print("New transaction")
        print("FROM: {}".format(new_txion['from']))
        print("TO: {}".format(new_txion['to']))
        print("AMOUNT: {}\n".format(new_txion['amount']))
        # Then we let the client know it worked out
        return "Transaction submission successful\n"

node.run()

# "To control the difficulty of mining new SnakeCoins, we’ll implement a
# Proof-of-Work (PoW) algorithm. A Proof-of-Work algorithm is essentially
# an algorithm that generates an item that is DIFFICULT to create but EASY
# to verify."

