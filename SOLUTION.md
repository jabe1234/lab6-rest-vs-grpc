
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	|   3.631ms	|   4.977	|  312.234	|
|   gRPC add	|   1.064ms	|   1.428	|    151.081	|
|   REST rawimg	|   6.681ms	|   11.178	|   1228.954	|
|   gRPC rawimg	|   7.759ms    |  11.393 	|   188.346	|
|   REST dotproduct	|   5.023ms	|   6.018	|  308.0343	|
|   gRPC dotproduct	|   1.210ms	|   1.508	|    158.293	|
|   REST jsonimg	|   67.390ms	|   75.404	|   1472.988	|
|   gRPC jsonimg	|   64.746ms    |   69.005	|   249.784	|
|   PING        |   0.044ms    |   0.346   |    146.187   |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.


It seems that grpc often offers a much faster latency for most use cases compared to rest. The only case where grpc took longer than rest was the rawImage when the client and server are close in proximity. grpc and rest are much closer in speed when the client and server are close in proximity while grpc gains a much bigger performance comparative increase when the client and server are far away from each other. This is likley because of the handshake that happens for every rest connection vs the one time handshake for the grpc connection before any requests are made.