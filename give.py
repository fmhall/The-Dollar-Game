def give(graph, node_num) :
    neighbor_dict = graph[node_num]
    #neighbor_list = graph.neighbors(node_num)
    nbers = len(neighbor_dict)
    #nbersl = len(neighbor_list)
    money = graph.node[node_num]['value']
    print('node: ' + str(node_num))
    print('money before give: ' + str(money))
    print('# of neighbors: ' + str(nbers))
    print('neighbor dictionary: ' + str(neighbor_dict))

    for node in neighbor_dict :
        print(graph.node[node]['value'])
    
    print('----transferring money ----')

    for node in neighbor_dict :
        graph.node[node]['value'] += 1
        graph.node[node_num]['value'] -= 1
    
    for node in neighbor_dict :
        print(graph.node[node])
    
    money = graph.node[node_num]['value']
    print('money after give: ' + str(money))