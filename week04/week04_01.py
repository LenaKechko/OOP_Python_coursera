EVENT_GET, EVENT_SET = "EventGet", "EventSet"
INT_TYPE, FLOAT_TYPE, STR_TYPE = "int", "float", "str"


# class SomeObject:
#     def __init__(self):
#         self.integer_field = 0
#         self.float_field = 0.0
#         self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.name_event = "EventGet"
        self.kind = {int: INT_TYPE, float: FLOAT_TYPE, str: STR_TYPE}[kind]


class EventSet:
    def __init__(self, value):
        self.name_event = "EventSet"
        self.value = value
        self.kind = {int: INT_TYPE, float: FLOAT_TYPE, str: STR_TYPE}[type(value)]


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == INT_TYPE:
            if event.name_event == EVENT_GET:
                return obj.integer_field
            elif event.name_event == EVENT_SET:
                obj.integer_field = event.value
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == FLOAT_TYPE:
            if event.name_event == EVENT_GET:
                return obj.float_field
            elif event.name_event == EVENT_SET:
                obj.float_field = event.value
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == STR_TYPE:
            if event.name_event == EVENT_GET:
                return obj.string_field
            elif event.name_event == EVENT_SET:
                obj.string_field = event.value
        else:
            return super().handle(obj, event)


# obj = SomeObject()
# obj.integer_field = 42
# obj.float_field = 3.14
# obj.string_field = "some text"
# chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
# print(chain.handle(obj, EventGet(int)))
# # 42
# print(chain.handle(obj, EventGet(float)))
# # 3.14
# print(chain.handle(obj, EventGet(str)))
# # 'some text'
# chain.handle(obj, EventSet(100))
# print(chain.handle(obj, EventGet(int)))
# # 100
# chain.handle(obj, EventSet(0.5))
# print(chain.handle(obj, EventGet(float)))
# # 0.5
# chain.handle(obj, EventSet('new text'))
# print(chain.handle(obj, EventGet(str)))
# # 'new text'
