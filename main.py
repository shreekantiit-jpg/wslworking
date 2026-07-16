from src.utils import get_spark_session
from src.logger import get_logger
from jobs.daily_transaction_job import run_job


logger = get_logger()

spark = get_spark_session()

logger.info("Reading transaction data")

df = (
    spark.read
         .option("header", True)
         .option("inferSchema", True)
         .csv("data/transactions.csv")
)

result_df = run_job(df)

logger.info("Writing customer summary")

(
    result_df.write
             .mode("overwrite")
             .csv("output/customer_summary")
)

result_df.show()

spark.stop()