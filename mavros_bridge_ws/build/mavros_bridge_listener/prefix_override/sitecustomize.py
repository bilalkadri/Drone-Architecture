import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aeel/mavros_bridge_ws/install/mavros_bridge_listener'
