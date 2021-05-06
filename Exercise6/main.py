from flask import Flask, render_template
from Blockchain import Blockchain

app = Flask(__name__, template_folder="templates")


@app.route('/wallet', methods=['GET'])
def get_wallet():
    """ method GET to return wallet value based of last transaction
    :return: amount of transaction in json form
    """
    for block in blockchain.chain:
        block_transaction = block['transactions']
        for trans in block_transaction:
            transaction = trans['amount']

    return {"block_wallet": transaction}


@app.route('/transactions', methods=['GET'])
def get_transactions():
    """ method GET to return transaction values - recipient, sender, amount
    :return: info on transaction in json form
    """
    for block in blockchain.chain:
        block_transaction = block['transactions']
        for trans in block_transaction:
            recipient = trans['recipient']
            sender = trans['sender']
            amount = trans['amount']

    return {"trans_recipient": recipient,
            "trans_sender": sender,
            "trans_amount": amount}


@app.route('/blocks', methods=['GET'])
def get_blocks():
    """ method GET to return blockchain length
    :return: blockchain length in json form
    """
    return {"blockchain_length": len(blockchain.chain)}


@app.route('/')
def home():
    """
    Renders template
    :return: the rendered template 'home.html'
    """
    return render_template('home.html')


if __name__ == '__main__':
    blockchain = Blockchain()
    t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
    blockchain.new_block(12345)
    app.run(debug=True, port=5000)