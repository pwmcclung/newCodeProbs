from preloaded import DuplicateFromError, DuplicateSelectError, DuplicateGroupByError, DuplicateOrderByError


class Query:
    def __init__(self):
        self._from_tables = None
        self._select_func = None
        self._where_conditions = []
        self._group_by_funcs = None
        self._having_conditions = []
        self._order_by_func = None
        self._from_called = False
        self._select_called = False
        self._group_by_called = False
        self._order_by_called = False
    
    def from_(self, *tables):
        if self._from_called:
            raise DuplicateFromError()
        self._from_called = True
        self._from_tables = tables
        return self
    
    def select(self, func=None):
        if self._select_called:
            raise DuplicateSelectError()
        self._select_called = True
        self._select_func = func
        return self
    
    def where(self, *conditions):
        self._where_conditions.append(conditions)
        return self
    
    def group_by(self, *funcs):
        if self._group_by_called:
            raise DuplicateGroupByError()
        self._group_by_called = True
        self._group_by_funcs = funcs
        return self
    
    def having(self, *conditions):
        self._having_conditions.append(conditions)
        return self
    
    def order_by(self, func):
        if self._order_by_called:
            raise DuplicateOrderByError()
        self._order_by_called = True
        self._order_by_func = func
        return self
    
    def execute(self):
        result = []
        if self._from_tables:
            if len(self._from_tables) == 1:
                result = list(self._from_tables[0])
            else:
                result = []
                def cartesian_product(tables, current_combo=[]):
                    if not tables:
                        result.append(current_combo)
                        return
                    for item in tables[0]:
                        cartesian_product(tables[1:], current_combo + [item])
                
                cartesian_product(self._from_tables)
        for where_group in self._where_conditions:
            result = [item for item in result if any(condition(item) for condition in where_group)]
        if self._group_by_funcs:
            result = self._group_by(result, self._group_by_funcs)
        if self._group_by_funcs:  
            for having_group in self._having_conditions:
                result = [group for group in result if any(condition(group) for condition in having_group)]
        if self._select_func:
            result = [self._select_func(item) for item in result]
        if self._order_by_func:
            from functools import cmp_to_key
            result.sort(key=cmp_to_key(self._order_by_func))
        
        return result
    
    def _group_by(self, data, funcs):
        if not funcs:
            return data
        
        func = funcs[0]
        remaining_funcs = funcs[1:]
        
        groups = {}
        for item in data:
            key = func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        
        result = []
        for key, group in groups.items():
            if remaining_funcs:
                subgroups = self._group_by(group, remaining_funcs)
                result.append([key, subgroups])
            else:
                result.append([key, group])
        
        return result

def query():
    return Query()