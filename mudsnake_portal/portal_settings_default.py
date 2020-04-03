# Lockdown mode will cut off the game from any external connections
# and only allow connections from localhost. Requires a cold reboot.
LOCKDOWN_MODE = False

# Activate telnet service
TELNET_ENABLED = True


# Telnet interface to listen to. If 0.0.0.0, listen to all. Use :: for IPv6.
TELNET_INTERFACE = "0.0.0.0"
# The port used by Telnet.
TELNET_PORT = 4000

# Same as TELNET_INTERFACE, but uses TLS/SSL for security.
TLS_TELNET_INTERFACE = "0.0.0.0"
TLS_TELNET_PORT = 4001

# Interface for the WebSocket Server to listen to.
WEBSOCKET_INTERFACE = "0.0.0.0"
# Port used by the WebSocket Server.
WEBSOCKET_PORT = 4002

# AMP uses the local interface by default, assuming that all Servers will be local.
# Change this if this assumption is wrong. However, all servers must have the
# pre-shared password if using anything but 127.0.0.1.
AMP_HOST = "localhost"
AMP_PORT = 4003
AMP_INTERFACE = "127.0.0.1"
AMP_PASSWORD = "changemeplz"

