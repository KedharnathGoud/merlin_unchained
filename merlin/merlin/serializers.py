from rest_framework import serializers
from .models import Devices, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

class DevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devices
        fields = ('hostname', 'alias', 'device_type', 'os', 'username', 'protocol', 'ip_address', 'port', 'connection_timeout', 'timestamp')

class LearnACLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnACL
        fields = ('pyats_alias', 'os', 'acl', 'ace', 'permission', 'logging', 'source_network', 'destination_network', 'l3_protocol', 'l4_protocol', 'operator', 'port', 'timestamp')

class LearnARPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnARP
        fields = ('pyats_alias', 'os', 'interface', 'neighbor_ip', 'neighbor_mac', 'origin', 'local_proxy', 'proxy', 'timestamp')

class LearnARPStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnARPStatistics
        fields = ('pyats_alias', 'os', 'entries_total', 'in_drops', 'incomplete_total', 'timestamp')

class LearnBGPInstancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnBGPInstances
        fields = ('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'neighbor_counters_received_bytes_in_queue', 'neighbor_counters_received_capability', 'neighbor_counters_received_keepalives', 'neighbor_counters_received_notifications', 'neighbor_counters_received_opens', 'neighbor_counters_received_route_refresh', 'neighbor_counters_received_total', 'neighbor_counters_received_total_bytes', 'neighbor_counters_received_updates', 'neighbor_counters_sent_bytes_in_queue', 'neighbor_counters_sent_capability', 'neighbor_counters_sent_keepalives', 'neighbor_counters_sent_notifications', 'neighbor_counters_sent_opens', 'neighbor_counters_sent_route_refresh', 'neighbor_counters_sent_total', 'neighbor_counters_sent_total_bytes', 'neighbor_counters_sent_updates', 'last_reset', 'reset_reason', 'timestamp')

class LearnBGPRoutesPerPeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnBGPRoutesPerPeer
        fields = ('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as', 'timestamp')

class LearnBGPTablesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnBGPTables
        fields = ('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight', 'timestamp')

class LearnVLANSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnVLAN
        fields = ('pyats_alias', 'os', 'vlan', 'interfaces', 'mode', 'name', 'shutdown', 'state', 'timestamp')

class LearnVRFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnVRF
        fields = ('pyats_alias', 'os', 'vrf', 'address_family_ipv4', 'address_family_ipv6', 'route_distinguisher', 'timestamp')

class ParseShowInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowInventory
        fields = ('pyats_alias', 'os', 'part', 'description', 'pid', 'serial_number', 'timestamp')

class ParseShowIPIntBriefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowIPIntBrief
        fields = ('pyats_alias', 'os', 'interface', 'interface_status', 'ip_address', 'timestamp')

class ParseShowVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowVersion
        fields = ('pyats_alias', 'bootflash', 'chassis', 'cpu', 'device_name', 'memory', 'model', 'processor_board_id', 'rp', 'slots', 'days', 'hours', 'minutes', 'seconds', 'name', 'os', 'reason', 'system_compile_time', 'system_image_file', 'system_version', 'chassis_sn', 'compiled_by', 'curr_config_register', 'image_id', 'image_type', 'label', 'license_level', 'license_type', 'non_volatile', 'physical', 'next_reload_license_level', 'platform', 'processor_type', 'returned_to_rom_by', 'rom', 'rtr_type', 'uptime', 'uptime_this_cp', 'version_short', 'xe_version', 'timestamp')