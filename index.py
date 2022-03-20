genesis_block[1] = "Y paid $100 to X"
genesis_block_hash = get_hash_itself(genesis_block)

print "genesis_block_hash:", genesis_block_hash
print "block1_parent_hash:", get_parent_hash(block1)
