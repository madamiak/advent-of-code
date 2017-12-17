class Spinlock(object):
    def next(self, step, iterations=2017):
        buffer = [0]
        current_position = 0
        for index in range(iterations):
            new_position = (current_position + step) % len(buffer)
            new_position += 1
            buffer.insert(new_position, index + 1)
            current_position = new_position
        return buffer[(current_position + 1) % len(buffer)]

    def after_first(self, step, iterations=50000000):
        current_position = 0
        result = None
        for index in range(1, iterations + 1):
            current_position = (current_position + step) % index + 1
            if current_position == 1:
                result = index
        return result
