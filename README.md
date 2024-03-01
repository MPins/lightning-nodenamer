# Overview
The lightning network protocol is implemented by various different projects: LND, Core
Lightning, Eclair and LDK. Each implementation has their own default values for various public
pieces of information, which can be used to fingerprint them. This information can be useful for
an attacker looking to exploit vulnerabilities that are specific to one implementation (or version
of an implementation). This information can also be used to make informed decisions about
protocol upgrades and deprecating features.

Examples of default values:
● Feature bits that are distinct to an implementation, or a version of an implementation.
● Default routing policies such as fees and cltv delta.
● Default generated node aliases or RGB colors.

Input format:
● A json description of the public graph. See the ones we use to start developing this project on graphs directory.

Output a CSV of node IDs, implementation names and version numbers:
● Node ID (string): the hex-encoded pubkey of a node in the graph.
● Implementation (string): LND, CLN, ECLR, LDK or UNKNOWN.
● Version (string): the implementation version or UNKNOWN.

This project was proposed by Chaincode Hackathon, see the document here.
