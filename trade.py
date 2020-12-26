#!/usr/bin/env python
import sys
import time

from pyiqoptionapi import IQOption

try:
    from env import *
except ImportError:
    pass


class Trade:
    def __init__(self, email=None, password=None):
        email = email or os.environ['IQ_OPTIONS_API_EMAIL']
        password = password or os.environ['IQ_OPTIONS_API_PASSWORD']
        self.option = IQOption(email, password)
        _, reason = self.option.connect()  # connect to iqoption
        if reason:
            raise ConnectionRefusedError(reason)

    def start(self, name, active, _type, buffersize=10, run_time=10):
        print("_____________subscribe_live_deal_______________")
        self.option.subscribe_live_deal(name, active, _type, buffersize)
        start_t = time.time()
        while True:
            # data size is below buffersize
            # data[0] is the last data
            data = self.option.get_live_deal(name, active, _type)
            print(f"Data: {data}")
            time.sleep(1)
            if time.time() - start_t > run_time:
                break
        print("_____________unsubscribe_live_deal_______________")
        self.option.unscribe_live_deal(name, active, _type)


if __name__ == '__main__':
    trade = Trade()
    if len(sys.argv) > 0 and sys.argv[0].strip().lower().startswith('d'):  # 'digital' option is probably expected
        ################################################
        # Option: digital.
        # `name` can be one of: 'live-deal-binary-option-placed', 'live-deal-digital-option'
        # `_type` can be one of: 'PT1M', 'PT5M', 'PT15M'
        ################################################
        trade.start(name="live-deal-digital-option", active="EURUSD", _type="turbo")
    else:  # 'binary' option is implied
        ################################################
        # Option: binary.
        # `_type` can be one of: 'turbo', 'binary'
        ################################################
        trade.start(name="live-deal-binary-option-placed", active="EURUSD", _type="turbo")
