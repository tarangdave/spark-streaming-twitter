import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="StreamingWindowCount")
    ssc = StreamingContext(sc, 2)

    ssc.checkpoint("file:///tmp/spark")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

    counts = lines.countByWindow(10, 2)

    counts.pprint()

    ssc.start()
    ssc.awaitTermination()
