from Double_Linked_Lists import Double_LL

class PositionalList(Double_LL.Double_LL):
    class Position:
        def __init__(self,container,node):
            self.container = container
            self.node = node
        def element(self):
            return self.node.element
        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node
        def __ne__(self, other):
            return not (self==other)

    def validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node
    def make_position(self,node):
        if node is self.header or node is self.trailer:
            return None
        else:
            return self.Position(self,node)
    def first(self):
        return self.make_position(self.header.next)
    def before(self,p):
        node = self.validate(p)
        return self.make_position(node.prev)
    def after(self,p):
        node = self.validate(p)
        return self.make_position(node.next)
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self,e,predecessor,successor):
        node = super().insertBetween(e,predecessor,successor)
        return self.make_position(node)
    def add_first(self,e):
        return self.insert_between(e,self.header,self.header.next)
    def add_last(self,e):
        return self.insert_between(e,self.trailer.prev,self.trailer)
    def add_before(self,p,e):
        original = self.validate(p)
        return self.insert_between(e,original.prev,original)
    def add_after(self,p,e):
        original = self.validate(p)
        return self.insert_between(e,original,original.next)

    def delete(self,p):
        original = self.validate(p)
        return super().deleteNode(original)

    def replace(self,p,e):
        original =  self.validate(p)
        old_value = original.element
        original.element =e
        return old_value

p = PositionalList()
p.add_first(1)
p.add_last(3)
p.add_first(2)




