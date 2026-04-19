from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4, tcp

log = core.getLogger()

class TrafficControl(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        ip_packet = packet.find('ipv4')
        tcp_packet = packet.find('tcp')

        # Block HTTP traffic (port 80)
        if ip_packet and tcp_packet:
            if tcp_packet.dstport == 80:
                log.info("Blocking HTTP traffic")

                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.priority = 100
                # No actions = DROP

                self.connection.send(msg)
                return

        # Allow other traffic
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        msg.in_port = event.port

        self.connection.send(msg)

def launch():
    def start_switch(event):
        log.info("New switch connected")
        TrafficControl(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
    log.info("POX Traffic Controller Started")
