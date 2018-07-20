import plotly.offline as po
import plotly.graph_objs as go

class ggplot(object):
    def __init__(self, data=None):
        """

        :param data (pandas.DataFrame):
        """
        self._data = data
        self._aes = None
        self._geom = None

        po.init_notebook_mode(connected=True)

    def _create_plot(self):
        self.traces = []
        df = self._data
        x = self._aes.x
        y = self._aes.y
        # print(self._geom.name)
        if self._geom.name == "point":
            color = self._aes.color
            if color is not None:
                for c in df[color].unique():
                    temp = df[df[color] == c]
                    self.traces.append(go.Scatter(x=temp[x], y=temp[y],
                                              mode="markers", name=c))
            else:
                self.traces.append(go.Scatter(x=df[x],
                                              y= df[y],
                                              mode="markers"))
        # print(self.traces)
        self.layout = go.Layout()
        self.fig = go.Figure(data=self.traces, layout=self.layout)
        return po.iplot(self.fig)

    def __add__(self, obj):
        class_name = type(obj).__name__
        # print(class_name)

        if class_name == "aes":
            self._aes = obj
            return self

        elif class_name in ["geom", "geom_point"]:
            self._geom = obj

            self.iplot = self._create_plot()
            return self.iplot