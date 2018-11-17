# spark-streaming-sample
Sample Spark Streaming

### Setup
1. Install Spark (spark 2.3.0 with hadoop 2.7 or later)
2. ```sudo tar -xvzf spark-2.3.0-bin-hadoop2.7.tgz```
3. Update the ```~/.bash-profile``` with environment varibles
4. run ```source ~/.bash-profile```
5. run ```pyspark``` to check if the installation is working proper or not


### Running each file
1. On one terminal run ```nc -l 9999```
2. On another terminal run ```spark-submit "filename".py localhost 9999```
