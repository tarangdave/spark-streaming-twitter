# spark-streaming-sample
Sample Spark Streaming

### Setup
> Install Spark (spark 2.3.0 with hadoop 2.7 or later)
> sudo tar -xvzf spark-2.3.0-bin-hadoop2.7.tgz
> Update the ~/.bash-profile with environment varibles
> source ~/.bash-profile
> run pyspark to check if the installation is working proper or not


### Running each file
> On one terminal run nc -l 9999
> On another terminal run spark-submit "filename".py localhost 9999