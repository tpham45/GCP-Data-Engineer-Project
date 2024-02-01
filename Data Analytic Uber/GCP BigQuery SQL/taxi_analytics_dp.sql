
--Create Trip Duration first
CREATE OR REPLACE TABLE `taxi-project-412919.taxi_dataanalytics_project.trip_duration` AS (
 SELECT
    d.datetimeindex_id,
    d.drop_datetime,
    d.pick_datetime,
    CAST(d.pick_datetime AS TIMESTAMP) AS pickup_timestamp,
    CAST(d.drop_datetime AS TIMESTAMP) AS dropoff_timestamp,
    -- Extract the hour and minute from the pickup and dropoff timestamps
    FORMAT_TIMESTAMP('%H:%M', CAST(d.pick_datetime AS TIMESTAMP)) AS pickup_time,
    FORMAT_TIMESTAMP('%H:%M', CAST(d.drop_datetime AS TIMESTAMP)) AS dropoff_time
  FROM
    `taxi-project-412919.taxi_dataanalytics_project.dim_datetime` d
)


--Create taxi_analytics second
CREATE OR REPLACE TABLE `taxi-project-412919.taxi_dataanalytics_project.taxi_analytics` AS (
  SELECT 
    f.trip_id,
    d.pick_datetime,
    td.pickup_time,
    d.drop_datetime,
    td.dropoff_time,
    TIMESTAMP_DIFF(td.dropoff_timestamp, td.pickup_timestamp, MINUTE) AS trip_duration_minutes,
    f.passenger_count,
    f.trip_distance,
    l.PUlocationCode AS pickup_location_code,
    l.DOlocationCode AS dropoff_location_code,
    v.vendor_type,
    r.ratecode_name,
    p.payment_type_name,
    f.fare_amount,
    f.extra,
    f.mta_tax,
    f.tip_amount,
    f.tolls_amount,
    f.improvement_surcharge,
    f.congestion_surcharge,
    f.Airport_fee,
    f.total_amount
  FROM 
    `taxi-project-412919.taxi_dataanalytics_project.fact_trip` f

  JOIN `taxi-project-412919.taxi_dataanalytics_project.dim_datetime` d ON f.datetimeindex_id = d.datetimeindex_id
  JOIN `taxi-project-412919.taxi_dataanalytics_project.dim_ratecode` r ON f.ratecodeindex_id = r.ratecodeindex_id 
  JOIN `taxi-project-412919.taxi_dataanalytics_project.dim_location` l ON f.locationindex_id = l.locationindex_id
  JOIN `taxi-project-412919.taxi_dataanalytics_project.dim_payment_type` p ON f.payment_typeindex_id = p.payment_typeindex_id
  JOIN `taxi-project-412919.taxi_dataanalytics_project.dim_vendor` v ON f.vendorindex_id = v.vendorindex_id
  JOIN `taxi-project-412919.taxi_dataanalytics_project.trip_duration` td ON f.datetimeindex_id = td.datetimeindex_id
)

