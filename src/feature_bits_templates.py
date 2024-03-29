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
