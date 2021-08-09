         670003 function calls (662003 primitive calls) in 2.817 seconds

   Ordered by: cumulative time
   List reduced from 204 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.024    0.024    2.817    2.817 main.py:37(load_users)
     2000    0.026    0.000    2.597    0.001 collection.py:654(insert_one)
     2000    0.012    0.000    2.495    0.001 collection.py:608(_insert)
     2000    0.038    0.000    2.470    0.001 collection.py:559(_insert_one)
     2000    0.018    0.000    2.312    0.001 mongo_client.py:1495(_retryable_write)
     2000    0.015    0.000    2.044    0.001 mongo_client.py:1374(_retry_with_session)
     2000    0.038    0.000    2.011    0.001 mongo_client.py:1386(_retry_internal)
     2000    0.018    0.000    1.262    0.001 collection.py:578(_insert_command)
     2000    0.041    0.000    1.227    0.001 pool.py:612(command)
     2000    0.058    0.000    1.085    0.001 network.py:43(command)
     2000    0.025    0.000    0.601    0.000 network.py:186(receive_message)
18002/14002    0.051    0.000    0.587    0.000 {built-in method builtins.next}
     4000    0.032    0.000    0.539    0.000 network.py:279(_receive_data_on_socket)
     4000    0.500    0.000    0.500    0.000 {method 'recv_into' of '_socket.socket' objects}
     4000    0.030    0.000    0.331    0.000 mongo_client.py:1243(_get_socket)
6000/4000    0.016    0.000    0.324    0.000 contextlib.py:108(__enter__)
     2000    0.020    0.000    0.310    0.000 mongo_client.py:1257(_select_server)
6000/4000    0.021    0.000    0.262    0.000 contextlib.py:117(__exit__)
     2000    0.034    0.000    0.222    0.000 message.py:692(_op_msg)
     4000    0.016    0.000    0.220    0.000 pool.py:1204(get_socket)
     4000    0.013    0.000    0.210    0.000 mongo_client.py:1821(_tmp_session)
     2000    0.011    0.000    0.157    0.000 topology.py:236(select_server)
     2000    0.009    0.000    0.149    0.000 database.py:278(__getattr__)
     2000    0.007    0.000    0.136    0.000 database.py:292(__getitem__)
     2000    0.052    0.000    0.129    0.000 collection.py:82(__init__)
     2000    0.073    0.000    0.121    0.000 {built-in method pymongo._cmessage._op_msg}
     2000    0.010    0.000    0.119    0.000 mongo_client.py:1232(_get_topology)
     2000    0.007    0.000    0.116    0.000 mongo_client.py:1808(_ensure_session)
     2000    0.014    0.000    0.115    0.000 topology.py:174(select_servers)
     2000    0.030    0.000    0.115    0.000 pool.py:1303(return_socket)
     2000    0.023    0.000    0.109    0.000 mongo_client.py:1756(__start_session)
    20000    0.037    0.000    0.090    0.000 {built-in method builtins.isinstance}
     2000    0.026    0.000    0.087    0.000 pool.py:1246(_get_socket)
     2000    0.010    0.000    0.084    0.000 topology.py:145(open)
    16000    0.039    0.000    0.083    0.000 abc.py:96(__instancecheck__)
     2000    0.006    0.000    0.082    0.000 client_session.py:362(end_session)
     2000    0.011    0.000    0.078    0.000 son.py:40(__init__)
     2000    0.018    0.000    0.077    0.000 topology.py:205(_select_servers_loop)
     2000    0.010    0.000    0.076    0.000 client_session.py:369(_end_session)
     2000    0.015    0.000    0.071    0.000 mongo_client.py:1860(_process_response)
     2000    0.011    0.000    0.071    0.000 topology.py:532(_ensure_opened)
     2000    0.067    0.000    0.067    0.000 {method 'sendall' of '_socket.socket' objects}
     4000    0.028    0.000    0.066    0.000 son.py:135(update)
     2000    0.006    0.000    0.065    0.000 mongo_client.py:1800(_get_server_session)
     2000    0.007    0.000    0.060    0.000 thread_util.py:81(release)
     2000    0.013    0.000    0.059    0.000 topology.py:488(get_server_session)
     2000    0.006    0.000    0.058    0.000 mongo_client.py:1804(_return_server_session)
     4000    0.017    0.000    0.058    0.000 periodic_executor.py:57(open)
    14000    0.040    0.000    0.056    0.000 son.py:57(__setitem__)
     2000    0.021    0.000    0.055    0.000 client_session.py:787(_apply_to)


