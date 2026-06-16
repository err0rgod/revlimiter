import threading
import time

class LeakyBucket:
    def __init__(self, bucket_size,output_packet_size, interval = 1) -> None:
        self.storage = 0
        self.bucket_size = bucket_size
        self.output_packet_size = output_packet_size
        self.running = True
        self.lock = threading.Lock()
        self.interval = interval
        t = threading.Thread(target=self._leak_loop, daemon=True)
        t.start()

    def addRequest(self,no_of_requests : int) -> bool:
        space_left = self.bucket_size - self.storage
        accepted = min(no_of_requests,space_left)
        dropped = no_of_requests - accepted
        
        self.storage+= accepted
        print(f"{accepted} processed out of {no_of_requests} ")
    
    def leak(self):
        self.storage = max(0,self.storage - self.output_packet_size)

    def _leak_loop(self):
        while self.running:
            time.sleep(self.interval)
            self.leak()

    def current_storage(self):
        return self.storage