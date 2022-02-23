# Profiling and Performance Study

## Introduction

Study on the effect of multiprocessing for loading data into a NoSQL database (MongoDB).
The pandas and multiprocessing library were employed for the load_users and
load_status_updates methods to improve their performance in passing data from a
csv file to a MongoDB collection. Profiling tools (cProfile/pstats) were used to
measure and record performance improvements with multiprocessing implemented.

## Results and Discussion

The Pandas dataframe chunk size was calculated as

<p align="center">
  <img src="/images/chunk.png" alt="Chunk Size" style="height:auto; width:250px;"/>
</p>

where “length of data” is an integer representing the number of rows in the consumed
csv file and “num of **logical** cores” is an integer representing the number of cpu logical
cores available. The above method for calculating the chunk size optimizes the use of
the available hardware as the resulting number of “chunks” is equal to the number of
cores available for multiprocessing. Increasing the chunk size above the number of
cores reduces performance. This is due to the number of chunks being less than the
available logic cores in the cpu leaving a surplus of unused cores for multiprocessing.
Performance was less sensitive to reducing the chunk size as all cores remain active.
However, as the chunk size is further reduced a limit is reached and it is assumed the
increased number of associated processes starts to dominate and nullify any performance
gains made from multiprocessing.

The cumulative time and number of function calls for the baseline and multiprocessing
social network structures are shown in Table 01 and Table 02. The right hand column
shows the percentage of time or function calls for multiprocessing compared to the
baseline. For both metrics, multiprocessing improved performance by an order of
magnitude or more.

<div align="center">Table 1: Cumulative Time</div>
<p align="center">
  <img src="/images/time.png" alt="Cumulative Time" style="height:auto; width:800px;"/>
</p>

<div align="center">Table 2: Total Function Calls</div>
<p align="center">
  <img src="/images/funct_calls.png" alt="Function Calls" style="height:auto; width:800px;"/>
</p>
