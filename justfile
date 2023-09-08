# python exercise_runner.py --lecture 1 --algorithm Gossip --type async --devices {{n}}
gossip n:
    nodemon --exec "python" ./exercise_runner.py \
        --lecture 1 \
        --algorithm Gossip \
        --type async \
        --devices {{n}} \
