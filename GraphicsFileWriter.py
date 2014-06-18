#!/usr/bin.python3
from abc import ABCMeta, abstractmethod
import json
import matplotlib


class AbstractGraphicsFileWriter(metaclass=ABCMeta):

    graphsTypes = (
        'barPlot',
        'boxPlot',
        'histogram',
        'linePlot',
        'piePlot',
        'scatter',
        'stackedArea'
    )

    def __init__(self, data, xAxis, yAxis, chartType):
        """
        Parameters
        -----------------------------------
        data: json encoded data that is to be visualized
        xAxis: The name of the xAxis
        yAxis: The name of the yAxis
        type: The type related to the type of visualization model
        """
        self.data = json.loads(data)
        self.xAxis = xAxis
        self.yAxis = yAxis
        if chartType in AbstractGraphicsFileWriter.graphsTypes:
            self.chartType = chartType

    @abstractmethod
    def write(self):
        pass


class RGraphicsFileWriter(AbstractGraphicsFileWriter):
    """
    docstring for RGraphicsFileWriter
    """

    def __init__(self, data, xAxis, yAxis, chartType):
        AbstractGraphicsFileWriter.__init__(self, data, xAxis, yAxis, chartType)

    def write(self):
        with open('test.txt', 'w') as f:
            f.write('Hello')


class PythonGraphicsFileWriter(AbstractGraphicsFileWriter):
    """
    docstring for PythonGraphicsFileWriter
    """

    def __init__(self, data, xAxis, yAxis, chartType):
        super.__init__(self, data, xAxis, yAxis, chartType)

    def write(self):
        pass


