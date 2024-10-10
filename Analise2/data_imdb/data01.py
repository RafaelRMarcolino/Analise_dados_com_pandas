from faker import Faker
import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

spark = SparkSession.builder.appName('').getOrCreate()

# Inicializando o Faker
fake = Faker()

# Função para gerar dados fictícios
def generate_data(num_entries):
    data = []
    for _ in range(num_entries):
        nconst = f"nm{str(random.randint(1, 300)).zfill(7)}"
        primaryName = fake.name()
        birthYear = random.randint(1900, 2000)
        deathYear = random.choice([fake.year() for _ in range(10)])  # escolha aleatória de ano ou None
        primaryProfession = ",".join(random.sample(["actor", "actress", "writer", "director", "producer", "music_department", "editor", "miscellaneous", "soundtrack", "archive_footage"], random.randint(1, 5)))
        knownForTitles = ",".join([f"tt{str(random.randint(1000000, 9999999)).zfill(7)}" for _ in range(4)])

        data.append({
            "nconst": nconst,
            "primaryName": primaryName,
            "birthYear": birthYear,
            "deathYear": deathYear if random.random() > 0.2 else None,  
            "primaryProfession": primaryProfession,
            "knownForTitles": knownForTitles
        })
    return data

# Gerando 300 registros
fake_data = generate_data(300)


df = spark.createDataFrame(fake_data)

df.show(truncate=False)

df_order = df.orderBy(desc('nconst'))

df_order.show(truncate=False)


