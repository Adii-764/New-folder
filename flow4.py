from graphviz import Digraph

# Create Digraph object
flowchart = Digraph(format='png')

# Add nodes and edges
flowchart.node('A', 'Conduct Security Audit')
flowchart.node('B', 'Implement Encryption Protocols')
flowchart.node('C', 'Configure Access Control')
flowchart.node('D', 'Monitor for Anomalies')

flowchart.edges(['AB', 'BC', 'CD'])

# Render and save the flow chart
flowchart.render('security_enhancement_flowchart', view=True)
