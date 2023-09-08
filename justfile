# run the gossip algorithm on a network of n devices
gossip n:
    nodemon --exec "python" ./exercise_runner.py \
        --lecture 1 \
        --algorithm Gossip \
        --type async \
        --devices {{n}} \
