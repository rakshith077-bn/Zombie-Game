from pyspark import SparkContext

spark_context = SparkContext("local", "Assingment 3")

# With UTF-8 encoding
words = spark_context.textFile("input.txt", 1, use_unicode=False).map(lambda line: line.decode('utf-8', 'replace'))

words_per_se = words.flatMap(lambda line: line.split(" "))

single_words = words_per_se.map(lambda word: (word, 1))

word_count = single_words.reduceByKey(lambda a, b: a + b)

print("Word count")
for (word, count) in word_count.collect():
    print(f"{word}: {count}")

decending_words = word_count.sortBy(lambda x: x[1], ascending=False)

print(" ")
print(" ")
print("Repeated words")
for (word, count) in decending_words.take(10):
    print(f"{word}: {count}")

m_words = word_count.filter(lambda x: x[0].lower().startswith('m')).distinct()

print(" ")
print(" ")
print("Words Starting with 'm'")
for (word, count) in m_words.collect():
    print(word)

spark_context.stop()
