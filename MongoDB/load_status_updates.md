         67002855 function calls (66202855 primitive calls) in 293.282 seconds

   Ordered by: cumulative time
   List reduced from 204 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.564    2.564  293.282  293.282 main.py:72(load_status_updates)
   200000    2.682    0.000  270.584    0.001 collection.py:654(insert_one)
   200000    1.262    0.000  260.255    0.001 collection.py:608(_insert)
   200000    3.984    0.000  257.720    0.001 collection.py:559(_insert_one)
   200000    1.782    0.000  241.309    0.001 mongo_client.py:1495(_retryable_write)
   200000    1.524    0.000  213.825    0.001 mongo_client.py:1374(_retry_with_session)
   200000    4.061    0.000  210.452    0.001 mongo_client.py:1386(_retry_internal)
   200000    1.864    0.000  132.838    0.001 collection.py:578(_insert_command)
   200000    4.286    0.000  129.180    0.001 pool.py:612(command)
   200000    5.989    0.000  114.518    0.001 network.py:43(command)
   200000    2.833    0.000   63.977    0.000 network.py:186(receive_message)
1800002/1400002    5.405    0.000   60.758    0.000 {built-in method builtins.next}
   400000    3.619    0.000   57.229    0.000 network.py:279(_receive_data_on_socket)
   400000   52.901    0.000   52.901    0.000 {method 'recv_into' of '_socket.socket' objects}
   400000    3.132    0.000   34.332    0.000 mongo_client.py:1243(_get_socket)
600000/400000    1.678    0.000   33.244    0.000 contextlib.py:108(__enter__)
   200000    2.055    0.000   31.873    0.000 mongo_client.py:1257(_select_server)
600000/400000    2.157    0.000   27.369    0.000 contextlib.py:117(__exit__)
   400000    1.730    0.000   22.942    0.000 pool.py:1204(get_socket)
   200000    3.540    0.000   22.920    0.000 message.py:692(_op_msg)
   400000    1.340    0.000   21.594    0.000 mongo_client.py:1821(_tmp_session)
   200000    1.120    0.000   16.084    0.000 topology.py:236(select_server)
   200000    0.985    0.000   15.213    0.000 database.py:278(__getattr__)
   200000    0.727    0.000   13.918    0.000 database.py:292(__getitem__)
   200000    5.219    0.000   13.191    0.000 collection.py:82(__init__)
   200000    7.763    0.000   12.642    0.000 {built-in method pymongo._cmessage._op_msg}
   200000    1.124    0.000   12.333    0.000 mongo_client.py:1232(_get_topology)
   200000    3.299    0.000   12.097    0.000 pool.py:1303(return_socket)
   200000    0.706    0.000   11.826    0.000 mongo_client.py:1808(_ensure_session)
   200000    1.503    0.000   11.783    0.000 topology.py:174(select_servers)
   200000    2.318    0.000   11.119    0.000 mongo_client.py:1756(__start_session)
  2000000    3.797    0.000    9.218    0.000 {built-in method builtins.isinstance}
   200000    2.620    0.000    8.834    0.000 pool.py:1246(_get_socket)
   200000    1.094    0.000    8.723    0.000 topology.py:145(open)
  1600000    3.943    0.000    8.521    0.000 abc.py:96(__instancecheck__)
   200000    0.641    0.000    8.428    0.000 client_session.py:362(end_session)
   200000    1.185    0.000    7.945    0.000 son.py:40(__init__)
   200000    1.794    0.000    7.856    0.000 topology.py:205(_select_servers_loop)
   200000    1.014    0.000    7.787    0.000 client_session.py:369(_end_session)
   200000    7.426    0.000    7.426    0.000 {method 'sendall' of '_socket.socket' objects}
   200000    1.120    0.000    7.324    0.000 topology.py:532(_ensure_opened)
   200000    1.569    0.000    7.265    0.000 mongo_client.py:1860(_process_response)
   400000    2.868    0.000    6.760    0.000 son.py:135(update)
   200000    0.705    0.000    6.589    0.000 mongo_client.py:1800(_get_server_session)
   200000    0.732    0.000    6.169    0.000 thread_util.py:81(release)
   200000    0.651    0.000    5.986    0.000 mongo_client.py:1804(_return_server_session)
   400000    1.712    0.000    5.979    0.000 periodic_executor.py:57(open)
  1400000    4.190    0.000    5.890    0.000 son.py:57(__setitem__)
   200000    1.343    0.000    5.884    0.000 topology.py:488(get_server_session)
   200000    2.124    0.000    5.633    0.000 client_session.py:787(_apply_to)


