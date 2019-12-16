from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("result_smr").getOrCreate()
    df1 = spark.read.load("hdfs:///user/maria_dev/project/prj_15_smr.csv", format="csv", sep=",", inferSchema="true", header="true")
    df2 = spark.read.load("hdfs:///user/maria_dev/project/prj_16_smr.csv", format="csv", sep=",", inferSchema="true", header="true")
    df3 = spark.read.load("hdfs:///user/maria_dev/project/prj_17_smr.csv", format="csv", sep=",", inferSchema="true", header="true")
    df4 = spark.read.load("hdfs:///user/maria_dev/project/prj_18_smr.csv", format="csv", sep=",", inferSchema="true", header="true")
    df5 = spark.read.load("hdfs:///user/maria_dev/project/prj_19_smr.csv", format="csv", sep=",", inferSchema="true", header="true")

    df1.createOrReplaceTempView("wordcount1")
    df2.createOrReplaceTempView("wordcount2")
    df3.createOrReplaceTempView("wordcount3")
    df4.createOrReplaceTempView("wordcount4")
    df5.createOrReplaceTempView("wordcount5")

    result1 = spark.sql("""
        SELECT word, count(count) as cnt
        FROM wordcount1
        GROUP BY word
        ORDER BY cnt DESC
        LIMIT 10
      """)
    result1.write \
        .format('com.databricks.spark.csv') \
        .option("delimiter",",") \
        .mode("overwrite") \
        .save("hdfs:///user/maria_dev/project/result_smr_15.csv")

    result2 = spark.sql("""
        SELECT word, count(count) as cnt
        FROM wordcount2
        GROUP BY word
        ORDER BY cnt DESC
        LIMIT 10
      """)
    result2.write \
        .format('com.databricks.spark.csv') \
        .option("delimiter",",") \
        .mode("overwrite") \
        .save("hdfs:///user/maria_dev/project/result_smr_16.csv")

    result3 = spark.sql("""
        SELECT word, count(count) as cnt
        FROM wordcount3
        GROUP BY word
        ORDER BY cnt DESC
        LIMIT 10
      """)
    result3.write \
        .format('com.databricks.spark.csv') \
        .option("delimiter",",") \
        .mode("overwrite") \
        .save("hdfs:///user/maria_dev/project/result_smr_17.csv")

    result4 = spark.sql("""
        SELECT word, count(count) as cnt
        FROM wordcount4
        GROUP BY word
        ORDER BY cnt DESC
        LIMIT 10
      """)
    result4.write \
        .format('com.databricks.spark.csv') \
        .option("delimiter",",") \
        .mode("overwrite") \
        .save("hdfs:///user/maria_dev/project/result_smr_18.csv")

    result5 = spark.sql("""
        SELECT word, count(count) as cnt
        FROM wordcount5
        GROUP BY word
        ORDER BY cnt DESC
        LIMIT 10
      """)
    result5.write \
        .format('com.databricks.spark.csv') \
        .option("delimiter",",") \
        .mode("overwrite") \
        .save("hdfs:///user/maria_dev/project/result_smr_19.csv")
