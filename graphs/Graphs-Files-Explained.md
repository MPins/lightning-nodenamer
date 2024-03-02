# Explaining each of graphs files used to generate the "NodeNamer"

I used the Lightning Polar (https://lightningpolar.com) to create the network of nodes.

With a network of lightning nodes running on Lightning Polar with at list one channel created for each node I runned following the command line on LND node:
- lncli describegraph

Obs.1 - To get the feature flags on Eclair node the coomand is: eclair-cli nodes
Obs.2 - To get the feature flags on Core Lightning the command is:  lightning-cli listnodes

As the LDK node is not available at Lightning Polar yet, I runned on my machine the ldk sample node available at (https://lightningdevkit.org/running-a-sample-ldk-node/) and connected it on graph1 lightning polar network opennig a channel to the LND node and generate the graph1-1.txt. 

graph1.json

    Eclair v0.8.0
    "alias": "alice",
    "pub_key": "0387794d6227a05b812807180cc51340408b4246b25f624b47c44cc92edb9f746b"

    LND v0.17.3
    "alias": "bob"
    "pub_key": "03878a8503028e1cd095c7fe35297e6bd978f1bf822610ab626dd5e0d792756be6"

    Core Lightning v23.05.2
    "alias": "carol"
    "pub_key": "02bef23553128cef07c1f46ff0caff369c0966d740dd81bf7f60d284cb36bb3a5d"

graph1-1.json

    just added the LDK node to the lightning polar network of graph1
    LDK v0.1.0
    "alias": "hellolightning"
    "pub_key": "02e383e9d5e2a46d125ddf1a6387bdea05558b1d740f75883573a9d76cb865e252"

graph2.json

    LND v0.17.2
    "alias": "bob"
    "pub_key": "03a4be97a9c8b451601ceb66659d08f3777b7ac6ad3f2ba93b2b75b2c3ee8e2bbf"

    Core Lightning v23.02.2
    "alias": "dave"
    "pub_key": "034b4be20be00ed419869bd63d7c251217e113ae62fb9e2ea81febbcbf3b4e6ece"

    Eclair v0.9.0
    "alias": "erin"
    "pub_key": "03fe86a02a6aa27a3a4a4c8636aa7195fa929dcb5c295914e60696eddd2a10f71d"

graph3.json

    LND v0.17.1
    "alias": "bob"
    "pub_key": "02f0ad7f85d5a0031dc388db35cbdacf18cb15b1da6457385ea039091e1a5de587"

    Eclair v0.7.0
    "alias": "carol"
    "pub_key": "0324ae9b5ed02cce42ab6a79cbf7ce7014071c239544aa76fd2bf16c5920a1ec17"
            
    Core Lightning v0.12.0
    "alias": "dave"
    "pub_key": "02c8ba5caf916107411433e7fbea90734834b46518f8593884bfd70a2801f23148"






    

            