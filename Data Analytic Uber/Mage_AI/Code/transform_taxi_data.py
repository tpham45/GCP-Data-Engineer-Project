import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    # Create trip_index_id for the data source for reference
    df.insert(0, 'trip_index_id', df.index)

    # Create Dim_Datetime table
    dim_datetime = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].reset_index(drop=True)
    dim_datetime['datetimeindex_id'] = dim_datetime.index
    dim_datetime['pick_datetime'] = pd.to_datetime(dim_datetime['tpep_pickup_datetime'])
    dim_datetime['pick_hour'] = pd.to_datetime(dim_datetime['tpep_pickup_datetime']).dt.hour
    dim_datetime['pick_day'] = pd.to_datetime(dim_datetime['tpep_pickup_datetime']).dt.day
    dim_datetime['pick_month'] = pd.to_datetime(dim_datetime['tpep_pickup_datetime']).dt.month
    dim_datetime['pick_year'] = pd.to_datetime(dim_datetime['tpep_pickup_datetime']).dt.year
    dim_datetime['pick_weekday'] = pd.to_datetime(dim_datetime['tpep_pickup_datetime']).dt.weekday
    dim_datetime['drop_datetime']= pd.to_datetime(dim_datetime['tpep_dropoff_datetime'])
    dim_datetime['drop_hour'] = pd.to_datetime(dim_datetime['tpep_dropoff_datetime']).dt.hour
    dim_datetime['drop_day'] = pd.to_datetime(dim_datetime['tpep_dropoff_datetime']).dt.day
    dim_datetime['drop_month'] = pd.to_datetime(dim_datetime['tpep_dropoff_datetime']).dt.month
    dim_datetime['drop_year'] = pd.to_datetime(dim_datetime['tpep_dropoff_datetime']).dt.year
    dim_datetime['drop_weekday'] = pd.to_datetime(dim_datetime['tpep_dropoff_datetime']).dt.weekday
    dim_datetime = dim_datetime[[
                                'datetimeindex_id', 'pick_datetime', 'pick_hour', 'pick_day', 
                                'pick_month', 'pick_year', 'pick_weekday',
                                'drop_datetime', 'drop_hour', 'drop_day', 
                                'drop_month', 'drop_year', 'drop_weekday'
                                ]]

    #Create Dim_Ratecode table
    rate_code_type = {
        1: 'Standard Rate',
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group Ride"
    }
    dim_ratecode = df[['RatecodeID']].reset_index(drop=True)
    dim_ratecode['ratecodeindex_id'] = dim_ratecode.index
    dim_ratecode['ratecode_id'] = dim_ratecode ['RatecodeID']
    dim_ratecode['ratecode_name'] = dim_ratecode ['RatecodeID'].map(rate_code_type)
    dim_ratecode = dim_ratecode [[
                                    'ratecodeindex_id','ratecode_id','ratecode_name'
                                ]]

    #Create Dim_Payment_type table
    payment_type_name = {
        1:"Credit card",
        2:"Cash",
        3:"No charge",
        4:"Dispute",
        5:"Unknown",
        6:"Voided trip"
    }
    dim_payment_type = df[['payment_type']].reset_index(drop=True)
    dim_payment_type['payment_typeindex_id'] = dim_payment_type.index
    dim_payment_type['payment_type_id'] = dim_payment_type ['payment_type']
    dim_payment_type['payment_type_name'] = dim_payment_type['payment_type'].map(payment_type_name)
    dim_payment_type = dim_payment_type[[
                                            'payment_typeindex_id','payment_type_id','payment_type_name'
                                        ]]

    #Create Dim_Store_and-FWD_Flag table
    store_and_fwd_flag = {
        'Y': 'store and forward trip',
        'N': 'Not a store and forward trip'
    }

    dim_store_and_fwd_flag = df [['store_and_fwd_flag']].reset_index(drop=True)
    dim_store_and_fwd_flag ['store_and_fwd_flag_index_id'] = dim_store_and_fwd_flag.index
    dim_store_and_fwd_flag ['store_and_fwd_flag_id'] = dim_store_and_fwd_flag ['store_and_fwd_flag']
    dim_store_and_fwd_flag ['store_and_fwd_flag_type'] = dim_store_and_fwd_flag['store_and_fwd_flag'].map (store_and_fwd_flag)
    dim_store_and_fwd_flag = dim_store_and_fwd_flag [[
                                                        'store_and_fwd_flag_index_id','store_and_fwd_flag_id','store_and_fwd_flag_type'
                                                    ]]

    #Create Dim_Vendor table
    vendor_type_list = {
        1: 'Creative Mobile Technologies,LLC',
        2: 'Verifone Inc'
    }

    dim_vendor = df [['VendorID']].reset_index(drop=True)
    dim_vendor ['vendorindex_id'] = dim_vendor.index
    dim_vendor ['vendor_type'] = dim_vendor ['VendorID'].map(vendor_type_list)
    dim_vendor ['vendor_id']  = dim_vendor ['VendorID']
    dim_vendor = dim_vendor [['vendorindex_id','vendor_id','vendor_type']]

    #Create Dim_Location table
    dim_location = df[['PULocationID', 'DOLocationID']].reset_index(drop=True)
    dim_location['locationindex_id'] = dim_location.index
    dim_location['PUlocationCode'] = dim_location['PULocationID'] 
    dim_location['DOlocationCode'] = dim_location['DOLocationID']
    dim_location = dim_location[['locationindex_id', 'PUlocationCode', 'DOlocationCode']]

    #Create Fact_Trip table
    fact_trip= pd.DataFrame()
    fact_trip['trip_id'] = df.index
    fact_trip = fact_trip.merge (dim_ratecode,left_on='trip_id',right_on='ratecodeindex_id')\
                     .merge (dim_payment_type,left_on='trip_id',right_on='payment_typeindex_id')\
                     .merge (dim_store_and_fwd_flag,left_on='trip_id',right_on='store_and_fwd_flag_index_id')\
                     .merge (dim_vendor,left_on='trip_id',right_on='vendorindex_id')\
                     .merge (dim_datetime,left_on='trip_id',right_on='datetimeindex_id')\
                     .merge (dim_location,left_on='trip_id',right_on='locationindex_id')\
                     .merge (df, left_on='trip_id', right_on='trip_index_id')
    fact_trip = fact_trip [[
                        
                            'trip_id','vendorindex_id','datetimeindex_id','locationindex_id','ratecodeindex_id',
                            'payment_typeindex_id','store_and_fwd_flag_id','passenger_count','trip_distance',
                            'fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge',
                            'congestion_surcharge','Airport_fee','total_amount'
                       
                          ]]


    return {
        "dim_datetime":dim_datetime.to_dict(orient="dict"),
        "dim_ratecode":dim_ratecode.to_dict(orient="dict"),
        "dim_payment_type":dim_payment_type.to_dict(orient="dict"),
        "dim_store_and_fwd_flag":dim_store_and_fwd_flag.to_dict(orient="dict"),
        "dim_vendor":dim_vendor.to_dict(orient="dict"),
        "dim_location":dim_location.to_dict(orient="dict"),
        "fact_trip":fact_trip.to_dict(orient="dict")}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
