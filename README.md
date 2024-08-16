# Overview
The lightning network protocol is implemented by various different projects: LND, Core
Lightning, Eclair and LDK. Each implementation has their own default values for various public
pieces of information, which can be used to fingerprint them. This information can be useful for
an attacker looking to exploit vulnerabilities that are specific to one implementation (or version
of an implementation). This information can also be used to make informed decisions about
protocol upgrades and deprecating features.

Examples of default values:
- Feature bits that are distinct to an implementation, or a version of an implementation.
- Default routing policies such as fees and cltv delta.
- Default generated node aliases or RGB colors.

Input format:
- A json description of the public graph. See the ones we use to start developing this project on graphs folder. We get it running the following command on a LND node:
    - lncli describegraph

Output (nodenamer.log) with the node IDs, implementation names and version numbers:
- Node ID (string): the hex-encoded pubkey of a node in the graph.
- Implementation (string): LND, CLN, ECLR, LDK or UNKNOWN.
- Version (string): the implementation version or UNKNOWN.

Obs: The investigation done until the moment did not indicate that there is a reliable way to get the version of a lightning node implementation from feature bits, color or default policy

This project was proposed by Chaincode Hackathon, see the document [here](https://github.com/MPins/lightning-nodenamer/blob/main/Hackathon-Project-NodeNamer.pdf).

# Dependencies

- IJSON python Library

ijson is a Python library that provides a way to work with JSON data in a streaming manner. It allows you to parse large JSON documents efficiently without loading the entire document into memory. Instead, it iterates over the JSON data, allowing you to process it piece by piece.

Run the following command to install the `ijson` library

```sh
pip install ijson
```

# How to run

To run the Nodenamer is very simple, just clone the git repository on your machine.

```sh
git clone https://github.com/MPins/lightning-nodenamer
```

Go to the source folder and make sure you can run the `nodenamer.py` python program.

```sh
python nodenamer.py <json_file> <log_dir>
```

You can start using some json file examples on the graphs folder. The nodenamer will create the following files:
- nodenamer.log, nodenamer-features.log and nodenamer-features-total.log into the <log_dir> folder indicate in the command line.
- nodenamer-unknown-fingerprints.txt into the same folder of the graph file folder indicate in the command line.

# Screen Output

Besides the files created the program will show the following information on the screen

- Nodes: #of_nodes | Channels: #of_channels
- LND: #total of LND nodes
- CLN: #total of CLN nodes
- ECLR: #total of ECLR nodes
- LDK: #total of LDK nodes
- UNKNOWN NODES: #total of unknown nodes
- NO UPDATES NODES: #total of nodes which there is no updates on this json graph file
- NO FEATURE BIT NODES: #total of nodes which there is no feature bits on this json graph file

- Additionaly it will output the counting of each feature bits encountered on each node

# Understanding the approach

The programm approach the node implementation identification using 3 layers of information:

- The first layer is considering only the features bit, in my opinion it is the strongest info we have, if it is possible to identify the implementation using the feature bits the program will not run the following two layers on the specific node.

- The second layer takes the unknown nodes from the first layer and try to figure them out looking at the default channel policies.

- Only the third layer of investigation is considering the default color, which in my opinion is the weakest information to be considered.

This way I think we minimize the chance of getting false positives.

# The State Machine

This is the State Machine tha was coded to read the Graph JSON file.

![alt text](image.png)

# Grafana integration

I created a [Grafana Dashboard](https://pins.grafana.net/public-dashboards/478199ff803c44138feb1439908e891f) to show the Lightning Nodenamer results.

I'm using Promtail agent which ships the contents of local logs to a private Grafana Loki instance or Grafana Cloud (I'm using Grafana Cloud).

Now the Nodenamer creates 3 log files:
- nodenamer.log - each line on the log brings the pubkey, the implementation and version
- nodenamer-features.log - each line on the log brings the bubkey and the feature bit, one line for each feature of each node. Grafana Cloud compleined about the data ingestion rate, for this reason the third log file was implemented and this one is not being used yet.
- nodenamer-features-total.log - just one line for eache feature bit that brings the amount of nodes using that feature.

Installing Promtail using Docker, modify tag to the most recent version.

```sh
docker pull grafana/promtail:latest
```

Configuring Promtail to send logs, follow the instructions [here](https://grafana.com/docs/grafana-cloud/send-data/logs/collect-logs-with-promtail/#option-1-send-logs-from-a-standalone-host), I'm sending logs from a standalone host.

The grafana json file that exports the dashboard you can see [here](https://pins.grafana.net/public-dashboards/478199ff803c44138feb1439908e891f) is found on the main folder of the project with the name [lightning-nodenamer-grafana-dashboard.json](lightning-nodenamer-grafana-dashboard.json)

# Feature Bits Fingerprint File

Additionaly the file nodenamer-unknown-fingerprints.txt is generated at the same folder of the json graph file. It contains the unknown fingerprints and the reason to generate it is helping to identify new fingerprints during the use of nodenamer.





