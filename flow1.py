from graphviz import Digraph

# Create Digraph object
flowchart = Digraph(format='png')

# Add nodes and edges
flowchart.node('A', 'Gather Network Data')
flowchart.node('B', 'Conduct Performance Analysis')
flowchart.node('C', 'Identify Bottlenecks')
flowchart.node('D', 'Generate Reports')

flowchart.edges(['AB', 'BC', 'CD'])

# Render and save the flow chart
flowchart.render('wireless_network_analysis_flowchart', view=True)
