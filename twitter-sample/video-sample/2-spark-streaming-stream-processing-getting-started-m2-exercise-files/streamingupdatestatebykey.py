import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="StreamingWordCount")
    ssc = StreamingContext(sc, 30)

    ssc.checkpoint("file:///tmp/spark")

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

    def countWords(newValues, lastSum):
      if lastSum is None:
        lastSum = 0
      return sum(newValues, lastSum)  

    word_counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .updateStateByKey(countWords)

    word_counts.pprint()

    ssc.start()
    ssc.awaitTermination()
