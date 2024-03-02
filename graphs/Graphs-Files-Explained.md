# Explaining each of graphs files used to generate the "NodeNamer"

I used the Lightning Polar (https://lightningpolar.com) to create the network of nodes.

With a network of lightning nodes running on Lightning Polar with at list one channel created for each node I runned following the command on LND node:
- lncli describegraph

As the LDK node is not available at Lightning Polar yet, I runned ldk sample node on my machine (https://lightningdevkit.org/running-a-sample-ldk-node/) and connected it on graph1 lightning polar network opennig a channel to the LND node and generate the graph1-1.json.

I collected the fingerprint of the following implementation and version.

graph-1.json

    Eclair v0.8.0
    "alias": "alice",
    "pub_key": "0387794d6227a05b812807180cc51340408b4246b25f624b47c44cc92edb9f746b"

    LND v0.17.3
    "alias": "bob"
    "pub_key": "03878a8503028e1cd095c7fe35297e6bd978f1bf822610ab626dd5e0d792756be6"

    Core Lightning v23.05.2
    "alias": "carol"
    "pub_key": "02bef23553128cef07c1f46ff0caff369c0966d740dd81bf7f60d284cb36bb3a5d"

graph-1-1.json

    just added the LDK node to the lightning polar network of graph1
    LDK v0.1.0
    "alias": "hellolightning"
    "pub_key": "02e383e9d5e2a46d125ddf1a6387bdea05558b1d740f75883573a9d76cb865e252"

graph-2.json

    LND v0.17.2
    "alias": "bob"
    "pub_key": "03a4be97a9c8b451601ceb66659d08f3777b7ac6ad3f2ba93b2b75b2c3ee8e2bbf"

    Core Lightning v23.02.2
    "alias": "dave"
    "pub_key": "034b4be20be00ed419869bd63d7c251217e113ae62fb9e2ea81febbcbf3b4e6ece"

    Eclair v0.9.0
    "alias": "erin"
    "pub_key": "03fe86a02a6aa27a3a4a4c8636aa7195fa929dcb5c295914e60696eddd2a10f71d"

graph-3.json

    LND v0.17.1
    "alias": "bob"
    "pub_key": "02f0ad7f85d5a0031dc388db35cbdacf18cb15b1da6457385ea039091e1a5de587"

    Eclair v0.7.0
    "alias": "carol"
    "pub_key": "0324ae9b5ed02cce42ab6a79cbf7ce7014071c239544aa76fd2bf16c5920a1ec17"
            
    Core Lightning v0.12.0
    "alias": "dave"
    "pub_key": "02c8ba5caf916107411433e7fbea90734834b46518f8593884bfd70a2801f23148"

graph-4.json

    LND v0.17.0
    "alias": "alice"
    "pub_key": "03b6193d8a341a616c182ef044624a6b64fb77beee882356823aeb031cfd63c25b"       
    
    LND v0.16.4
    "alias": "bob"        
    "pub_key": "021a66c2edbd0be82d7c66e57316b773b6dd51c173c9cc10913134ea813a19735f"

    LND v0.16.2
    "alias": "carol"
    "pub_key": "03c5630a7778c655e9abfe038cc674c7e4046f5b1e2b397379b7447193b9c6b279"

    Core Lightning v0.12.0
    "alias": "dave"
    "pub_key": "03f6a5acc209b8b9cd80f2b93db6f41812553063d09163a2c244bd104268fc838a"
                    
    Core Lightning v0.11.2
    "alias": "erin"
    "pub_key": "02ccd160a839941b4a34664cd886b7deb996387f7e1b7c1378f1da1f9a635899b2"

    Eclair v0.6.2
    "alias": "frank"
    "pub_key": "037d1659cef7711ae3b8891f5dc20137941c6a99412ed1587985d33be6e4f9299f"

graph-5.json

    LND v0.16.1
    "alias": "bob"
    "pub_key": "02361a03ccd076281df7eec7bae72e5c9db63d87ee8dcef810aa8f5f2c538e08b9"

    LND v0.16.0
    "alias": "carol"
    "pub_key": "03b1126e2121d016284aadc6b1345177bec7f9d487ad839170dca4fc81eae0fd57"

    LND v0.15.5
    "alias": "dave"
    "pub_key": "02fba2d62eac50a26f785c2140024b09ca716e65ec2be1e4031235e854df959bff"
    
            
    