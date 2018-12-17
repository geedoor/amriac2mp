class Stats:
    def __init__(self, api, struct):
        self.api = api
        self._struct = struct

    @property
    def download_speed(self):
        # Overall download speed (byte/sec).
        return self._struct.get("downloadSpeed")

    @property
    def upload_speed(self):
        # Overall upload speed(byte/sec).
        return self._struct.get("uploadSpeed")

    @property
    def num_active(self):
        # The number of active downloads.
        return self._struct.get("numActive")

    @property
    def num_waiting(self):
        # The number of waiting downloads.
        return self._struct.get("numWaiting")

    @property
    def num_stopped(self):
        # The number of stopped downloads in the current session. This value is capped by the
        # --max-download-result option.
        return self._struct.get("numStopped")

    @property
    def num_stopped_total(self):
        # The number of stopped downloads in the current session and not capped by the
        # --max-download-result option.
        return self._struct.get("numStoppedTotal")
