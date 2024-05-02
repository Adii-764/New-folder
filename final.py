from graphviz import Digraph

# Create Digraph object for the second part
flowchart_part2 = Digraph(format='png')

# Define colors for different stages
colors = {
    'optimization': '#8A2BE2',  # Purple
    'implementation': '#32CD32',# Green
    'monitoring': '#FFD700'      # Yellow
}

# Define nodes and edges for the second part
nodes_edges_part2 = {
    'optimization': [('Optimize Network Topology', 'implementation'), ('Implement Quality of Service', 'implementation')],
    'implementation': [('Configure Routers and Switches', 'monitoring'), ('Set Up Security Protocols', 'monitoring')],
    'monitoring': [('Monitor Traffic and Performance', 'monitoring'), ('Perform Regular Audits', 'monitoring')]
}

# Add nodes and edges with colors for the second part
for stage, items in nodes_edges_part2.items():
    flowchart_part2.attr('node', style='filled', color=colors[stage], fontcolor='black')
    for item in items:
        flowchart_part2.node(item[0])
        flowchart_part2.edge(item[0], item[1])

# Set graph attributes for a compact layout
flowchart_part2.attr('graph', splines='ortho', nodesep='0.6', ranksep='1')

# Render and save the second part of the flow chart
flowchart_part2.render('network_flowchart_part2', view=True)
