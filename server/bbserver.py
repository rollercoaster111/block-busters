from flask import Flask
from flask import request, jsonify
import json
from pysimplechain import Block, SimpleChain, Message

app = Flask(__name__)


@app.route('/')
def info():
    return \
        json.dumps({
            'server': 'bbserver',
            'version': 0.1,
            'description': 'block-buster blockchain server'
        })


@app.route('/add', methods=['POST'])
def add_block():
    post_data = request.get_json()

    block = Block()
    block.add_message(Message(
        json.dumps(
            post_data
        )
    ))
    chain.add_block((block))

    return \
            json.dumps({
                'status': 'ok',
                'message': 'block added',
                'hash': block._hash_block()
            })


@app.route('/chain')
def show_chain():
    return \
        jsonify([b.__repr__() for b in chain.chain]) # chain.__repr__())


if __name__ == '__main__':
    chain = SimpleChain()
    app.run()