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
