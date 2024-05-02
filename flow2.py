from graphviz import Digraph

# Create Digraph object
flowchart = Digraph(format='png')

# Add nodes and edges
flowchart.node('A', 'Analyze Interference Sources')
flowchart.node('B', 'Optimize Channel Allocation')
flowchart.node('C', 'Adjust Transmission Power')
flowchart.node('D', 'Evaluate Improvements')

flowchart.edges(['AB', 'BC', 'CD'])

# Render and save the flow chart
flowchart.render('network_optimization_flowchart', view=True)
