from datetime import datetime
from hashlib import sha256

class BlockChain:
    def __init__(self,chain):
        self.index = 1
        self.chain = chain
        self.prev_hash = sha256("first block".encode()).hexdigest()
        print("Blockchain has been initiated! And first block has been attached!")
        self.chain.append(self.genesis_block())
        print(self.chain)

    def genesis_block(self):
        self.data = input()
        self.new_hash = self.curr_hash(self.data)
        block = self.create_block()

        return block

    def curr_hash(self, x):
        encoded_hash = sha256(x.encode())
        hash_value = encoded_hash.hexdigest()

        return hash_value

    def create_block(self):
        curr_time = datetime.now()
        block = {'Index': self.index, 'Data': self.data, 'Previous_hash': self.prev_hash,
                 'Current_hash': self.new_hash, 'Time_stamp': curr_time.strftime("%m/%d/%Y, %H:%M:%S")}

        return block

    def add_block(self):

        print("Please enter number of blocks you want to add: ")
        n = int(input())

        while self.chain[-1]['Index'] < n:
            print("Please enter a valid hash: ")
            hash = input()

            if self.chain[-1]['Current_hash'] == hash:
                print("Congratulations! this is a valid hash")
                self.prev_hash = hash
                print("Enter the data for the block: ")
                data = input()
                self.data = data
                self.new_hash = self.curr_hash(data)
                self.index += 1

                next_block = self.create_block()

                print("new block added is: ")
                print(next_block)

                self.chain.append(next_block)

            else:
                print("This is not a valid hash! Please provide a valid hash code to continue!")

        @property
        def chain(self):
            print("Getting the chain")
            return self._chain

        @chain.setter
        def chain(self, value):
            print("Setting the chain")
            self._chain = value











