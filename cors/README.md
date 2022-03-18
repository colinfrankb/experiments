- Abstract
  - Show that Same-origin policy is a browser feature
- Experiment
  - Create and run two servers that represent two different HTTP origins
  - From the one server return a HTML document that will execute javascript to fetch a resource from the 2nd server
  - The browser should block the call
    ```
    Access to fetch at 'http://localhost:8000/numbers.json' from origin 'http://localhost:9000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
    ```
- Experiment
  - Create and run three servers to test that the javascript resource has it's origin sent to Origin C.
    - the original document that loads a script (even from a different origin), and if that script performs requests, the Origin header is set to the origin of the document not the origin of the script
