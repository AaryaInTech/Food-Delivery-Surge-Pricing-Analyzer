import random
from datetime import datetime, timedelta, timezone
from snowflake.snowpark import Session

def main(session: Session):

    #ENSURE CONTEXT (IMPORTANT)
    session.sql("CREATE DATABASE IF NOT EXISTS food_delivery").collect()
    session.sql("CREATE SCHEMA IF NOT EXISTS food_delivery.surge_demo").collect()
    session.sql("USE DATABASE food_delivery").collect()
    session.sql("USE SCHEMA surge_demo").collect()

    #PARAMETERS
    num_orders = 200
    num_locations = 12
    num_surge_locations = 3

    #BUILD LOCATION LIST
    locations = [f"L{n:03d}" for n in range(1, num_locations + 1)]
    surge_locations = random.sample(locations, k=num_surge_locations)

    #GENERATE ORDERS DATA
    now = datetime.now(timezone.utc)
    orders_data = []

    for idx in range(1, num_orders + 1):
        base_loc = random.choice(locations)
        location = random.choice([base_loc, random.choice(surge_locations)])
        event_time = now - timedelta(minutes=random.randint(0,45))
        orders_data.append([
            f"ORD-{idx:05d}",
            location,
            event_time.isoformat(),
            round(random.uniform(150,800),2)
        ])

    # CREATE ORDERS TABLE
    session.sql("""
        CREATE OR REPLACE TABLE orders_snowpark (
            order_id STRING,
            location_id STRING,
            event_time TIMESTAMP,
            order_value FLOAT
        )
    """).collect()

    #INSERT DATA
    orders_df = session.create_dataframe(
        orders_data,
        schema=["order_id","location_id","event_time","order_value"]
    )
    orders_df.write.mode("overwrite").save_as_table("orders_snowpark")

    # ---- RETURN SAMPLE OUTPUT ----
    return session.sql("SELECT * FROM orders_snowpark LIMIT 10")
