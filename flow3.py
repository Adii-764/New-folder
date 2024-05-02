from graphviz import Digraph

# Create Digraph object
flowchart = Digraph(format='png')

# Add nodes and edges
flowchart.node('A', 'Define QoS Policies')
flowchart.node('B', 'Prioritize Traffic Types')
flowchart.node('C', 'Implement Traffic Shaping')
flowchart.node('D', 'Monitor QoS Metrics')

flowchart.edges(['AB', 'BC', 'CD'])

# Render and save the flow chart
flowchart.render('qos_flowchart', view=True)
