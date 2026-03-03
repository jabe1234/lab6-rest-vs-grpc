
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	|   0.95ms	|   	|  	|
|   gRPC add	|   0.155ms	|   	|    	|
|   REST rawimg	|   2.82ms	|   	|   	|
|   gRPC rawimg	|   2.520ms    |   	|   	|
|   REST dotproduct	|   1.211ms	|   	|  	|
|   gRPC dotproduct	|   0.171ms	|   	|    	|
|   REST jsonimg	|   18.69ms	|   	|   	|
|   gRPC jsonimg	|   17.549ms    |   	|   	|
|   PING        |   0.285ms    |      |       |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.