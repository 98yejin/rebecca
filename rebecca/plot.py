import matplotlib.pyplot as plt

class RebeccaPlot:
    def __init__(self, data, title=None):
        self.data = data
        self.title = title
        self.figure = plt.figure()
        self.subplot = None

    def create_subplot(self):
        if self.data is not None:
            self.subplot = self.figure.add_subplot(111)
            self.subplot.plot(self.data['nums'])
            if self.title:
                self.subplot.set_title(self.title)
        else:
            raise ValueError("Data is required to create a subplot")

    def savefig(self, filename):
        if self.figure:
            self.figure.savefig(filename)
        else:
            raise ValueError("No figure to save")

# Create a global instance of RebeccaPlot
plt = RebeccaPlot(None)

def subplot(data, title=None):
    global plt
    plt = RebeccaPlot(data, title)
    plt.create_subplot()
    return plt

def plot(data, title=None):
    global plt
    plt = RebeccaPlot(data, title)
    plt.create_subplot()
    return plt
