         1184 function calls (1164 primitive calls) in 0.005 seconds

   Ordered by: cumulative time
   List reduced from 288 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 main.py:175(update_status)
        1    0.000    0.000    0.005    0.005 user_status.py:46(modify_status)
        2    0.000    0.000    0.003    0.002 collection.py:1289(find_one)
        2    0.000    0.000    0.003    0.002 cursor.py:1203(next)
        2    0.000    0.000    0.003    0.002 cursor.py:1089(_refresh)
        2    0.000    0.000    0.003    0.001 cursor.py:983(__send_message)
        2    0.000    0.000    0.003    0.001 mongo_client.py:1332(_run_operation_with_response)
        2    0.000    0.000    0.003    0.001 mongo_client.py:1443(_retryable_read)
        2    0.000    0.000    0.002    0.001 mongo_client.py:1359(_cmd)
        2    0.000    0.000    0.002    0.001 server.py:70(run_operation_with_response)
        1    0.000    0.000    0.001    0.001 collection.py:950(update_one)
        1    0.000    0.000    0.001    0.001 collection.py:852(_update_retryable)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1495(_retryable_write)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1374(_retry_with_session)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1386(_retry_internal)
        3    0.000    0.000    0.001    0.000 network.py:186(receive_message)
        6    0.000    0.000    0.001    0.000 network.py:279(_receive_data_on_socket)
    23/13    0.000    0.000    0.001    0.000 {built-in method builtins.next}
        6    0.001    0.000    0.001    0.000 {method 'recv_into' of '_socket.socket' objects}
        1    0.000    0.000    0.001    0.001 collection.py:859(_update)
        1    0.000    0.000    0.001    0.001 collection.py:764(_update)
        2    0.000    0.000    0.001    0.000 pool.py:718(receive_message)
        1    0.000    0.000    0.001    0.001 pool.py:612(command)
        1    0.000    0.000    0.001    0.001 network.py:43(command)
      9/4    0.000    0.000    0.001    0.000 contextlib.py:108(__enter__)
        4    0.000    0.000    0.001    0.000 mongo_client.py:1296(_slaveok_for_server)
        2    0.000    0.000    0.001    0.000 message.py:329(get_message)
        6    0.000    0.000    0.001    0.000 mongo_client.py:1243(_get_socket)
        3    0.000    0.000    0.001    0.000 mongo_client.py:1257(_select_server)
        3    0.000    0.000    0.000    0.000 message.py:692(_op_msg)
        1    0.000    0.000    0.000    0.000 _logger.py:1969(info)
        1    0.000    0.000    0.000    0.000 _logger.py:1841(_log)
        6    0.000    0.000    0.000    0.000 pool.py:1204(get_socket)
      9/4    0.000    0.000    0.000    0.000 contextlib.py:117(__exit__)
        5    0.000    0.000    0.000    0.000 mongo_client.py:1232(_get_topology)
        3    0.000    0.000    0.000    0.000 topology.py:236(select_server)
        2    0.000    0.000    0.000    0.000 message.py:294(as_command)
        3    0.000    0.000    0.000    0.000 database.py:278(__getattr__)
        3    0.000    0.000    0.000    0.000 {built-in method pymongo._cmessage._op_msg}
        3    0.000    0.000    0.000    0.000 mongo_client.py:1808(_ensure_session)
        1    0.000    0.000    0.000    0.000 _handler.py:98(emit)
        3    0.000    0.000    0.000    0.000 database.py:292(__getitem__)
        3    0.000    0.000    0.000    0.000 mongo_client.py:1756(__start_session)
        5    0.000    0.000    0.000    0.000 topology.py:145(open)
        3    0.000    0.000    0.000    0.000 collection.py:82(__init__)
        3    0.000    0.000    0.000    0.000 topology.py:174(select_servers)
        5    0.000    0.000    0.000    0.000 topology.py:532(_ensure_opened)
        3    0.000    0.000    0.000    0.000 pool.py:1303(return_socket)
        1    0.000    0.000    0.000    0.000 {method 'format_map' of 'str' objects}
       10    0.000    0.000    0.000    0.000 periodic_executor.py:57(open)


