from blockchain import blockchain_class

block_chain = blockchain_class.BlockChain([])
block_chain.add_block()
print(block_chain.chain)
print(block_chain.curr_hash)
