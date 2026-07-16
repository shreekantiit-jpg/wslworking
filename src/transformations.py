from pyspark.sql.functions import sum


def create_customer_summary(df):

    return (
        df.groupBy("customer_id")
          .agg(
              sum("transaction_amount")
              .alias("total_amount")
          )
    )