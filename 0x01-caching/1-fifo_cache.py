#!/usr/bin/python3
""" 1-fifo_cache.py """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache """

    def put(self, key, item):
        """ put function """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
                del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """ get function """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
