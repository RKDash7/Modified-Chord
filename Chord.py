import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

class ChordNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.successor = None
        self.keys = []

    def set_successor(self, successor):
        self.successor = successor

    def get_successor(self):
        return self.successor

class Chord:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = self.create_nodes()
        self.assign_successors()

    def create_nodes(self):
        # Create nodes with unique IDs
        node_ids = random.sample(range(1, 2**10), self.num_nodes)
        return [ChordNode(node_id) for node_id in sorted(node_ids)]

    def assign_successors(self):
        # Assign successors in the Chord ring
        for i in range(self.num_nodes):
            self.nodes[i].set_successor(self.nodes[(i + 1) % self.num_nodes])

    def store_key(self, key):
        key_id = key % (2**4)  # Simple hash function
        responsible_node = self.get_responsible_node(key_id)
        responsible_node.keys.append(key_id)

    def get_responsible_node(self, key_id):
        # Find the responsible node for the key
        for node in self.nodes:
            if node.node_id >= key_id:
                return node
        return self.nodes[0]  # Wrap around if necessary

    def join(self, new_node_id):
        new_node = ChordNode(new_node_id)
        self.nodes.append(new_node)
        self.nodes.sort(key=lambda x: x.node_id)
        self.assign_successors()
        # Reassign keys to the new node
        for key in range(1024):  # Reassign existing keys (0 to 15)
            self.store_key(key)

    def leave(self, node_id):
        # Find the node to leave
        node_to_leave = next((node for node in self.nodes if node.node_id == node_id), None)
        if node_to_leave:
            successor = node_to_leave.get_successor()
            # Transfer keys to successor
            successor.keys.extend(node_to_leave.keys)
            self.nodes.remove(node_to_leave)
            self.assign_successors()  # Re-assign successors

    def plot(self,id):
        plt.figure(figsize=(7, 7))
        ax = plt.subplot(111, polar=True)

        # Plot nodes in a clockwise manner
        node_angles = [2 * np.pi * (node.node_id / (2 ** 10)) for node in self.nodes]
        ax.scatter(node_angles, [1] * len(self.nodes), label='Nodes', color='blue', s=100)

        # Plot keys
        for node in self.nodes:
            for key in node.keys:
                key_angle = 2 * np.pi * (key / (2 ** 10))
                ax.scatter(key_angle, [0.5], label='Keys', color='white', s=50)

        # Label the nodes
        for node in self.nodes:
            ax.text(2 * np.pi * (node.node_id / (2 ** 10)), 1.05, str(node.node_id),
                    horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')

        # Remove degree markings
        ax.set_xticks([])  # Remove x-tick labels
        ax.set_yticks([])  # Remove y-tick labels

        # Set the direction of the plot to be clockwise
        ax.set_theta_direction(-1)

        # Display settings
        #plt.title('Chord Ring Visualization with Node Labels')
        #plt.legend(loc='upper left')
        plt.savefig(f'chord_{id}.svg', dpi=2000, bbox_inches='tight')
        plt.show()
