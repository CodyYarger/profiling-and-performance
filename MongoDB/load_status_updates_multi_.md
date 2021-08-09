         67004452 function calls (66204452 primitive calls) in 285.553 seconds

   Ordered by: cumulative time
   List reduced from 204 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.509    2.509  285.553  285.553 main.py:72(load_status_updates)
   200000    2.610    0.000  263.429    0.001 collection.py:654(insert_one)
   200000    1.278    0.000  253.170    0.001 collection.py:608(_insert)
   200000    3.807    0.000  250.641    0.001 collection.py:559(_insert_one)
   200000    1.789    0.000  234.672    0.001 mongo_client.py:1495(_retryable_write)
   200000    1.490    0.000  207.525    0.001 mongo_client.py:1374(_retry_with_session)
   200000    3.900    0.000  204.175    0.001 mongo_client.py:1386(_retry_internal)
   200000    1.857    0.000  128.385    0.001 collection.py:578(_insert_command)
   200000    4.200    0.000  124.770    0.001 pool.py:612(command)
   200000    6.008    0.000  110.371    0.001 network.py:43(command)
   200000    2.615    0.000   60.978    0.000 network.py:186(receive_message)
1800002/1400002    5.250    0.000   59.605    0.000 {built-in method builtins.next}
   400000    3.322    0.000   54.573    0.000 network.py:279(_receive_data_on_socket)
   400000   50.555    0.000   50.555    0.000 {method 'recv_into' of '_socket.socket' objects}
   400000    3.092    0.000   33.548    0.000 mongo_client.py:1243(_get_socket)
600000/400000    1.656    0.000   32.818    0.000 contextlib.py:108(__enter__)
   200000    1.985    0.000   31.287    0.000 mongo_client.py:1257(_select_server)
600000/400000    2.120    0.000   26.577    0.000 contextlib.py:117(__exit__)
   200000    3.452    0.000   22.401    0.000 message.py:692(_op_msg)
   400000    1.624    0.000   22.311    0.000 pool.py:1204(get_socket)
   400000    1.280    0.000   21.323    0.000 mongo_client.py:1821(_tmp_session)
   200000    1.098    0.000   15.799    0.000 topology.py:236(select_server)
   200000    0.923    0.000   14.867    0.000 database.py:278(__getattr__)
   200000    0.706    0.000   13.645    0.000 database.py:292(__getitem__)
   200000    5.254    0.000   12.939    0.000 collection.py:82(__init__)
   200000    7.448    0.000   12.266    0.000 {built-in method pymongo._cmessage._op_msg}
   200000    1.050    0.000   12.024    0.000 mongo_client.py:1232(_get_topology)
   200000    0.686    0.000   11.734    0.000 mongo_client.py:1808(_ensure_session)
   200000    3.100    0.000   11.604    0.000 pool.py:1303(return_socket)
   200000    1.451    0.000   11.580    0.000 topology.py:174(select_servers)
   200000    2.328    0.000   11.048    0.000 mongo_client.py:1756(__start_session)
  2000000    3.744    0.000    9.104    0.000 {built-in method builtins.isinstance}
   200000    2.595    0.000    8.803    0.000 pool.py:1246(_get_socket)
   200000    1.058    0.000    8.474    0.000 topology.py:145(open)
  1600000    3.891    0.000    8.414    0.000 abc.py:96(__instancecheck__)
   200000    0.624    0.000    8.309    0.000 client_session.py:362(end_session)
   200000    1.119    0.000    7.835    0.000 son.py:40(__init__)
   200000    1.763    0.000    7.736    0.000 topology.py:205(_select_servers_loop)
   200000    0.991    0.000    7.686    0.000 client_session.py:369(_end_session)
   200000    1.589    0.000    7.215    0.000 mongo_client.py:1860(_process_response)
   200000    1.089    0.000    7.121    0.000 topology.py:532(_ensure_opened)
   200000    7.009    0.000    7.009    0.000 {method 'sendall' of '_socket.socket' objects}
   400000    2.858    0.000    6.716    0.000 son.py:135(update)
   200000    0.613    0.000    6.569    0.000 mongo_client.py:1800(_get_server_session)
   200000    0.705    0.000    6.012    0.000 thread_util.py:81(release)
   200000    1.348    0.000    5.956    0.000 topology.py:488(get_server_session)
   200000    0.639    0.000    5.915    0.000 mongo_client.py:1804(_return_server_session)
   400000    1.656    0.000    5.840    0.000 periodic_executor.py:57(open)
  1400000    4.026    0.000    5.709    0.000 son.py:57(__setitem__)
   200000    2.134    0.000    5.566    0.000 client_session.py:787(_apply_to)


