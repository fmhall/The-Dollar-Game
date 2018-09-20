def get_node(G) :
    while 1 :
        node_num = input('Which node do you want give money from?')
        if node_num == 'e' :
            exit()
        if int(node_num) in range(0,len(G.nodes)) :
            return node_num
        else :
            print('That index doesnt exist! Try again.')