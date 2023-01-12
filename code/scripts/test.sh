#!/bin/sh

INPUT_GRAPH="inputs/soc-LiveJournal1-trim-100_sym.adj"

if [ $1 = "sa" ]
then
    # run static algorithm
    make run_static_algorithm
    numactl -i all ./run_static_algorithm -all -src 10012 -nsrc 576 -s -m -f $INPUT_GRAPH
    # ./run_static_algorithm -all -src 10012 -nsrc 576 -s -m -f $INPUT_GRAPH
elif [ $1 = "mf" ]
then
    # run memory foot print
    make memory_footprint
    numactl -i all ./memory_footprint -s -m -f $INPUT_GRAPH
    # ./memory_footprint -s -m -f $INPUT_GRAPH
elif [ $1 = "bu" ]
then
    # batch update
    make run_batch_updates
    numactl -i all ./run_batch_updates -s -f $INPUT_GRAPH
elif [ $1 = "suq" ]
then
    # simultaneous updates queries
    make run_simultaneous_updates_queries
    numactl -i all ./run_simultaneous_updates_queries -queryiters 200 -m -s -f $INPUT_GRAPH
else
    echo "please specify right arguments"
fi
