         410 function calls (406 primitive calls) in 0.002 seconds

   Ordered by: cumulative time
   List reduced from 240 to 50 due to restriction <50>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 main.py:109(add_user)
        1    0.000    0.000    0.002    0.002 users.py:25(add_user)
        1    0.000    0.000    0.001    0.001 collection.py:654(insert_one)
        1    0.000    0.000    0.001    0.001 collection.py:608(_insert)
        1    0.000    0.000    0.001    0.001 collection.py:559(_insert_one)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1495(_retryable_write)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1374(_retry_with_session)
        1    0.000    0.000    0.001    0.001 mongo_client.py:1386(_retry_internal)
        1    0.000    0.000    0.001    0.001 collection.py:578(_insert_command)
        1    0.000    0.000    0.001    0.001 pool.py:612(command)
        1    0.000    0.000    0.001    0.001 network.py:43(command)
        1    0.000    0.000    0.000    0.000 _logger.py:1969(info)
        1    0.000    0.000    0.000    0.000 _logger.py:1841(_log)
      8/6    0.000    0.000    0.000    0.000 {built-in method builtins.next}
        1    0.000    0.000    0.000    0.000 network.py:186(receive_message)
        2    0.000    0.000    0.000    0.000 network.py:279(_receive_data_on_socket)
        2    0.000    0.000    0.000    0.000 {method 'recv_into' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 _handler.py:98(emit)
      3/2    0.000    0.000    0.000    0.000 contextlib.py:108(__enter__)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1243(_get_socket)
        1    0.000    0.000    0.000    0.000 mongo_client.py:1257(_select_server)
        1    0.000    0.000    0.000    0.000 {method 'format_map' of 'str' objects}
      3/2    0.000    0.000    0.000    0.000 contextlib.py:117(__exit__)
        1    0.000    0.000    0.000    0.000 _datetime.py:13(__format__)
        2    0.000    0.000    0.000    0.000 mongo_client.py:1821(_tmp_session)
        2    0.000    0.000    0.000    0.000 pool.py:1204(get_socket)
        1    0.000    0.000    0.000    0.000 message.py:692(_op_msg)
        1    0.000    0.000    0.000    0.000 topology.py:236(select_server)
        1    0.000    0.000    0.000    0.000 mongo_client.py:1808(_ensure_session)
        1    0.000    0.000    0.000    0.000 database.py:278(__getattr__)
        1    0.000    0.000    0.000    0.000 mongo_client.py:1756(__start_session)
        1    0.000    0.000    0.000    0.000 database.py:292(__getitem__)
        1    0.000    0.000    0.000    0.000 collection.py:82(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method pymongo._cmessage._op_msg}
        1    0.000    0.000    0.000    0.000 mongo_client.py:1232(_get_topology)
        1    0.000    0.000    0.000    0.000 pool.py:1303(return_socket)
        1    0.000    0.000    0.000    0.000 topology.py:174(select_servers)
       16    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 pool.py:1246(_get_socket)
        1    0.000    0.000    0.000    0.000 topology.py:145(open)
        1    0.000    0.000    0.000    0.000 mongo_client.py:1800(_get_server_session)
        1    0.000    0.000    0.000    0.000 {method 'sendall' of '_socket.socket' objects}
        1    0.000    0.000    0.000    0.000 topology.py:488(get_server_session)
        8    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
        1    0.000    0.000    0.000    0.000 {method 'sub' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 son.py:40(__init__)
        1    0.000    0.000    0.000    0.000 topology.py:205(_select_servers_loop)
        1    0.000    0.000    0.000    0.000 client_session.py:362(end_session)
        1    0.000    0.000    0.000    0.000 topology.py:532(_ensure_opened)
        1    0.000    0.000    0.000    0.000 _datetime.py:81(aware_now)


