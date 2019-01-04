# Python Ninja
Set of tricks to become a true Master of Python. Directly related with Data Science and ML tools such as tensorflow, pandas and common interfaces between them.


1. Dictionary where keys can be accessed as attributes:

        class AttrDict(dict):
          __getattr__ = dict.__getitem__
          __setattr__ = dict.__setitem__
      
     One example could be:
  
          config = AttrDict()
          config.layer_sizes = [100, 100]
          config.output_size = 10
          config.learning_rate = 1e-3
          
     The difference with an empty class with attributes? We have access to all the nice `dict` functions and properties.
     
2. Decorator to share variables across functions and methods in TF: [link to GIST.](https://gist.github.com/danijar/720394a9071a03413be8a60852374aa4) (Code also found in this repo under `code/share_variables.py`

3. Return all TF variables defined in a function:

        def define_graph(config):
          tf.reset_default_graph()
          inputs, targets = define_data_pipeline()
          prediction = my_network(inputs, config)
          loss = tf.losses.mean_squared_error(targets, prediction)
          optimizer = config.optimizer()
          optimize = optimizer.minimize(loss)
          return AttrDict(locals())  # The magic line.

     Thanks to this, we can define a graph with the following way:
         
        graph = define_graph(config)
        with tf.Session() as sess:
          sess.run(tf.global_variables_initializer())
          for _ in range(config.num_epochs):
            sess.run(graph.optimize)
          loss = sess.run(graph.loss)  # No name collision anymore.
          print(loss)
