         1119 function calls (1103 primitive calls) in 0.081 seconds

   Ordered by: cumulative time
   List reduced from 286 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.081    0.081 main.py:138(delete_user)
        1    0.000    0.000    0.081    0.081 users.py:60(delete_user)
        2    0.000    0.000    0.078    0.039 collection.py:1185(_delete_retryable)
        2    0.000    0.000    0.078    0.039 mongo_client.py:1495(_retryable_write)
        2    0.000    0.000    0.078    0.039 mongo_client.py:1374(_retry_with_session)
        2    0.000    0.000    0.078    0.039 mongo_client.py:1386(_retry_internal)
        2    0.000    0.000    0.077    0.039 collection.py:1190(_delete)
        2    0.000    0.000    0.077    0.039 collection.py:1129(_delete)
        1    0.000    0.000    0.077    0.077 collection.py:1245(delete_many)
        2    0.000    0.000    0.077    0.039 pool.py:612(command)
        2    0.000    0.000    0.077    0.038 network.py:43(command)
        3    0.000    0.000    0.077    0.026 network.py:186(receive_message)
        6    0.000    0.000    0.077    0.013 network.py:279(_receive_data_on_socket)
        6    0.076    0.013    0.076    0.013 {method 'recv_into' of '_socket.socket' objects}
        1    0.000    0.000    0.002    0.002 collection.py:1289(find_one)
        1    0.000    0.000    0.001    0.001 cursor.py:1203(next)
        1    0.000    0.000    0.001    0.001 cursor.py:1089(_refresh)
        1    0.000    0.000    0.001    0.001 collection.py:1201(delete_one)
        1    0.000    0.000    0.001    0.001 cursor.py:983(__send_message)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1332(_run_operation_with_response)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1443(_retryable_read)
    23/15    0.000    0.000    0.001    0.000 {built-in method builtins.next}
        1    0.000    0.000    0.001    0.001 mongo_client.py:1359(_cmd)
        1    0.000    0.000    0.001    0.001 server.py:70(run_operation_with_response)
        6    0.000    0.000    0.001    0.000 mongo_client.py:1243(_get_socket)
        1    0.000    0.000    0.001    0.001 _logger.py:1969(info)
      9/5    0.000    0.000    0.001    0.000 contextlib.py:108(__enter__)
        1    0.000    0.000    0.000    0.000 _logger.py:1841(_log)
        3    0.000    0.000    0.000    0.000 mongo_client.py:1257(_select_server)
      9/5    0.000    0.000    0.000    0.000 contextlib.py:117(__exit__)
        6    0.000    0.000    0.000    0.000 pool.py:1204(get_socket)
        3    0.000    0.000    0.000    0.000 message.py:692(_op_msg)
        1    0.000    0.000    0.000    0.000 pool.py:718(receive_message)
        1    0.000    0.000    0.000    0.000 _handler.py:98(emit)
        3    0.000    0.000    0.000    0.000 database.py:278(__getattr__)
        3    0.000    0.000    0.000    0.000 topology.py:236(select_server)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1296(_slaveok_for_server)
        3    0.000    0.000    0.000    0.000 database.py:292(__getitem__)
        3    0.000    0.000    0.000    0.000 collection.py:82(__init__)
        1    0.000    0.000    0.000    0.000 message.py:329(get_message)
        1    0.000    0.000    0.000    0.000 {method 'format_map' of 'str' objects}
        4    0.000    0.000    0.000    0.000 mongo_client.py:1232(_get_topology)
        4    0.000    0.000    0.000    0.000 mongo_client.py:1821(_tmp_session)
        1    0.000    0.000    0.000    0.000 _datetime.py:13(__format__)
        3    0.000    0.000    0.000    0.000 {built-in method pymongo._cmessage._op_msg}
        3    0.000    0.000    0.000    0.000 pool.py:1303(return_socket)
        3    0.000    0.000    0.000    0.000 mongo_client.py:1808(_ensure_session)
        3    0.000    0.000    0.000    0.000 mongo_client.py:1756(__start_session)
        3    0.000    0.000    0.000    0.000 topology.py:174(select_servers)
        4    0.000    0.000    0.000    0.000 topology.py:145(open)


