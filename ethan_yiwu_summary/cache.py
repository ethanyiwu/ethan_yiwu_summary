## cache.py
from collections import OrderedDict

class Cache:
    def __init__(self, capacity: int = 100):
        """
        Initialize the cache with a given capacity. Default capacity is set to 100.

        :param capacity: Maximum number of entries in the cache.
        """
        self.cache_storage = OrderedDict()
        self.capacity = capacity

    def get_cached_summary(self, url: str) -> str:
        """
        Retrieve a cached summary based on the URL if it exists and move it to the end to indicate recent use.

        :param url: The URL of the content to summarize.
        :return: The cached summary or None if not found.
        """
        summary = self.cache_storage.get(url)
        if summary:
            self.cache_storage.move_to_end(url)
        return summary

    def cache_summary(self, url: str, summary: str) -> None:
        """
        Cache a summary for a given URL and ensure the cache does not exceed its capacity.
        If the URL is already in the cache, move it to the end to indicate recent use.
        If the cache is full, remove the least recently used item.

        :param url: The URL of the content to summarize.
        :param summary: The summary to cache.
        """
        if url in self.cache_storage:
            self.cache_storage.move_to_end(url)
        self.cache_storage[url] = summary
        if len(self.cache_storage) > self.capacity:
            self.cache_storage.popitem(last=False)

    def clear_cache(self) -> None:
        """
        Clear the entire cache.
        """
        self.cache_storage.clear()

    def remove_from_cache(self, url: str) -> None:
        """
        Remove a specific entry from the cache based on the URL.

        :param url: The URL of the content to remove from the cache.
        """
        self.cache_storage.pop(url, None)
