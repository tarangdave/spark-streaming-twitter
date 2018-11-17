import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="StreamingWindowSum")
    ssc = StreamingContext(sc, 2)
    
    ssc.checkpoint("file:///tmp/spark")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

    sum = lines.reduceByWindow(
           lambda x, y: int(x) + int(y), 
    	   lambda x, y: int(x) - int(y),
    	   10, 2)


    sum.pprint()
    ssc.start()
    ssc.awaitTermination()
