## How does logging work at first principles?

- https://docs.python.org/3/library/logging.html
- https://docs.python.org/3/howto/logging.html


## What are the components of logging?

- https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
Loggers expose the interface that application code directly uses.
Handlers send the log records (created by loggers) to the appropriate destination.
Filters provide a finer grained facility for determining which log records to output.
Formatters specify the layout of log records in the final output.

Each instance has a name, and they are conceptually arranged in a namespace hierarchy using dots (periods) as separators.

loggers work as a hierarchy in a graph, where the root logger is the root of the graph

The default logging level is WARNING

if you don't call logging.basicConfig, it will be called automatically.

basicConfig configures the root logger

## When not setting basicConfig, and setting the log level on a logger to INFO, it still didn't log the message, why not?

- Child loggers propagate messages up to the handlers associated with their ancestor loggers. Because of this, it is unnecessary to define and configure handlers for all the loggers an application uses. It is sufficient to configure handlers for a top-level logger and create child loggers as needed. (You can, however, turn off propagation by setting the propagate attribute of a logger to False.)

- https://docs.python.org/3/howto/logging.html#handler-basic

- By default, no destination is set for any logging messages.

- Therefore the logger would propogate the LogRecord to the Handler of the root which is set to WARNING, explaining why the message was not logged