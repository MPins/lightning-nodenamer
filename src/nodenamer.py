import sys 
import ijson
import re
import os

# Feature bits templates 
templates_index = [
                    {'implementation': 'CLN', 'version': 'UNKNOWN','Qty': 0}, #based on CLN v.23.05.2
                    {'implementation': 'ECLR', 'version': 'UNKNOWN','Qty': 0}, #based on ECLR v0.9.0 or v0.8.0
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0}, #based on LND v0.17.2, v0.17.1, v0.17.0, v0.16.4, v0.16.2, v0.16.1, v0.15.5
                    {'implementation': 'LDK', 'version': 'UNKNOWN', 'Qty': 0}, #based on LDK v0.1.0
                    {'implementation': 'CLN', 'version': 'UNKNOWN', 'Qty': 0}, #based on CLN v.23.0.2 or v0.12.0
                    {'implementation': 'ECLR', 'version': 'UNKNOWN', 'Qty': 0}, #based on ECLR v0.7.0
                    {'implementation': 'CLN', 'version': 'UNKNOWN', 'Qty': 0}, #based on CLN v0.11.2
                    {'implementation': 'ECLR', 'version': 'UNKNOWN', 'Qty': 0}, #based on ECLR v0.6.2
                    {'implementation': 'LND', 'version': 'Keysend','Qty': 0}, #base above + keysend 
                    {'implementation': 'LND', 'version': 'Tap+Wumbo', 'Qty': 0}, #base above + Simple taproot Channels and wumbo channels
                    {'implementation': 'LND', 'version': 'Tap', 'Qty': 0}, #base above + Simple taproot Channels
                    {'implementation': 'LND', 'version': 'Wumbo', 'Qty': 0}, # base above + Wumbo channels
                    {'implementation': 'LND', 'version': 'Wumbo+scid_alias+zero-conf', 'Qty': 0}, #base above + Wumbo + scid-alias + zero-conf
                    {'implementation': 'LND', 'version': 'no-shutdwon_any_seg+key_send', 'Qty': 0}, #base above + keysend with no shutdown-any-segwit 
                    {'implementation': 'LND', 'version': 'no-shutdwon_any_seg', 'Qty': 0}, #base above with no shutdown-any-segwit 
                    {'implementation': 'LND', 'version': 'scid_alias+zero_conf', 'Qty': 0}, #base above + scid-alias + zero-conf 
                    {'implementation': 'CLN', 'version': 'Wumbo','Qty': 0}, #base above + Wumbo                    
                    {'implementation' : 'UNKNOWN', 'version': 'UNKNOWN','Qty': 0}, 
                    {'implementation': 'NOFEATURES', 'version': 'NOFEATURES', 'Qty': 0},
                    {'implementation': 'NOUPDATE', 'version': 'NOUPDATE', 'Qty': 0}
                   ]
templates_list = [
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.39.name': 'unknown', 'nodes.item.features.39.is_required': False, 'nodes.item.features.39.is_known': False,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True,  'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.39.name': 'unknown', 'nodes.item.features.39.is_required': False, 'nodes.item.features.39.is_known': False,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.39.name': 'unknown', 'nodes.item.features.39.is_required': False, 'nodes.item.features.39.is_known': False,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True,  'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True, 
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True,  'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True, 
                     'nodes.item.features.181.name': 'simple-taproot-chans-x', 'nodes.item.features.181.is_required': False, 'nodes.item.features.181.is_known': True,
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True,  'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True, 
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True,  'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True, 
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True, 
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True, 
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True, 
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True, 
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True, 
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True, 
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True, 
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True, 
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True, 
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True, 
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True,
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True, 
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True, 
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True, 
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True, 
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True, 
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True, 
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True, 
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True,
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True, 
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True, 
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True, 
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True, 
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True, 
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True, 
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True, 
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True, 
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True, 
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True, 
                     'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True, 
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True, 
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True, 
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True, 
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True, 
                     'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True, 
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True, 
                     'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                    },
                    {
                     'nodes.item.features.1.name': 'data-loss-protect', 'nodes.item.features.1.is_required': False, 'nodes.item.features.1.is_known': True, 
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True, 
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True, 
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False, 
                     'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True, 
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True, 
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True, 
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True, 
                     'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False, 
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True, 
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True, 
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True, 
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True, 
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                    }                                                            
]

