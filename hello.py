class Dinglemouse(object):

    def __init__(self):
        self.attributes = {}  # Dictionary to store attribute values
        self.attribute_order = []  # List to store attribute order

    def setAge(self, age):
        self._set_attribute("age", age)
        return self

    def setSex(self, sex):
        self._set_attribute("sex", sex)
        return self

    def setName(self, name):
        self._set_attribute("name", name)
        return self

    def _set_attribute(self, attribute_name, value):
        if attribute_name not in self.attributes:
            self.attribute_order.append(attribute_name)
        self.attributes[attribute_name] = value

    def hello(self):
        output = "Hello."
        for attribute_name in self.attribute_order:
            if attribute_name == "name":
                output += f" My name is {self.attributes['name']}."
            elif attribute_name == "age":
                output += f" I am {self.attributes['age']}."
            elif attribute_name == "sex":
                output += f" I am {'male' if self.attributes['sex'] == 'M' else 'female'}."
        return output