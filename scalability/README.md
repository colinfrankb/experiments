# Scalability

- Dimensions measuring the ability to scale
  - Handling more data
    - Effeciently handle processing more data
  - Handling higher concurrency levels
    - Concurrency measures how many clients your system can serve at the same time
  - Handling higher interaction rates
    - Rate of interactions between your system and your clients
    - The rate of interactions measure how often your clients exchange information with your servers.

## Objective

I want to be able to scale the concurrency of a http web server

## Outcome

- When using Gunicorn's pre-fork worker model
  - HTTP Requests are processed synchronously
  - This meant that as I increased the number of users more than the number of gunicorn workers, the latency of the request increased, and the number of requests per second decreased
  - Meaning it did not scale
- Using gevent
  - http://www.gevent.org/
  - This uses Asynchronous Processing
  - As the number of users increased more than the number of gunicorn workers, the latency remained constant and the number of requests per second remained constant
  - Meaning it did scale