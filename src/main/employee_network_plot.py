# Imports and initialize dictionaries
#### Imports
import sys
import json
import networkx as nx
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
plt.rc('figure', figsize=[16,16])
#### Initialize dictionaries
sys.path.append('/Users/petermyers/Desktop/New_Code/employee_network_plot/src/main')
from employeemappings.employeemappings import Config

def draw_graph(year='2019', color_by='department'):
    # Initialize
    G = nx.Graph(k=0.8,iterations=50)
    job_titles, locations, names, department_names, edge_list = [], [], [], [], []
    date = datetime.strptime('{}-12-31'.format(year), '%Y-%m-%d')
    department_nodes = {}
    for department in Config.departments:
        department_nodes[department] = []
    location_nodes = {}
    for location in Config.location_nodes:
        location_nodes[location] = []

    # Read file
    with open('../../data/raw/data.json') as json_file:
        data = json.load(json_file)
        G.add_node("Top position")
        for person1 in data['directReports']:
            if date > datetime.strptime(person1['hireDate'], '%Y-%m-%d'):
                job_titles.append(person1['jobTitle'])
                locations.append(Config.location_mapping[person1['location']])
                department_names.append(str(person1['departmentName']))
                G.add_node(person1['name'])
                department_nodes[str(person1['departmentName'])].append(person1['name'])
                location_nodes[Config.location_mapping[person1['location']]].append(person1['name'])
                G.add_edge(person1['name'], "Top position")
                person1_name = person1['name']
            else:
                person1_name = "Top position"
            names.append(person1_name)
            for person2 in person1['directReports']:
                if date > datetime.strptime(person2['hireDate'], '%Y-%m-%d'):
                    job_titles.append(person2['jobTitle'])
                    locations.append(Config.location_mapping[person2['location']])
                    department_names.append(str(person2['departmentName']))
                    G.add_node(person2['name'])
                    department_nodes[str(person2['departmentName'])].append(person2['name'])
                    location_nodes[Config.location_mapping[person2['location']]].append(person2['name'])
                    G.add_edge(person2['name'], person1_name)
                    person2_name = person2['name']
                else:
                    person2_name = person1['name'] if date > datetime.strptime(person1['hireDate'], '%Y-%m-%d') else "Top position"
                names.append(person2_name)
                for person3 in person2['directReports']:
                    if date > datetime.strptime(person3['hireDate'], '%Y-%m-%d'):
                        job_titles.append(person3['jobTitle'])
                        locations.append(Config.location_mapping[person3['location']])
                        department_names.append(str(person3['departmentName']))
                        G.add_node(person3['name'])
                        department_nodes[str(person3['departmentName'])].append(person3['name'])
                        location_nodes[Config.location_mapping[person3['location']]].append(person3['name'])
                        G.add_edge(person3['name'], person2_name)
                        person3_name = person3['name']
                    else:
                        person3_name = person2['name'] if date > datetime.strptime(person2['hireDate'], '%Y-%m-%d') else person1['name'] if date > datetime.strptime(person1['hireDate'], '%Y-%m-%d') else "Top position"
                    names.append(person3_name)
                    for person4 in person3['directReports']:
                        if date > datetime.strptime(person4['hireDate'], '%Y-%m-%d'):
                            job_titles.append(person4['jobTitle'])
                            locations.append(Config.location_mapping[person4['location']])
                            department_names.append(str(person4['departmentName']))
                            G.add_node(person4['name'])
                            department_nodes[str(person4['departmentName'])].append(person4['name'])
                            location_nodes[Config.location_mapping[person4['location']]].append(person4['name'])
                            G.add_edge(person4['name'], person3_name)
                            person4_name = person4['name']
                        else:
                            person4_name = person3['name'] if date > datetime.strptime(person3['hireDate'], '%Y-%m-%d') else person2['name'] if date > datetime.strptime(person2['hireDate'], '%Y-%m-%d') else person1['name'] if date > datetime.strptime(person1['hireDate'], '%Y-%m-%d') else "Top position"
                        names.append(person4_name)
                        for person5 in person4['directReports']:
                            if date > datetime.strptime(person5['hireDate'], '%Y-%m-%d'):
                                job_titles.append(person5['jobTitle'])
                                locations.append(Config.location_mapping[person5['location']])
                                department_names.append(str(person5['departmentName']))
                                G.add_node(person5['name'])
                                department_nodes[str(person5['departmentName'])].append((person5['name']))
                                location_nodes[Config.location_mapping[person5['location']]].append(person5['name'])
                                G.add_edge(person5['name'], person4_name)
                                person5_name = person5['name']
                            else:
                                person5_name = person4['name'] if date > datetime.strptime(person4['hireDate'], '%Y-%m-%d') else person3['name'] if date > datetime.strptime(person3['hireDate'], '%Y-%m-%d') else person2['name'] if date > datetime.strptime(person2['hireDate'], '%Y-%m-%d') else person1['name'] if date > datetime.strptime(person1['hireDate'], '%Y-%m-%d') else "Top position"
                            names.append(person5_name)

    # Color
    ### By department
    if color_by == "location":
        for location in location_nodes.keys():
            for person_name in location_nodes[location]:
                G.nodes[person_name]['color'] = Config.location_color_mapping[location]
        legend_elements = [Line2D([0], [0], marker='o', color='#b5a265', label='Location 1',
                                  markerfacecolor='#b5a265', markersize=15),
                           Line2D([0], [0], marker='o', color='#d43a2f', label='Location 2',
                                  markerfacecolor='#d43a2f', markersize=15),
                           Line2D([0], [0], marker='o', color='#b5abaa', label='Location 3',
                                  markerfacecolor='#b5abaa', markersize=15),
                           Line2D([0], [0], marker='o', color='#150782', label='Location 4',
                                  markerfacecolor='#150782', markersize=15),
                           Line2D([0], [0], marker='o', color='#17cf0a', label='Location 5',
                                  markerfacecolor='#17cf0a', markersize=15),
                           Line2D([0], [0], marker='o', color='#faf619', label='Location 6',
                                  markerfacecolor='#faf619', markersize=15),
                           Line2D([0], [0], marker='o', color='#ffb700', label='Location 7',
                                  markerfacecolor='#ffb700', markersize=15),
                           Line2D([0], [0], marker='o', color='#07deed', label='Location 8',
                                  markerfacecolor='#07deed', markersize=15),
                           Line2D([0], [0], marker='o', color='#e3d698', label='Location 9',
                                  markerfacecolor='#e3d698', markersize=15),
                           Line2D([0], [0], marker='o', color='#bf08fc', label='Location 10',
                                  markerfacecolor='#bf08fc', markersize=15)]
    else:
        for department in department_nodes.keys():
            for person_name in department_nodes[department]:
                G.nodes[person_name]['color'] = Config.department_color_mapping[department]
        legend_elements = [Line2D([0], [0], marker='o', color='#b5a265', label='Department 1',
                                  markerfacecolor='#b5a265', markersize=15),
                           Line2D([0], [0], marker='o', color='#d43a2f', label='Department 2',
                                  markerfacecolor='#d43a2f', markersize=15),
                           Line2D([0], [0], marker='o', color='#b5abaa', label='Department 3',
                                  markerfacecolor='#b5abaa', markersize=15),
                           Line2D([0], [0], marker='o', color='#150782', label='Department 4',
                                  markerfacecolor='#150782', markersize=15),
                           Line2D([0], [0], marker='o', color='#17cf0a', label='Department 5',
                                  markerfacecolor='#17cf0a', markersize=15),
                           Line2D([0], [0], marker='o', color='#faf619', label='Department 6',
                                  markerfacecolor='#faf619', markersize=15),
                           Line2D([0], [0], marker='o', color='#ffb700', label='Department 7',
                                  markerfacecolor='#ffb700', markersize=15),
                           Line2D([0], [0], marker='o', color='#07deed', label='Department 8',
                                  markerfacecolor='#07deed', markersize=15),
                           Line2D([0], [0], marker='o', color='#e3d698', label='Department 9',
                                  markerfacecolor='#e3d698', markersize=15)]
    G.nodes['Top position']['color'] = '#b5abaa'
    colors = [node[1]['color'] for node in G.nodes(data=True)]

    # Plot and save
    nx.draw(G, with_labels=False, node_color=colors)
    plt.legend(handles=legend_elements, loc='fit')
    plt.savefig('../../data/output/{}_graph_{}.png'.format(color_by, year))
    G.clear()
    plt.clf()

# Execute
for year in range(2007, 2020):
    print("Saving graphs for year", year, "in data/output/")
    draw_graph(str(year), "department")
    draw_graph(str(year), "location")