# This function receives input JSON file and create the new output JSON file 
# without the alias field.
# Sometimes the field ends on the next line with the comma (,)
# When it happens it will be deleted also
def remove_alias(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            alias = False
            for line in f_in:
                if alias == True:
                    alias = False
                    if ',' in line:
                        continue
                if not re.search(r'"alias"', line):
                    f_out.write(line)
                else:
                    if ',' not in line:
                        alias = True

def implementation_by_color(color):
    if color == "#3399ff":
        return 'LND'
    elif color == "#49daaa":
        return 'ECLR'
    else:
        return 'UNKNOWN'

# State machine class
class state_machine:
    def __init__(self):
        self.state = 'initial'

    def event(self, event, prefix, data):

        if self.state == 'initial' and event == 'start_map':
            # print("Transitioning from 'initial' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            return False
        elif self.state == 'map_started' and event == 'map_key':
            # print("Transitioning from 'map_started' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_started' and event == 'end_map':
            # print("Transitioning from 'map_started' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            return False
        elif self.state == 'mapping' and event == 'start_map':
            # print("Transitioning from 'mapping' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            return False
        elif self.state == 'mapping' and event == 'start_array':
            # print("Transitioning from 'mapping' to 'array_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_started'
            return False
        elif self.state == 'mapping' and event == 'null':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = ""
            return False
        elif self.state == 'mapping' and event == 'number':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'mapping' and event == 'string':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'mapping' and event == 'boolean':
            # print("Transitioning from 'mapping' to 'mapped' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapped'
            # Add a new key-value pair to the data field
            self.data[prefix] = data
            return False
        elif self.state == 'array_started' and event == 'start_map':
            # print("Transitioning from 'array_started' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'           
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we initate the data field with nodes or edges
            if len(pieces) == 2: self.data = {"data_type":pieces[0]}
            return False 
        elif self.state == 'array_started' and event == 'end_array':
            # print("Transitioning from 'array_started' to 'array_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_ended'
            return False
        elif self.state == 'mapped' and event == 'map_key':
            # print("Transitioning from 'mapped' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'mapped' and event == 'end_map':
            # print("Transitioning from 'mapped' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            return False
        elif self.state == 'map_ended' and event == 'end_array':
            # print("Transitioning from 'map_ended' to 'array_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'array_ended'
            return False
        elif self.state == 'map_ended' and event == 'start_map':
            # print("Transitioning from 'map_ended' to 'map_started' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_started'
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we initate the data field
            if len(pieces) == 2: self.data = {"data_type":pieces[0]}            
            return False
        elif self.state == 'map_ended' and event == 'map_key':
            # print("Transitioning from 'map_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'map_ended' and event == 'end_map':
            # print("Transitioning from 'map_ended' to 'map_ended' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'map_ended'
            pieces = prefix.split('.')
            # If the prefix field has 2 pieces (e.g. "nodes.item") we return true.
            # This way the calling function know that the data field must be used 
            # imeddiatelly, because he might be initialised during the forward interactions
            if len(pieces) == 2: return True
        elif self.state == 'array_ended' and event == 'map_key':
            # print("Transitioning from 'array_ended' to 'mapping' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'mapping'
            return False
        elif self.state == 'array_ended' and event == 'end_map':
            # print("Transitioning from 'array_ended' to 'final' event:", event, "prefix:", prefix, "data:",data)
            self.state = 'final'
            return False
        else:
            print("Invalid transition")

# Process the json file generated by the lncli describegraph 
def main(json_file):
    try:
        # Initialize the output lists
        output = []
        output_temp = []
        output_unknown = []
        output_no_features = []
        output_no_updates = []
        output_no_features_temp = []
        output_no_updates_temp = []

        #Initialize counters
        counters = {'LND': 0, 'CLN': 0, 'ECLR': 0,'LDK': 0}
        nodes_counter = 0
        channels_counter = 0

        # Create an instance of the state machine
        sm = state_machine()

        # Open the JSON file for reading
        with open(json_file, 'r', encoding='utf-8', errors='ignore') as file:
            try:
                parser = ijson.parse(file)  # Create an iterator for the JSON data
                for prefix, event, value in parser:
                    # Process the JSON events as needed
                    # Perform transitions
                    # If the transition results in completed nodes or edges data
                    # Takes the data to mount the output
                    if sm.event(event, prefix, value) is True:
                        if sm.data['data_type'] == "nodes":
                            nodes_counter +=1
                            del sm.data['data_type']
                            pubkey = sm.data['nodes.item.pub_key']
                            node_color = sm.data['nodes.item.color']
                            last_update = sm.data['nodes.item.last_update']
                            # deleting data to compare the features fingerprint only
                            for key, value in sm.data.copy().items():
                                # Process the key-value pair
                                pieces = key.split('.')
                                if pieces[2] != "features" and len(pieces) > 2:
                                    del sm.data[key]

                            template_found = False
                            # ***** FIRST LAYER ***** trying to identify the node using the feature bits
                            for i, template in enumerate(templates_list):
                                if template == sm.data:
                                    template_found = True
                                    # Extract implementation and version from the template index
                                    templates_index[i]['Qty'] += 1
                                    new_output = {"id": pubkey, "implementation": templates_index[i]['implementation'], "version": templates_index[i]['version']}
                                    output.append(new_output)
                            
                            # If not found a template of features bits inserting this node as UNKOWN
                            # We are going to figure out the node implementation using the channel default policies
                            # And the default color captured above
                            if template_found == False and last_update != 0 and len(sm.data) > 0:
                                templates_index[len(templates_index)-3]['Qty'] += 1
                                new_output = {"id": pubkey, "color": node_color, "implementation": "UNKNOWN", "version": "UNKNOWN", 'LND': 0, 'LDK': 0, 'CLN': 0, 'ECLR': 0}
                                output_temp.append(new_output)
                            if template_found == False and last_update != 0 and len(sm.data) == 0:
                                templates_index[len(templates_index)-2]['Qty'] += 1
                                new_output = {"id": pubkey, "color": node_color, "implementation": "NOFEATURES", "version": "NOFEATURES", 'LND': 0, 'LDK': 0, 'CLN': 0, 'ECLR': 0}
                                output_no_features_temp.append(new_output)                    
                            if template_found == False and last_update == 0:
                                templates_index[len(templates_index)-1]['Qty'] += 1
                                new_output = {"id": pubkey, "color": node_color, "implementation": "NOUPDATE", "version": "NOUPDATE", 'LND': 0, 'LDK': 0, 'CLN': 0, 'ECLR': 0}
                                output_no_updates_temp.append(new_output)
                        # ***** SECOND LAYER ***** trying to identify the node using the defaul channel policies (continue)         
                        elif sm.data['data_type'] == "edges":
                            channels_counter += 1
                            if sm.data['edges.item.last_update'] == 0: continue
                            # I'm counting the each distribution time_lock_delta default of each channel of the nodes
                            # that based on feature bits are unkown
                            for node in output_temp:
                                if node.get('id') == sm.data['edges.item.node1_pub'] and node.get('implementation') == 'UNKNOWN':
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 144:
                                        node['ECLR'] +=1
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 72:
                                        node['LDK'] +=1
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 6:
                                        node['CLN'] +=1
                                    if sm.data.get('edges.item.node1_policy.time_lock_delta') == 40 or sm.data.get('edges.item.node1_policy.time_lock_delta') == 80:
                                        node['LND'] +=1
                                if node.get('id') == sm.data['edges.item.node2_pub'] and node.get('implementation') == 'UNKNOWN':
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 144:
                                        node['ECLR'] +=1
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 72:
                                        node['LDK'] +=1
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 6:
                                        node['CLN'] +=1
                                    if sm.data.get('edges.item.node2_policy.time_lock_delta') == 40 or sm.data.get('edges.item.node2_policy.time_lock_delta') == 80:
                                        node['LND'] +=1
                        print(f"Nodes: {nodes_counter} | Channels: {channels_counter}", end="\r")    
                                         
            except ijson.JSONError as e:
                print(f"Error parsing JSON: {e}")                
        print()
        # ***** SECOND LAYER ***** trying to identify the node using the defaul channel policies
        # Take the nodes data stored on output_unknown and use it to try identifying them
        output_temp.extend(output_no_features_temp)
        output_temp.extend(output_no_updates_temp)
        for node in output_temp:
            max_value = 0
            max_key = 'LND'
            for key in ['LND', 'CLN', 'ECLR', 'LDK']:
            # Update max_key and max_value if the current value is greater
                if node[key] > max_value:
                    max_key = key
            if node[max_key] > 0:
                new_output = {"id": node['id'], "implementation": max_key, "version": 'UNKNOWN'}
                output.append(new_output)
            else:
                # ***** THIRD LAYER ***** trying to identify the node using the defaul node color
                imp_by_color = implementation_by_color(node['color'])
                if imp_by_color == "UNKNOWN":
                    if node['implementation'] == "UNKNOWN": 
                        new_output = {"id": node['id'], "implementation": "UNKNOWN", "version": 'UNKNOWN'}
                        output_unknown.append(new_output)   
                    elif node['implementation'] == "NOFEATURES":
                        new_output = {"id": node['id'], "implementation": "NOFEATURES", "version": 'UNKNOWN'}
                        output_no_features.append(new_output)
                    elif node['implementation'] == "NOUPDATE":
                        new_output = {"id": node['id'], "implementation": "NOUPDATE", "version": 'UNKNOWN'}
                        output_no_updates.append(new_output)
                else:
                        new_output = {"id": node['id'], "implementation": imp_by_color, "version": 'UNKNOWN'}
                        output.append(new_output)

        with open('nodenamer.csv', 'w', encoding='utf-8') as f_out:
            for node in output:
                key = node.get('implementation')
                counters[key] += 1            
                line = node.get('id') + "," + node.get('implementation') + "," + node.get('version') + "\n"
                f_out.write(line)

        for label, qty in counters.items():
            print(f"{label}: {qty}")
        print(f"UNKNOWN NODES: {len(output_unknown)}")
        print(f"NO UPDATES NODES: {len(output_no_updates)}")
        print(f"NO FEATURE BIT NODES: {len(output_no_features)}")        

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nodenamer.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]

    # create another file ignoring the alias field due the erros it cause whe parsing it
    # because of unexpected characteres
    file_name, file_extension = os.path.splitext(json_file)

    s_json_file = file_name + "_s" + file_extension
    remove_alias(json_file, s_json_file)
        
    main(s_json_file)

    # delete the created file
    if os.path.exists(s_json_file):
        # Delete the file
        os.remove(s_json_file)

