Modified Chord
Modified Chord is a distributed peer-to-peer system based on the classic Chord protocol for efficient key lookup in a decentralized network. This version introduces enhancements to improve performance, scalability, and fault tolerance.

Features
  Improved Finger Table Maintenance
  Faster Lookup via Optimized Routing
  Resilient to Node Failures
  Support for Dynamic Node Joins and Leaves
  Optional Secure Communication (via TLS)
  Adaptive finger table layers for traffic conditions



Each node in the Modified Chord ring maintains:

A unique node_id (typically a SHA-1 hash)

A multi layered finger table for routing

Successor and predecessor pointers

A replicated storage cache 

Enhancements
Adaptive Stabilization: Dynamically adjusts stabilization frequency based on network churn.

Redundant Successor List: Increases resilience against node failures.

Load Balancing: Evenly redistributes keys when nodes join or leave.

Faster Lookups: Optimized finger selection for reduced hops.


License
This project is licensed under the MIT License. See the LICENSE file for details.
