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
            jsonify({
                'status': 'ok',
                'message': 'block added',
                'hash': block.hash
            })


@app.route('/chain')
def show_chain():
    return \
        jsonify([b.hash for b in chain.chain]) # chain.__repr__())


@app.route('/<block_hash>')
def show_block(block_hash):
    return \
        jsonify(
            [
            chain.get_block(block_hash).hash,
            chain.get_block(block_hash).prev_hash,
            [m.data for m in chain.get_block(block_hash).messages],
            str(chain.get_block(block_hash).timestamp)
            ]
        )


if __name__ == '__main__':
    chain = SimpleChain()
    chain_map = {}

    app.run()