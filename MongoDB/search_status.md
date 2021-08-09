         744 function calls (728 primitive calls) in 0.003 seconds

   Ordered by: cumulative time
   List reduced from 209 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 main.py:197(search_status)
        1    0.000    0.000    0.003    0.003 user_status.py:76(search_status)
        2    0.000    0.000    0.003    0.001 collection.py:1289(find_one)
        2    0.000    0.000    0.003    0.001 cursor.py:1203(next)
        2    0.000    0.000    0.003    0.001 cursor.py:1089(_refresh)
        2    0.000    0.000    0.002    0.001 cursor.py:983(__send_message)
        2    0.000    0.000    0.002    0.001 mongo_client.py:1332(_run_operation_with_response)
        2    0.000    0.000    0.002    0.001 mongo_client.py:1443(_retryable_read)
        2    0.000    0.000    0.001    0.001 mongo_client.py:1359(_cmd)
        2    0.000    0.000    0.001    0.001 server.py:70(run_operation_with_response)
        2    0.000    0.000    0.001    0.000 message.py:329(get_message)
     14/6    0.000    0.000    0.000    0.000 {built-in method builtins.next}
        4    0.000    0.000    0.000    0.000 mongo_client.py:1296(_slaveok_for_server)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1257(_select_server)
      6/2    0.000    0.000    0.000    0.000 contextlib.py:108(__enter__)
        4    0.000    0.000    0.000    0.000 mongo_client.py:1243(_get_socket)
        2    0.000    0.000    0.000    0.000 pool.py:718(receive_message)
        2    0.000    0.000    0.000    0.000 network.py:186(receive_message)
        4    0.000    0.000    0.000    0.000 mongo_client.py:1232(_get_topology)
        2    0.000    0.000    0.000    0.000 pool.py:701(send_message)
        2    0.000    0.000    0.000    0.000 message.py:692(_op_msg)
        2    0.000    0.000    0.000    0.000 {method 'sendall' of '_socket.socket' objects}
        2    0.000    0.000    0.000    0.000 message.py:294(as_command)
        4    0.000    0.000    0.000    0.000 network.py:279(_receive_data_on_socket)
        4    0.000    0.000    0.000    0.000 pool.py:1204(get_socket)
        4    0.000    0.000    0.000    0.000 topology.py:145(open)
        4    0.000    0.000    0.000    0.000 {method 'recv_into' of '_socket.socket' objects}
        2    0.000    0.000    0.000    0.000 database.py:278(__getattr__)
        2    0.000    0.000    0.000    0.000 database.py:292(__getitem__)
        2    0.000    0.000    0.000    0.000 topology.py:236(select_server)
        2    0.000    0.000    0.000    0.000 collection.py:82(__init__)
        4    0.000    0.000    0.000    0.000 topology.py:532(_ensure_opened)
        2    0.000    0.000    0.000    0.000 {built-in method pymongo._cmessage._op_msg}
      6/2    0.000    0.000    0.000    0.000 contextlib.py:117(__exit__)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1808(_ensure_session)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1756(__start_session)
        8    0.000    0.000    0.000    0.000 periodic_executor.py:57(open)
        2    0.000    0.000    0.000    0.000 collection.py:1323(find)
        2    0.000    0.000    0.000    0.000 message.py:181(_gen_find_command)
        2    0.000    0.000    0.000    0.000 topology.py:174(select_servers)
        2    0.000    0.000    0.000    0.000 cursor.py:110(__init__)
        4    0.000    0.000    0.000    0.000 server.py:44(open)
        2    0.000    0.000    0.000    0.000 pool.py:1303(return_socket)
        4    0.000    0.000    0.000    0.000 monitor.py:79(open)
        8    0.000    0.000    0.000    0.000 threading.py:1071(is_alive)
        2    0.000    0.000    0.000    0.000 pool.py:1246(_get_socket)
        2    0.000    0.000    0.000    0.000 topology.py:205(_select_servers_loop)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1800(_get_server_session)
        2    0.000    0.000    0.000    0.000 topology.py:488(get_server_session)
       30    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}


