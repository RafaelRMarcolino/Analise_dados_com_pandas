from faker import Faker
import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

spark = SparkSession.builder.appName('').getOrCreate()

sexo = {0: 'Masculino',
        1: 'Feminino'}

cor = {0: 'Indigena',
       1: 'Branca',
       3: 'Preta',
       4: 'Amarela',
       5: 'Parda',
       6: 'Sem Declaração'}



def fake_renda(num):
    data = []
    for _ in range(num):
        renda = f"nm{str(random.randint(1, 300)).zfill(7)}"

