# Feature bits are specified in Bolt 9.
# They let nodes publicly advertise that they support or require a given feature.
# Feature bits in the 0-255 range are reserved for BOLTs: bLIPs must use feature bits above that range.
# Custom feature bits used in the I Bolt 11 context must be <= 5114 due to the size limitations on tagged fields.
# BOLT #9: Assigned Feature Flags. bLIPs where commented.
bolt9_feature_flags = [
                        {'0':'option_data_loss_protect'},
                        {'1':'option_data_loss_protect'},
                        {'2':'initial_routing_sync'},
                        {'3':'initial_routing_sync'},
                        {'4':'option_upfront_shutdown_script'},
                        {'5':'option_upfront_shutdown_script'},
                        {'6':'gossip_queries'},
                        {'7':'gossip_queries'},
                        {'8':'var_onion_optin'},
                        {'9':'var_onion_optin'},
                        {'10':'gossip_queries_ex'},
                        {'11':'gossip_queries_ex'},
                        {'12':'option_static_remotekey'},
                        {'13':'option_static_remotekey'},
                        {'14':'payment_secret'},
                        {'15':'payment_secret'},
                        {'16':'basic_mpp'},
                        {'17':'basic_mpp'},
                        {'18':'option_support_large_channel'},
                        {'19':'option_support_large_channel'},
                        {'20':'option_anchor_outputs'},
                        {'21':'option_anchor_outputs'},
                        {'22':'option_anchors_zero_fee_htlc_tx'},
                        {'23':'option_anchors_zero_fee_htlc_tx'},
                        {'24':'option_route_blinding'},
                        {'25':'option_route_blinding'},
                        {'26':'option_shutdown_anysegwit'},
                        {'27':'option_shutdown_anysegwit'},
                        {'28':'option_dual_fund'},
                        {'29':'option_dual_fund'},
                        {'30':'amp'},                               # bolts/pull/658
                        {'31':'amp'},                               # bolts/pull/658                        
                        {'32':'option_alternative_feerates'},       # bolts/pull/1036
                        {'33':'option_alternative_feerates'},       # bolts/pull/1036
                        {'34':'option_quiesce'},                    # bolts/pull/869
                        {'35':'option_quiesce'},                    # bolts/pull/869
                        {'36':'option_attributable_error'},         # bolts/pull/1044
                        {'37':'option_attributable_error'},         # bolts/pull/1044
                        {'38':'option_onion_messages'},
                        {'39':'option_onion_messages'},
                        {'40':'want_peer_backup_storage'},          # bolts/pull/881
                        {'41':'want_peer_backup_storage'},          # bolts/pull/881
                        {'42':'provide_peer_backup_storage'},       # bolts/pull/881
                        {'43':'provide_peer_backup_storage'},       # bolts/pull/881
                        {'44':'option_channel_type'},
                        {'45':'option_channel_type'},
                        {'46':'option_scid_alias'},
                        {'47':'option_scid_alias'},
                        {'48':'option_payment_metadata'},
                        {'49':'option_payment_metadata'},
                        {'50':'option_zeroconf'},
                        {'51':'option_zeroconf'},
                        {'52':'option_htlc_hold'},                  # bolts/pull/989
                        {'53':'option_htlc_hold'},                  # bolts/pull/989
                        {'54':'keysend'},                           # bLIP 3
                        {'55':'keysend'},                           # bLIP 3
                        {'56':'trampoline_routing'},                # bolts/pull/836
                        {'57':'trampoline_routing'},                # bolts/pull/836
                        {'60':'option_simple_close'},               # bolts/pull/1096
                        {'61':'option_simple_close'},               # bolts/pull/1096
                        {'62':'option_splice'},                     # bolts/pull/863
                        {'63':'option_splice'},                     # bolts/pull/863
                        {'64':'option_zero_reserve'},               # bolts/pull/1140
                        {'65':'option_zero_reserve'},               # bolts/pull/1140
                        {'106':'option_simplified_update'},         # bolts/pull/867
                        {'107':'option_simplified_update'},         # bolts/pull/867
                        {'256':'hosted_channels'},                  # bLIP 17
                        {'257':'hosted_channels'}                   # bLIP 17
]

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
                    {'implementation': 'LND', 'version': 'UNKNOWN','Qty': 0}, #base above + keysend 
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, #base above + Simple taproot Channels and wumbo channels
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, #base above + Simple taproot Channels
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, # base above + Wumbo channels
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, #base above + Wumbo + scid-alias + zero-conf
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, #base above + keysend with no shutdown-any-segwit 
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, #base above with no shutdown-any-segwit 
                    {'implementation': 'LND', 'version': 'UNKNOWN', 'Qty': 0}, #base above + scid-alias + zero-conf 
                    {'implementation': 'CLN', 'version': 'UNKNOWN','Qty': 0}, #base above + Wumbo
                    {'implementation': 'CLN', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation': 'LDK', 'version': 'UNKNOWN', 'Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},
                    {'implementation':'LND', 'version': 'UNKNOWN','Qty': 0},       
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
                    },
                    {
                     'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                     'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                     'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                     'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                     'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
                     'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                     'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                     'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                     'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                     'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                     'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                     'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                     'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                     'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                     'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                     'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True
                     },
                     {
                      'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                      'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                      'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                      'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                      'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                      'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                      'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True,
                      'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                      'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                      'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                      'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                      'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                      'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True,
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
                      'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                      'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
                      'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                      'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                      'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                      'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                      'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                      'nodes.item.features.181.name': 'simple-taproot-chans-x', 'nodes.item.features.181.is_required': False, 'nodes.item.features.181.is_known': True,
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
                      'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                      'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                      'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True,
                      'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                      },
                      {'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True, 
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
                       'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                       'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                       'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True,
                       'nodes.item.features.181.name': 'simple-taproot-chans-x', 'nodes.item.features.181.is_required': False, 'nodes.item.features.181.is_known': True,
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
                       'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                       'nodes.item.features.25.name': 'unknown', 'nodes.item.features.25.is_required': False, 'nodes.item.features.25.is_known': False,
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
                       'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                       'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True
                        },
                        {
                       'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                       'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                       'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                       'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                       'nodes.item.features.12.name': 'static-remote-key', 'nodes.item.features.12.is_required': True, 'nodes.item.features.12.is_known': True,
                       'nodes.item.features.14.name': 'payment-addr', 'nodes.item.features.14.is_required': True, 'nodes.item.features.14.is_known': True,
                       'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True
                       },
                       {
                       'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                       'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                       'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                       'nodes.item.features.9.name': 'tlv-onion', 'nodes.item.features.9.is_required': False, 'nodes.item.features.9.is_known': True,
                       'nodes.item.features.13.name': 'static-remote-key', 'nodes.item.features.13.is_required': False, 'nodes.item.features.13.is_known': True,
                       'nodes.item.features.15.name': 'payment-addr', 'nodes.item.features.15.is_required': False, 'nodes.item.features.15.is_known': True,
                       'nodes.item.features.17.name': 'multi-path-payments', 'nodes.item.features.17.is_required': False, 'nodes.item.features.17.is_known': True
                       },
                       {
                       'nodes.item.features.0.name': 'data-loss-protect', 'nodes.item.features.0.is_required': True, 'nodes.item.features.0.is_known': True,
                       'nodes.item.features.5.name': 'upfront-shutdown-script', 'nodes.item.features.5.is_required': False, 'nodes.item.features.5.is_known': True,
                       'nodes.item.features.7.name': 'gossip-queries', 'nodes.item.features.7.is_required': False, 'nodes.item.features.7.is_known': True,
                       'nodes.item.features.8.name': 'tlv-onion', 'nodes.item.features.8.is_required': True, 'nodes.item.features.8.is_known': True,
                       'nodes.item.features.11.name': 'unknown', 'nodes.item.features.11.is_required': False, 'nodes.item.features.11.is_known': False,
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
                       'nodes.item.features.19.name': 'wumbo-channels', 'nodes.item.features.19.is_required': False, 'nodes.item.features.19.is_known': True,
                       'nodes.item.features.23.name': 'anchors-zero-fee-htlc-tx', 'nodes.item.features.23.is_required': False, 'nodes.item.features.23.is_known': True,
                       'nodes.item.features.27.name': 'shutdown-any-segwit', 'nodes.item.features.27.is_required': False, 'nodes.item.features.27.is_known': True,
                       'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                       'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                       'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                       'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
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
                       'nodes.item.features.31.name': 'amp', 'nodes.item.features.31.is_required': False, 'nodes.item.features.31.is_known': True,
                       'nodes.item.features.45.name': 'explicit-commitment-type', 'nodes.item.features.45.is_required': False, 'nodes.item.features.45.is_known': True,
                       'nodes.item.features.47.name': 'scid-alias', 'nodes.item.features.47.is_required': False, 'nodes.item.features.47.is_known': True,
                       'nodes.item.features.51.name': 'zero-conf', 'nodes.item.features.51.is_required': False, 'nodes.item.features.51.is_known': True,
                       'nodes.item.features.55.name': 'keysend', 'nodes.item.features.55.is_required': False, 'nodes.item.features.55.is_known': True,
                       'nodes.item.features.259.name': 'unknown', 'nodes.item.features.259.is_required': False, 'nodes.item.features.259.is_known': False,
                       'nodes.item.features.2023.name': 'script-enforced-lease', 'nodes.item.features.2023.is_required': False, 'nodes.item.features.2023.is_known': True
                       }
]