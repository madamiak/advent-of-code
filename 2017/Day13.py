import itertools


class PacketScanners(object):
    def enter_firewall(self, puzzle):
        rows = [row.split(': ') for row in str.split(puzzle, '\n')]
        scanners = {int(depth): int(range) - 1 for depth, range in rows}
        immediate_severity = 0
        for delay in itertools.count():
            severity = 0
            caught = False
            for time in scanners:
                if self._current_position(scanners[time], time + delay) == 0:
                    severity += time * (scanners[time] + 1)
                    caught = True
            if delay == 0:
                immediate_severity = severity
            if not caught:
                break
        return immediate_severity, delay

    def _current_position(self, range, time):
        offset = time % (range * 2)
        if offset > range:
            return 2 * range - offset
        else:
            return offset
