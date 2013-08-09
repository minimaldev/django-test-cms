from django.db import models
from caching.base import CachingMixin, CachingManager, CachingQuerySet
FETCH_BY_ID=True
class CachedManager(CachingManager):
    
    def __init__(self, *args, **kwargs):
        self.timeout = kwargs.pop('cache_timeout', None)
        self.default_from_cache = kwargs.pop('default_from_cache', False)
        super(CachedManager, self).__init__(*args, **kwargs)
    
    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)
 
    def get_query_set(self):
        return CachedQuerySet(self.model, timeout=self.timeout, default_from_cache=self.default_from_cache)
 
 
class CachedQuerySet(CachingQuerySet):
    
    def __init__(self, *args, **kwargs):
        new_timeout = kwargs.pop('timeout', None)
        self._retrieve_from_cache = kwargs.pop('default_from_cache', False)
        super(CachedQuerySet, self).__init__(*args, **kwargs)
        self.timeout = new_timeout
        
    def _clone(self, *args, **kw):
        qs = super(CachingQuerySet, self)._clone(*args, **kw)
        qs._retrieve_from_cache = self._retrieve_from_cache
        return qs
    
    def from_cache(self, **kwargs):
        self._retrieve_from_cache = True
        return self
 
    def skip_cache(self, **kwargs):
        self._retrieve_from_cache = False
        return self
 
    def iterator(self):
        from_cache = self._retrieve_from_cache
        iterator = super(CachingQuerySet, self).iterator
        if not from_cache:
            return iter(iterator())
        else:
            try:
                # Work-around for Django #12717.
                query_string = self.query_key()
            except query.EmptyResultSet:
                return iterator()
            if FETCH_BY_ID:
                iterator = self.fetch_by_id
            return iter(CacheMachine(query_string, iterator, self.timeout))